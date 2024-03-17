import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.errors import PyMongoError  # Adicione esta linha para importar PyMongoError

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
mongo_uri = os.environ.get('MONGO_URI')
database_name = os.environ.get('DATABASE_NAME')
collection_name = os.environ.get('COLLECTION_NAME')

client = MongoClient(mongo_uri or 'localhost', 27017)
db = client[database_name]
shopping_collection = db[collection_name]

# Function to populate the database with initial data
# from scripts.populate_database import populate_database
# populate_database()

# Endpoint to return the shopping list
@app.route('/v1/shopping', methods=['GET'])
def get_shopping_list():
    try:
        shopping_list = list(shopping_collection.find({}, {'_id': False}))
        print(shopping_list)
        return jsonify(shopping_list)
    except PyMongoError as e:

        print(f'Error fetching shopping list: {e}')
        return jsonify({'error': str(e)}), 500  # Return error response if something goes wrong with MongoDB

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

def item_exists(item_id):
    return shopping_collection.find_one({'id': item_id}) is not None

# Endpoint to delete an item from the shopping list based on the ID
@app.route('/v1/shopping/<int:id>', methods=['DELETE'])
def delete_item(id):
    try:
        if not item_exists(id):
            return jsonify({'error': f'Item with ID {id} not found'}), 404
        
        shopping_collection.delete_one({'id': id})
        return jsonify({'message': 'Item deleted successfully'})
    except PyMongoError as e:
        return jsonify({'error': str(e)}), 500  # Retornar mensagem de erro em caso de falha no MongoDB

@app.route('/health-check')
def health_check():
    return jsonify({'message': 'Service is up and running'})


# Main method to run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
