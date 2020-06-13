from pymongo import MongoClient

# establing connection
try:
    client = MongoClient("mongodb+srv://admin:admin@cluster0-89mew.mongodb.net/TestDatabase?retryWrites=true&w=majority")
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = client.get_database()
assert db.name == 'TestDatabase'

collection = db.create_collection('TestCreatedNow')

document1 = {
        "name":"John",
        "age":24,
        "location":"New York"
        }
#second document
document2 = {
        "name":"Sam",
        "age":21,
        "location":"Chicago"
        }

collection.insert_one(document1)
collection.insert_one(document2)