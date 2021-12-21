from transitions.extensions import GraphMachine

from utils import send_address, send_book, send_contact, send_text_message,send_about, send_use, send_book,send_address,send_contact,send_fsm


class TocMachine(GraphMachine):
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


    ### show fsm
    def on_enter_show_fsm(self, event):
        print("I'm entering show_fsm")

        reply_token = event.reply_token
        #send_text_message(reply_token, "呈現使用說明")
        send_fsm(reply_token)
        self.go_back()

    def on_exit_show_fsm(self):
        print("Leaving show_fsm")
        
    ### 使用說明
    def on_enter_menu(self, event):
        print("I'm entering menu")

        reply_token = event.reply_token
        #send_text_message(reply_token, "呈現使用說明")
        send_use(reply_token)
        self.go_back()

    def on_exit_menu(self):
        print("Leaving menu")

    ### 房間預約
    def on_enter_room_booking(self, event):
        print("I'm entering room_booking")

        reply_token = event.reply_token
        #send_text_message(reply_token, "呈現房間預約")
        send_book(reply_token)
        self.go_back()

    def on_exit_room_booking(self):
        print("Leaving room_booking")

    ### 取消訂房
    def on_enter_cancel(self, event):
        print("I'm entering cancel")

        reply_token = event.reply_token
        send_text_message(reply_token, "呈現取消訂房")
        self.go_back()

    def on_exit_cancel(self):
        print("Leaving cancel")

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

