from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)
mongo_uri = os.environ.get('MONGO_URI')
client = MongoClient(mongo_uri)
db = client.get_default_database()

# Collection in MongoDB to store the shopping list items
shopping_collection = db['shopping_list']

# Function to populate the database with initial data
# from scripts.populate_database import populate_database
# populate_database()

# Endpoint to return the shopping list
@app.route('/v1/shopping', methods=['GET'])
def get_shopping_list():
    shopping_list = list(shopping_collection.find({}, {'_id': False}))
    return jsonify(shopping_list)

# Endpoint to return a specific item from the shopping list based on the ID
@app.route('/v1/shopping/<int:id>', methods=['GET'])
def get_item(id):
    item = shopping_collection.find_one({'id': id}, {'_id': False})
    if item:
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 404

# Endpoint to add a new item to the shopping list
@app.route('/v1/shopping', methods=['POST'])
def add_item():
    data = request.json
    new_item = {
        'id': data['id'],
        'item': data['item'],
        'quantity': data['quantity']
    }
    shopping_collection.insert_one(new_item)
    return jsonify({'message': 'Item added successfully'}), 201

# Endpoint to update an item in the shopping list based on the ID
@app.route('/v1/shopping/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.json
    updated_item = {
        'id': data['id'],
        'item': data['item'],
        'quantity': data['quantity']
    }
    shopping_collection.update_one({'id': id}, {'$set': updated_item})
    return jsonify({'message': 'Item updated successfully'})

# Endpoint to delete an item from the shopping list based on the ID
@app.route('/v1/shopping/<int:id>', methods=['DELETE'])
def delete_item(id):
    shopping_collection.delete_one({'id': id})
    return jsonify({'message': 'Item deleted successfully'})

# Main method to run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
