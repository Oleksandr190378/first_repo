from pymongo import MongoClient


def get_mongodb():
    client = MongoClient(
        "mongodb+srv://user8:567234@oleksandr.1c2z3g9.mongodb.net/?retryWrites=true&w=majority&appName=Oleksandr")
    db = client.homework
    return db