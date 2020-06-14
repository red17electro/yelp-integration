import json
from functions import db_connect, get_api_call, get_collection, insert_data

url = "https://api.yelp.com/v3/businesses/search?term=restaurants&location=Dallas&limit=50"
payload = {}

response = get_api_call(url, payload)
businesses = json.loads(response.text)['businesses']

client = db_connect()

id_list = insert_data(client, 'Businesses', businesses)
print(id_list)

for id in id_list:
    url = "https://api.yelp.com/v3/businesses/" + str(id) + "/reviews"
    payload = {}
    response = get_api_call(url, payload)
    reviews = json.loads(response.text)['reviews']
    id_list = insert_data(client, 'Reviews', reviews)

