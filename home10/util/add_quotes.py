import json
from bson.objectid import ObjectId
from pymongo import MongoClient


client = MongoClient("mongodb+srv://user8:123456python@oleksandr.1c2z3g9.mongodb.net/?retryWrites=true&w=majority&appName=Oleksandr")
db = client.homework

with open("quotes.json", 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({'quote': quote['quote'],
                             'tags': quote['tags'],
                              'author': ObjectId(author['_id'])})
