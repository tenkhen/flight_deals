import os
import requests

SHEETY_PRICES_ENDPOINT = os.environ.get('SHEETY_PRICES_ENDPOINT')
SHEETY_USERS_ENDPOINT = os.environ.get('SHEETY_USERS_ENDPOINT')
bearer_key = os.environ.get('bearer_key')
header = {
    'Authorization': bearer_key
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=f"{SHEETY_PRICES_ENDPOINT}", headers=header)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def add_user(self, f_name, l_name, email):
        new_data = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email
            }
        }
        response = requests.post(url=f"{SHEETY_USERS_ENDPOINT}", json=new_data, headers=header)
        response.raise_for_status()

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data