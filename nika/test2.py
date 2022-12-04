from test import *


class TestStudent(BaseTestCase):
    def test_get_student(self):
        response = self.user.get('/user/admin1',
                                   headers=self.get_auth_headers(self.user_auth))
        self.assertEqual(response, 200)



    def test_update_user(self):
        response = self.user.put('/user/admin12', data=json.dumps({
            "id": 12387,
            "name": "admin12",
            "surname": "admin12",
            "username": "admin12"
        }), content_type='application/json')
        self.assertEqual(response, 200)

    def test_wrong_update_user(self):
        response = self.user.put('/user/user12', data=json.dumps({
            "id": 123856,
            "name": "admin1",
            "surname": "admin1",
            "username": "admin1"
        }), content_type='application/json')
        self.assertEqual(response, 403)

    def test_wrong_data_update_user(self):
        response = self.user.put('/user/user1', data=json.dumps({
            "id": 1238,
            "name": "admin12",
            "surname": "admin12",
            "username": "admin12"
        }), content_type='application/json')
        self.assertEqual(response, 400)


class TestCar(BaseTestCase):
    car = {
        "id": 1,
        "brand": "bmw3",
        "model": "b5",
        "status": "available"
    }
    def test_get_car(self):
        response = self.user.get('/car/1')
        self.assertEqual(response, 200)



    def test_update_car(self):
        response = self.user.put('/car/1', data=json.dumps({
            "id": 1,
        "brand": "bmw3",
        "model": "b5",
        "status": "available"
        }), content_type='application/json')
        self.assertEqual(response, 200)

    def test_wrong_update_car(self):
        response = self.user.put('/car/2', data=json.dumps({
            "id": 2,
        "brand": "bmw3",
        "model": "b5",
        "status": "available"
        }), content_type='application/json')
        self.assertEqual(response, 403)

    def test_wrong_data_update_car(self):
        response = self.user.put('/car/1', data=json.dumps({
            "id": 12,
        "brand": "bmw323",
        "model": "b5",
        "status": "available"
        }), content_type='application/json')
        self.assertEqual(response, 400)
