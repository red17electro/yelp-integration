from pymongo import MongoClient
import pandas as pd

# establing connection
try:
    client = MongoClient("mongodb+srv://admin:admin@cluster0-89mew.mongodb.net/TestDatabase?retryWrites=true&w=majority")
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = client.get_database()
assert db.name == 'TestDatabase'

collection_name = 'Businesses'
try:
	collection = db[collection_name]
	print("Connected to the collection")
except:
	print("Could not connect")

fazenda = collection.find({'name': 'Fazenda'})
berlin = collection.find({'location.city': 'Berlin'})


df_berlin = pd.DataFrame(list(berlin))
df_fazenda = pd.DataFrame(list(fazenda))
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
	print(df_fazenda)
