# https://www.learncodewithmike.com/2020/02/python-email.html

import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from utils import send_text_message

gmail_password = os.getenv("GMAIL_PASSWORD",None)
port = os.environ.get("PORT", 8000)

def send_email_to_kanido(reply_token, feature_name, description):

    
    content = MIMEMultipart()
    print("complete")    
    content['subject'] = 'booking system 意見回饋'                        # 標題
    content['from'] = 'baobaomokk@gmail.com'                                    # 寄件者
    content['to'] = 'f64081169@gs.ncku.edu.tw'                         # 收件者
    content.attach(MIMEText(f'{feature_name}\n\n{description}'))  # 內容
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:  # 設定SMTP伺服器
        try:
            
            print("complete")    
            smtp.ehlo()
            print("complete")                                            # 驗證SMTP伺服器
            smtp.starttls()
            print("complete")                                        # 建立加密傳輸
            smtp.login('baobaomokk@gmail.com', gmail_password)  # 登入寄件者gmail
            print("complete")
            smtp.send_message(content)  
            print("complete")                           # 寄送郵件
            send_text_message(reply_token, f'{feature_name}  已收到你的回饋!\U0001f914')
        except Exception as e:
            send_text_message(reply_token, '不好意思，無法收到你的意見回饋')