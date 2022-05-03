import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .settings import MailConfig


class MailSender:
    def __init__(self, payload):
        self.__email = MailConfig.email.value
        self.__password = MailConfig.password.value
        self.__payload = payload

    def send(self):
        body = ""
        for each in self.__payload:
            for link in each['link_keyword']:
                msg = "\n".join(link['link'])
                body += f"{link['keyword']} : ({msg})\n"
            self.__send(each['client'], f"subject", body)

    def __send(self, receiver, subject, body):
        message = MIMEMultipart()
        message['From'] = self.__email
        message['To'] = receiver
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(self.__email, self.__password)
        text = message.as_string()
        session.sendmail(self.__email, receiver, text)
        session.quit()
