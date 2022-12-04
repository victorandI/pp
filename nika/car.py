from flask import Blueprint, request, jsonify, Response
from flask_bcrypt import Bcrypt
from marshmallow import ValidationError
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URI
from validation import CarSchema
from sqlalchemy import create_engine
from models import Car
from user import token_required_user, loginUser

car = Blueprint('car', __name__)
bcrypt = Bcrypt()
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

session = Session()


@car.route('/car/', methods=['POST'])
@token_required_user
#current_user
def createCar(current_user):
    if  current_user.role != 1:
        return jsonify({'message': 'This is only for admins'})

    data = request.get_json(force=True)
    try:
        CarSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    session.query(Car).filter_by(brand=data['brand']).first()
    session.query(Car).filter_by(model=data['model']).first()
    session.query(Car).filter_by(status=data['status']).first()
    users = Car(brand=data['brand'], model=data['model'], status=data['status'])
    session.add(users)
    session.commit()
    session.close()
    return Response(response="Car successfully added")


@car.route('/car/<id>', methods=['GET'])
def getCarById(id):
    id = session.query(Car).filter_by(id=id).first()
    if not id:
        return Response(status=404, response="Id doesn't exist")
    biblethump = {'id': id.id, 'brand': id.brand, 'model': id.model, 'status': id.status}
    return jsonify({'user': biblethump})


@car.route('/car', methods=['GET'])
def getCars():
    limbo = session.query(Car)
    quer = [CarSchema().dump(i) for i in limbo]
    if not quer:
        return {"message": "No cars available"}, 404
    res = {}
    for i in range(len(quer)):
        res[i + 1] = quer[i]
    return res


@car.route('/car/<id>', methods=['PUT'])
@token_required_user
def updateCar(current_user, id):
    if current_user.role != 1:
        return jsonify({'message': 'This is only for admins'})

    data = request.get_json(force=True)
    try:
        CarSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    car_data = session.query(Car).filter_by(id=id).first()
    if not car_data:
        return Response(status=404, response="Id doesn't exist")
    if 'brand' in data.keys():
        session.query(Car).filter_by(brand=data['brand']).first()
        car_data.brand = data['brand']

    if 'model' in data.keys():
        session.query(Car).filter_by(model=data['model']).first()
        car_data.model = data['model']

    if 'status' in data.keys():
        car_data.status = data['status']

    session.commit()
    session.close()
    return Response(response="Car successfully updated")


@car.route('/car/<id>', methods=['DELETE'])
@token_required_user
#current_user,
def deleteCar(current_user,id):
    if not current_user.role:
        return jsonify({'message': 'This is only for admins'})
    id = session.query(Car).filter_by(id=id).first()
    if not id:
        return Response(status=404, response="Id doesn't exist")
    session.delete(id)
    session.commit()
    session.close()
    return Response(response="Car successfully deleted")

