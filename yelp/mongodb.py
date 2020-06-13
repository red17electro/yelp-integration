import json
from functions import db_connect, get_api_call

url = "https://api.yelp.com/v3/businesses/search?term=restaurants&location=Manchester&limit=50"

payload = {}


response = get_api_call(url, payload)

businesses = json.loads(response.text)['businesses']

client = db_connect()
db = client.get_database()
collection = db["Businesses"]
id_list = []
for b in businesses:
    b['_id'] = b.pop('id')
    id_list.append(b.get('_id'))
    collection.insert_one(b)
