from datetime import datetime, timedelta
from flight_data import FlightData
import requests

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com'
TEQUILA_API_KEY = 'jnBpf7r2qnjq6Hj6o7ZBolZKNa95lFcF'
headers = {'apikey': TEQUILA_API_KEY}


def check_flights():
    query = {
        'fly_from': "YTO",
        'fly_to': 'PAR',
        'date_from': tomorrow.strftime('%d/%m/%Y'),
        'date_to': six_month_from_today.strftime('%d/%m/%Y'),
        'nights_in_dst_from': 7,
        'nights_in_dst_to': 28,
        'flight_type': 'round',
        'one_for_city': 1,
        'max_stopovers': 0,
        'curr': 'GBP'
    }

    response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', headers=headers, params=query)

    try:
        data = response.json()['data'][0]
    except IndexError:
        print(f"No flights found for {'PAR'}.")
        return None

    flight_data = FlightData(
        price=data['price'],
        origin_city=data['route'][0]['cityFrom'],
        origin_airport=data['route'][0]['flyFrom'],
        destination_city=data['route'][0]['cityTo'],
        destination_airport=data['route'][0]['flyTo'],
        out_date=data['route'][0]['local_departure'].split('T')[0],
        return_date=data['route'][1]['local_departure'].split('T')[0]
    )
    print(f'{flight_data.destination_city}: £{flight_data.price}')
    return flight_data

