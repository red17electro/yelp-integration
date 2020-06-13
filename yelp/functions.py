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