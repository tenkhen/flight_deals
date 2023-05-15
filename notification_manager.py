import os
import smtplib
from twilio.rest import Client

tw_sid = os.environ.get('tw_sid')
tw_auth_token = os.environ.get('tw_auth_token')
sender_num = os.environ.get('sender_num')
dest_num = os.environ.get('dest_num')

SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
GMAIL_APP_PW = os.environ.get('GMAIL_APP_PW')

MAIL_PROVIDER_SMTP_ADDRESS = 'smtp.gmail.com'

class NotificationManager:

    def __init__(self):
        self.client = Client(tw_sid, tw_auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=sender_num,
            to=dest_num,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(SENDER_EMAIL, GMAIL_APP_PW)
            for email in emails:
                connection.sendmail(
                    from_addr=SENDER_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )