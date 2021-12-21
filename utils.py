import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent, ImageSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"
##關於我們
def send_about(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    
    text1 = "我們提供良好的環境及優質的住宿服務，使您有賓至如歸的感受，歡迎來體驗美好的經歷。"
    message = [
        TextSendMessage(  #旅館簡介
            text = text1
        ),
        ImageSendMessage(  #旅館圖片
            original_content_url = "https://i.imgur.com/1NSDAvo.jpg",
            preview_image_url = "https://i.imgur.com/1NSDAvo.jpg"
        ),
    ]
    line_bot_api.reply_message(reply_token,message)

    return "OK"

### 使用說明
def send_use(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    
    text1 ='''
1. 「房間預約」及「取消訂房」可預訂及取消訂房。每個 LINE 帳號只能進行一個預約記錄。
2. 「關於我們」對旅館做簡單介紹及旅館圖片。
3. 「位置資料」列出旅館地址，並會顯示地圖。
4. 「聯絡我們」可直接撥打電話與我們聯繫。

額外小功能 輸入「查看小功能」玩完其他互動
               '''
    message = TextSendMessage(
        text = text1
    )
    line_bot_api.reply_message(reply_token,message)

    return "OK"


### 位置資訊
def send_address(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    
    text1 = "成功大學店 701台南市東區大學路1號"
    message = [
        TextSendMessage(  #顯示地址
            text = text1
        ),
        LocationSendMessage(  #顯示地圖
            title = "成功大學",
            address = text1,
            latitude = 23.000614,
            longitude = 120.217794
            ),
        ]
    line_bot_api.reply_message(reply_token,message)

    return "OK"

### 聯絡我們
def send_contact(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    
    message = TemplateSendMessage(
            alt_text = "聯絡我們",
            template = ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/tVjKzPH.jpg',
                title='聯絡我們',
                text='打電話給我們',
                actions=[
                    URITemplateAction(label='撥打電話', uri='tel:0123456789')  #開啟打電話功能
                ]
            )
        )
    line_bot_api.reply_message(reply_token,message)
    return "OK"
### show fsm
def send_fsm(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    fsm = ImageSendMessage(
            original_content_url='https://i.imgur.com/UuxQIKx.png',
            preview_image_url='https://i.imgur.com/UuxQIKx.png'
        )
    line_bot_api.reply_message(reply_token, fsm)
    return "OK"

### lobby
def send_lobby(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    fsm = ImageSendMessage(
            original_content_url='https://i.imgur.com/8EU4lGi.png',
            preview_image_url='https://i.imgur.com/8EU4lGi.png'
        )
    line_bot_api.reply_message(reply_token, fsm)
    return "OK"

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
