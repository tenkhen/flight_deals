import os
from twilio.rest import Client

tw_sid = os.environ.get('tw_sid')
tw_auth_token = os.environ.get('tw_auth_token')
sender_num = os.environ.get('sender_num')
dest_num = os.environ.get('dest_num')

class NotificationManager:
    def __init__(self, price, dep_city, dep_code, arr_city, arr_code, out_date, in_date):
        self.price = price
        self.dep_city = dep_city
        self.dep_code = dep_code
        self.arr_city = arr_city
        self.arr_code = arr_code
        self.out_date = out_date
        self.in_date = in_date

    def send_email(self):
        client = Client(tw_sid, tw_auth_token)

        message = client.messages \
            .create(
            body=f"Low price alert! Only ￡{self.price} to fly from {self.dep_city}-{self.dep_code} to {self.arr_city}-{self.arr_code}, from {self.out_date} to {self.in_date}",
            from_=sender_num,
            to=dest_num
        )

        print(message.status)