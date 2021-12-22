from os import name
from typing import Text
from transitions.extensions import GraphMachine
import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent, ImageSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction,MessageTemplateAction

from utils import send_address, send_contact, send_text_message,send_about, send_use,send_address,send_contact,send_fsm

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

class TocMachine(GraphMachine):
    RoomNum = 666 #房間號
    Price = 1800 #價錢
    name = "empty" #客人名
    breakfast = "empty" #要吃早餐嗎
    days = 0 #幾天
    date = "empty" #住宿日期
    state = "user"
    c=0#是否要cancel
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    ### is going to 系列
    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "@使用說明"

    def is_going_to_room_booking(self, event):
        text = event.message.text
        return text.lower() == "@房間預約"

    def is_going_to_cancel(self, event):
        text = event.message.text
        return text.lower() == "@取消訂房"

    def is_going_to_about(self, event):
        text = event.message.text
        return text.lower() == "@關於我們"

    def is_going_to_info(self, event):
        text = event.message.text
        return text.lower() == "@位置資訊"

    def is_going_to_comm(self, event):
        text = event.message.text
        return text.lower() == "@聯絡我們"

    def is_going_to_show_fsm(self, event):
        text = event.message.text
        return text.lower() == "show fsm"

    def is_going_to_lobby(self, event):
        text = event.message.text
        return text.lower() == "查看功能"

    ###訂房流程
    def is_going_to_name(self, event):
        text = event.message.text
        return True
    def is_going_to_date(self, event):
        text = event.message.text
        return True
    def is_going_to_day(self, event):
        text = event.message.text
        return True
    def is_going_to_success(self, event):
        text = event.message.text
        return True

    ###取消流程
    def is_going_to_cancel2(self, event):
        text = event.message.text
        return True
    



    ### 主功能選單
    def on_enter_lobby(self, event):
        print("I'm entering lobby")
        reply_token = event.reply_token
        send_fsm(reply_token)
        self.go_back()

    def on_exit_lobby(self):
        print("Leaving lobby")

    ### show fsm
    def on_enter_show_fsm(self, event):
        print("I'm entering show_fsm")
        #TocMachine.state="show_fsm"
        reply_token = event.reply_token
        send_fsm(reply_token)
        self.go_back()

    def on_exit_show_fsm(self):
        print("Leaving show_fsm")
        
    ### 使用說明
    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        send_use(reply_token)
        self.go_back()

    def on_exit_menu(self):
        print("Leaving menu")

    ### 房間預約
    def on_enter_room_booking(self, event):
        print("I'm entering room_booking")
        TocMachine.state="room_booking"
        reply_token = event.reply_token
        send_text_message(reply_token, "開始訂房服務，請輸入名稱")
        

    ### 輸入名稱
    def on_enter_name(self, event):
        self.c = 0
        print("I'm entering name")
        TocMachine.state="name"
        
        name = event.message.text
        print(name)
        if name !="@取消訂房":
            TocMachine.name = name
            reply_token = event.reply_token
            send_text_message(reply_token, "你好哇! "+name+"! \n請輸入想要入住的日期\nex:2021/12/25")
        else: 
            self.c=1
            self.go_cancel(event)
    

            
    ### 輸入日期
    def on_enter_date(self, event):
        self.c=0
        print("I'm entering date")
        TocMachine.state="date"
        if event.message.text !="@取消訂房":
            date = event.message.text
            TocMachine.date = date
            reply_token = event.reply_token
            send_text_message(reply_token, "請輸入預計入住天數")
        else:
            self.c=1
            self.go_cancel(event)



    ### 輸入天數
    def on_enter_day(self, event):
        self.c=0
        print("I'm entering date")
        TocMachine.state="day"
        day = event.message.text
        if day !="@取消訂房":
            TocMachine.days = int(day)
            reply_token = event.reply_token
            send_text_message(reply_token, "了解!"+TocMachine.name+"\n本大學...大飯店會免費提供早餐\n請問你是要西式還是中式呢？")
            #self.go_back()
        else:
            self.c=1
            self.go_cancel(event)


    ### 訂房成功
    def on_enter_success(self, event):
        self.c=0
        print("I'm entering date")
        TocMachine.state="day"
        breakfast = event.message.text
        if breakfast !="@取消訂房":
            TocMachine.breakfast = breakfast
            reply_token = event.reply_token
            line_bot_api = LineBotApi(channel_access_token)
    
            text1 ="訂房成功!房間號:666 價格:"+str(TocMachine.days*1800)
            text2="名稱:"+TocMachine.name+"\n日期:"+TocMachine.date+"\n天數:"+str(TocMachine.days)+"\n早餐:"+TocMachine.breakfast
            text3="感謝你支持本大學店"
            message = [
                TextSendMessage(
                text = text1
            ),
            TextSendMessage(
                text = text2
            ),
            TextSendMessage(
                text = text3
            ),
            ]
            line_bot_api.reply_message(reply_token,message)
            self.go_back()
        else:
            self.c=1
            self.go_cancel(event)

    def on_exit_success(self):
        print("Leaving success")



    ### 取消訂房
    def on_enter_cancel(self, event):
        print("I'm entering cancel")
        #TocMachine.state="cancel"
        reply_token = event.reply_token
        print(event.message.text)
        send_text_message(reply_token, "隨意輸入來取消訂房")
        

    def on_enter_cancel2(self, event):
        print("I'm entering cancel2")
        TocMachine.RoomNum = 0 #房間號
        TocMachine.Price = 0 #價錢
        TocMachine.name = "empty" #客人名
        TocMachine.breakfast = "empty" #要吃早餐嗎
        TocMachine.days = 0 #幾天
        TocMachine.date = "empty" #住宿日期
        #TocMachine.state="cancel"
        reply_token = event.reply_token
        print(event.message.text)
        send_text_message(reply_token, "取消成功")
        self.go_back()

    
        

    ### 關於我們
    def on_enter_about(self, event):
        print("I'm entering about")

        reply_token = event.reply_token
        
        #send_text_message(reply_token, "呈現關於我們")
        send_about(reply_token)
        self.go_back()

    def on_exit_about(self):
        print("Leaving about")

    ### 位置資訊
    def on_enter_info(self, event):
        print("I'm entering info")

        reply_token = event.reply_token
        #send_text_message(reply_token, "呈現位置資訊")
        send_address(reply_token)
        self.go_back()

    def on_exit_info(self):
        print("Leaving about")

    ### 聯絡我們
    def on_enter_comm(self, event):
        print("I'm entering comm")

        reply_token = event.reply_token
        #send_text_message(reply_token, "呈現聯絡我們")
        send_contact(reply_token)
        self.go_back()

    def on_exit_comm(self):
        print("Leaving comm")

