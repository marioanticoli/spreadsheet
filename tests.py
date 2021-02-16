import unittest

from app import create_app, db, socketio
from app.models import Cell
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_read_cells(self):
        self.assertEqual(Cell.list_last_values(), {})

        Cell.write_values("A1", "10")
        self.assertEqual(Cell.list_last_values(), {"A1": "10"})


    def test_write_cells(self):
        Cell.write_values("B1", "20")
        self.assertEqual(Cell.list_last_values(), {"B1": "20"})

    
    def test_update_cells(self):
        Cell.write_values("C1", "30")
        Cell.write_values("C1", "31")
        self.assertEqual(Cell.list_last_values(), {"C1": "31"})


    def test_websocket_on_connect(self):
        socketio_test_client = self.__connect_websocket__()
        self.assertTrue(socketio_test_client.is_connected())


    def test_websocket_on_disconnect(self):
        socketio_test_client = self.__connect_websocket__()
        self.assertTrue(socketio_test_client.is_connected())
        socketio_test_client.disconnect()
        self.assertFalse(socketio_test_client.is_connected())


    def test_websocket_on_update(self):
        socketio_test_client = self.__connect_websocket__()
        self.assertEqual(Cell.list_last_values(), {})
        socketio_test_client.emit("update", {"cell": "A1", "value": "20"})
        self.assertEqual(Cell.list_last_values(), {"A1": "20"})


    def __connect_websocket__(self):
        flask_test_client = self.app.test_client()
        return socketio.test_client(self.app, flask_test_client=flask_test_client)


if __name__ == '__main__':
    unittest.main(verbosity=2)