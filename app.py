import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "menu", "room_booking","cancel","about","info","comm","show_fsm","lobby","name","date",
    "day","success","cancel2","search","request"],
    transitions=[
        {"trigger": "advance","source": "user","dest": "menu","conditions": "is_going_to_menu",},
        {"trigger": "advance","source": "user","dest": "room_booking","conditions": "is_going_to_room_booking",},
        ###開始訂房流程
        {"trigger": "advance","source": "room_booking","dest": "name","conditions": "is_going_to_name",},
        {"trigger": "advance","source": "name","dest": "date","conditions": "is_going_to_date",},
        {"trigger": "advance","source": "date","dest": "day","conditions": "is_going_to_day",},
        {"trigger": "advance","source": "day","dest": "success","conditions": "is_going_to_success",},
        {"trigger": "advance","source": "success","dest": "user",},
        ###取消訂房
        {"trigger": "go_cancel","source": ["room_booking","name","date","day"],"dest": "cancel",},
        {"trigger": "advance","source": "user","dest": "cancel","conditions": "is_going_to_cancel",},
        {"trigger": "advance","source":"cancel","dest": "cancel2","conditions": "is_going_to_cancel2",},
        {"trigger": "advance","source": "cancel2","dest": "user",},
        ###查詢訂房
        {"trigger": "advance","source": "user","dest": "search","conditions": "is_going_to_search",},
        ###其他rich menu
        {"trigger": "advance","source": "user","dest": "about","conditions": "is_going_to_about",},
        {"trigger": "advance","source": "user","dest": "info","conditions": "is_going_to_info",},
        {"trigger": "advance","source": "user","dest": "comm","conditions": "is_going_to_comm",},
        {"trigger": "advance","source": "user","dest": "show_fsm","conditions": "is_going_to_show_fsm",},
        ###其他小功能
        {"trigger": "advance","source": "user","dest": "lobby","conditions": "is_going_to_lobby",},
        {"trigger": "advance","source": "user","dest": "request","conditions": "is_going_to_request",},
        ###go back
        {"trigger": "go_back", "source": ["success","menu", "room_booking","cancel","about","info",
        "comm","show_fsm","lobby","name","date","day","cancel2","search","request"], "dest": "user"},
        
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "抱歉我看不懂QQ")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
