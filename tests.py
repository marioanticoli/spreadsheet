from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import Cell

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

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


if __name__ == '__main__':
    unittest.main(verbosity=2)