from pymongo import MongoClient
import os

def populate_database():
    # Database connection
    mongo_uri = os.environ.get('MONGO_URI')
    client = MongoClient(mongo_uri)
    db = client.get_default_database()

    # Store Items Collection
    shopping_collection = db['shopping_list']

    # Data to be added to the collection
    shopping_list_data = [
        {"id": 1, "item": "Maçãs", "quantidade": 5},
        {"id": 2, "item": "Leite", "quantidade": 1},
        {"id": 3, "item": "Pão", "quantidade": 2},
        {"id": 4, "item": "Ovos", "quantidade": 12},
        {"id": 5, "item": "Bananas", "quantidade": 6},
        {"id": 6, "item": "Café", "quantidade": 1},
        {"id": 7, "item": "Arroz", "quantidade": 1},
        {"id": 8, "item": "Feijão", "quantidade": 1},
        {"id": 9, "item": "Açúcar", "quantidade": 1},
        {"id": 10, "item": "Sal", "quantidade": 1},
        {"id": 11, "item": "Tomates", "quantidade": 3},
        {"id": 12, "item": "Cebolas", "quantidade": 2},
        {"id": 13, "item": "Batatas", "quantidade": 4},
        {"id": 14, "item": "Carne Moída", "quantidade": 500},
        {"id": 15, "item": "Frango", "quantidade": 1},
        {"id": 16, "item": "Peixe", "quantidade": 2},
        {"id": 17, "item": "Manteiga", "quantidade": 1},
        {"id": 18, "item": "Queijo", "quantidade": 1},
        {"id": 19, "item": "Iogurte", "quantidade": 6},
        {"id": 20, "item": "Papel Higiênico", "quantidade": 12}
    ]

    # Populando os dados na coleção
    shopping_collection.insert_many(shopping_list_data)

    print("Dados da lista de compras adicionados com sucesso!")