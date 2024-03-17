from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)
mongo_uri = os.environ.get('MONGO_URI')
client = MongoClient(mongo_uri)
db = client.get_default_database()

@app.route('/')
def index():
    return 'Hello, Flask with MongoDB!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
