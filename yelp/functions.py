from pymongo import MongoClient
import json
import requests

def db_connect():
    try:
        client = MongoClient("mongodb+srv://admin:admin@cluster0-89mew.mongodb.net/TestDatabase?retryWrites=true&w=majority")
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")
    return client


def get_api_call(url, payload):
    headers = {
  'Authorization': 'Bearer EST24WiV5UEu-BGZFd7vKtHGcAUa7-rn4Pl0N_a9SVBqvOpYmlezH44rtYxtZQ7oDl6KtA2uNuBqlfha_WJKRsbwElJI_-iWZIXDo01KERC1rJ_nksJecLYch6TjXnYx'
}
    response = requests.request("GET", url, headers=headers, data = payload)
    return response

def get_collection(client, database_name, collection_name):
	db = client.get_database()
	assert db.name == database_name

	try:
		collection = db[collection_name]
		print("The collection is found")
	except:
		print("Something is wrong")
		
	return collection

def insert_data(client, collection_name, json_data):
    id_list = []
    db = client.get_database()
    collection = db[collection_name]
    for j in json_data:
        j['_id'] = j.pop('id')
        id_list.append(j.get('_id'))
        collection.insert_one(j)
    return id_list
# interface for rating a review text
def rate_review(text):
	return True