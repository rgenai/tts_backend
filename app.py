from flask import Flask
from flask import request
from routes.authentication import authentication
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

uri = "mongodb+srv://soumyatarafder624:soumyatarafder6241234@cluster0.lze4vo3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print(e)

authentication(app, client)

@app.route('/')
def home():
	return "Welcome to Backend"

app.run(port=5000)
