import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-89mew.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.test
