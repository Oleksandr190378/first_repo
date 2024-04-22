from pymongo import MongoClient


def get_mongodb():
    client = MongoClient(
        "mongodb+srv://user8:123456python@oleksandr.1c2z3g9.mongodb.net/?retryWrites=true&w=majority&appName=Oleksandr")
    db = client.homework
    return db

