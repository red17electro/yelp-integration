from pymongo import MongoClient
import pandas as pd
from functions import db_connect, get_collection

# establing connection
client = db_connect()
collection = get_collection(client, 'TestDatabase', 'Businesses')

fazenda = collection.find({'name': 'Fazenda'})
berlin = collection.find({'location.city': 'Berlin'})


df_berlin = pd.DataFrame(list(berlin))
df_fazenda = pd.DataFrame(list(fazenda))
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
	print(df_fazenda)
