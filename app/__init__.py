from flask import Flask
from flask_mongoengine import MongoEngine
import json

app = Flask(__name__)
app.config.from_object('app.config')

# Initialize FlaskJSON before other extensions
json.JSONEncoder(app)
db = MongoEngine(app)