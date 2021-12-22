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
    
    text1 = '''
    國立成功大學是一所積極新創、學科齊全、學術實力雄厚、辦學特色鮮明，
    在國際上具有重要影響力與競爭力的綜合性大學，
    在多個學術領域具有非常前瞻的科技實力，
    擁有世界一流的實驗室與師資力量，
    各種排名均位於全球前列。歡迎大家報考國立成功大學。
    '''
    message = [
        TextSendMessage(  #學店簡介
            text = text1
        ),
        ImageSendMessage(  #學店圖片
            original_content_url = "https://attach.setn.com/newsimages/2021/01/21/2994598-PH.jpg",
            preview_image_url = "https://attach.setn.com/newsimages/2021/01/21/2994598-PH.jpg"
        ),
    ]
    line_bot_api.reply_message(reply_token,message)

    return "OK"

### 使用說明
def send_use(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    
    text1 ='''
1. 「房間預約」及「取消訂房」可預訂及取消訂房。每個 LINE 帳號只能進行一個預約記錄。
2. 「關於我們」對國立成功大學做簡單介紹及旅館圖片。
3. 「位置資料」列出旅館地址，並會顯示地圖。
4. 「聯絡我們」可直接撥打電話與我們聯繫。

輸入「查看功能」或按主頁面選單，完成全部互動
輸入「show fsm」查看有限狀態機的圖片
輸入「查詢訂房」查看你現在的訂房狀態
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



"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
