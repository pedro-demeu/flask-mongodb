import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_shopping_list(self):
        response = self.app.get('/v1/shopping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_add_item(self):
        data = {'id': 4, 'item': 'Abacaxi', 'quantity': 3}
        response = self.app.post('/v1/shopping', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')

    def test_update_item(self):
        data = {'id': 1, 'item': 'Maçãs', 'quantity': 10}
        response = self.app.put('/v1/shopping/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_delete_item(self):
        data = {'id': 4, 'item': 'Abacaxi', 'quantity': 3}
        self.app.post('/v1/shopping', json=data)

        response = self.app.delete('/v1/shopping/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

if __name__ == '__main__':
    unittest.main()
