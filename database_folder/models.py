#~movie-bag/database/models.py
from .database import db

class Card(db.Document):
    Name = db.StringField()
    Type = db.StringField()
    Level = db.StringField()
    Race = db.StringField()
    Attribute = db.StringField()
    ATK = db.StringField()
    DEF = db.StringField()
    
class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    username = db.StringField()
    first_name = db.StringField()
    last_name = db.StringField()
 