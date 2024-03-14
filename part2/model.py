from mongoengine import *


connect(
    db="web8",
    host="mongodb+srv://user8:567234@oleksandr.1c2z3g9.mongodb.net/?retryWrites=true&w=majority&appName=Oleksandr",
)


class Contact(Document):
    fullname = StringField(required=True, unique=True)
    email = StringField(max_length=50)
    completed = BooleanField(default=False)
