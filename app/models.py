# app/models.py

from app import db

class User(db.Document):
    username = db.StringField(unique=True, required=True)
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    balance = db.FloatField(default=0)
    xrpl_secret = db.StringField()  # Add this field to store XRPL wallet secret
