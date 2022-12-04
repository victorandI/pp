from sqlalchemy.orm import sessionmaker
import unittest

from base64 import b64encode
from app import app
import json
from models import User, Car, Order
from app import engine
from user import bcrypt


Session = sessionmaker(bind=engine)

class TestingBase(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    tester = app.test_client()
    session = Session()

    def tearDown(self):
        self.close_session()

    def close_session(self):
        self.session.close()

class BaseTestCase(TestingBase):
    car = {
        "brand": "bmw",
        "model": "b5",
        "status": "available"
    }

    user = {
        "name": "Valentin",
        "surname": "K",
        "username": "M",
        "password": "12345678",
        "role": 0
    }

    user1 = {
        "name": "Dmytro",
        "surname": "U",
        "username": "UK",
        "password": "12345678",
        "role": 0
    }

    order = {
        "user_id": 1,
        "car_id": 1,
        "beginningDate": "2021-09-09",
        "amountOfDays": "3",
        "complete": "successfully"
    }

    def test_User_Creation(self):
        response = self.tester.post("/user/", data=json.dumps(self.user),
                                    content_type='application/json')
        code = response.status_code
        self.assertEqual(200, code)
        self.session.query(User).filter_by(name='Valentin').delete()
        self.session.commit()

    def test_User_Creation_invalid(self):
        response = self.tester.post("/user/", data=json.dumps({
        "name": "Valdn",
        "surname": "Kasa",
        "username": "Vo",
        "password": "123",
        "role": 0
    }), content_type="application/json")
        code = response.status_code
        self.assertEqual(400, code)

    def test_Get_User_By_id(self):
        hashpassword = bcrypt.generate_password_hash('12345678')
        user = User(id=1234, name="Valentin", surname="K", username="M", password=hashpassword, role=0)
        self.session.add(user)
        self.session.commit()
        response = self.tester.get('/user/<username>')
        code = response.status_code
        self.assertEqual(200, code)

    def test_Delete_User_by_Id(self):
        hashpassword = bcrypt.generate_password_hash('12345678')
        user = User(name='Dmytro', surname='U', username='UK', password=hashpassword, role=0)
        self.session.add(user)
        self.session.commit()
        response = self.tester.delete('/user/4')
        code = response.status_code
        self.assertEqual(401, code)


    def test_User_Creation_invaIid(self):
        response = self.tester.post("/user/", data=json.dumps({
        "name": "Bary",
        "surname": "Surnha",
        "username": "Noo",
        "password": "123",
        "role": 0
    }),

        content_type="application/json")
        code = response.status_code
        self.assertEqual(400, code)




# python -m unittest tests.py




'''from unittest import TestCase
from flask import url_for
from flask_testing import TestCase
import db_utils, app
from app import Session
from flask_bcrypt import generate_password_hash
from models import User, Car, Order, engine, Base


class BaseCaseCase(TestCase):
    def _pre_setup(self):
        super().setUp()
        self.create_tables()

        self.admin_credentials = {
            "username": "admin-jwidhewudheiw",
            "password": "admin",
            "role": True,
        }
        self.user_1_data = {
            "name": "user1",
            "surname": "user11",
            "username": "username",
            "password": "123"
        }
        self.user_1_data_hashed = {
            **self.user_1_data,
            "password":generate_password_hash(self.user_1_data["password"]),

        }
        self.admin_credentials = {
            "username": self.user_1_data["username"],
            "password": self.user_1_data["password"],
            "role": True,
        }
        self.user_2_data = {
            "name": "user2",
            "surname": "user22",
            "username": "username2",
            "password": "1234"
        }
        self.user_2_data_hashed = {
            **self.user_2_data,
            "password": generate_password_hash(self.user_2_data["password"]),

        }
        self.admin_credentials = {
            "username": self.user_2_data["username"],
            "password": self.user_2_data["password"],
            "role": True,
        }

        def tearDown(self):
            self.close_session()

        def create_tables(self):
            Base.metadata.drop_all(engine),
            Base.metadata.create_all(engine)

        def close_session(self):
            Session().close()

        def create_app(self):
            return app

class BaseTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.create_tables()

        self.admin_credentials = {
            "username": "admin-hefeiohf",
            "password": "secret",
        }
class TestListUsers(BaseTestCase):
    def test_list_users(self):
        db_utils.create_entry(User, **self.user_1_data_hashed)
        db_utils.create_entry(User, **self.user_2_data_hashed)

        resp = self.client.get{
            url_for()
        }

'''




#

# coverage report --omit 'venv/*' -m