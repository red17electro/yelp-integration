from pymongo import MongoClient
import json
import requests


url = "https://api.yelp.com/v3/businesses/AniwYrGjpmp_B51XO_kIVQ/reviews"

payload = {}
headers = {
  'Authorization': 'Bearer EST24WiV5UEu-BGZFd7vKtHGcAUa7-rn4Pl0N_a9SVBqvOpYmlezH44rtYxtZQ7oDl6KtA2uNuBqlfha_WJKRsbwElJI_-iWZIXDo01KERC1rJ_nksJecLYch6TjXnYx'
}

response = requests.request("GET", url, headers=headers, data = payload)

your_document = json.loads(response.text)
print(your_document)
# establing connection
try:
    client = MongoClient("mongodb+srv://admin:admin@cluster0-89mew.mongodb.net/TestDatabase?retryWrites=true&w=majority")
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = client.get_database()
assert db.name == 'TestDatabase'

col = db["Reviews"]
result = col.insert_many(your_document['reviews'])

