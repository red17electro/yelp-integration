import pandas as pd
from pymongo import MongoClient
from functions import db_connect, get_collection, rate_review
from monkeylearn import MonkeyLearn

# establing connection
client = db_connect()
collection = get_collection(client, 'TestDatabase', 'Businesses')
collection_2 = get_collection(client, 'TestDatabase', 'Reviews')

fazenda = collection.find({'name': 'Fazenda'})
berlin = collection.find({'location.city': 'Berlin'})
reviews = collection_2.find()

df_berlin = pd.DataFrame(list(berlin))
df_fazenda = pd.DataFrame(list(fazenda))
df_reviews = pd.DataFrame(list(reviews))

for index, row in df_reviews.iterrows():
	review_text = row['text']
	text_file = open("Output.txt", "w")
	text_file.write("Review: %s" % review_text)
	rate_review(review_text)
	text_file.close()

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
	print(df_reviews['text'])

ml = MonkeyLearn('685d6ec80be3bea9502c9103a3c6eb5096cb866a')
data = ["I am updating my original review (below) as their management replied trying to play innocent. What they failed to mention is that we called to make a..."]
model_id = 'cl_pi3C7JiL'
result = ml.classifiers.classify(model_id, data)
print(result.body)