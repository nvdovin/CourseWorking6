import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from dotenv import load_dotenv

load_dotenv()


def send_yandex_message(mailer_header: str, text: str, recepient: str):    
    my_login = "vdovinna@yandex.ru"
    password = os.getenv("YANDEX_PASSWORD")

    msg = MIMEText(f'{text}', "plain", "utf-8")
    msg["Subject"] = Header(mailer_header, "utf-8")
    msg["From"] = my_login
    msg["To"] = recepient

    s = smtplib.SMTP("smtp.yandex.ru", 587, timeout=10)
    
    try:
        s.starttls()
        s.login(my_login, password)
        response = s.sendmail(from_addr=msg["From"], to_addrs=recepient, msg=msg.as_string())
        
    except Exception as error:
        print(error)
    
    finally:
        s.quit()
        return response
