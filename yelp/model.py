from pymongo import MongoClient

# establing connection
try:
    client = MongoClient("mongodb+srv://admin:admin@cluster0-89mew.mongodb.net/TestDatabase?retryWrites=true&w=majority")
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = client.get_database()
assert db.name == 'TestDatabase'

try:
	collection = db['Testdata']
	print("Connected to the collection")
except:
	print("Could not connect")

# print collection statistics
print(db.command("collstats", "events"))

# print database statistics
print(db.command("dbstats"))