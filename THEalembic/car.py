from alembic.util import exc
from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError
from flask_bcrypt import Bcrypt
from werkzeug.security import check_password_hash

from models import Car, Session, User
from schemas import CarSchema

car = Blueprint('car', __name__)
bcrypt = Bcrypt()

session = Session()
def verify_password(username, password):
    try:
        user = Session.query(User).filter_by(username=username).one()
        if check_password_hash(user.password, password):
            return username
    except exc.NoResultFound:
        return False

@car.route('/api/v1/car', methods=['POST'])
def create_car():
    # Get data from request body
    data = request.get_json()

    # Validate input data
    try:
        CarSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if car already exists
    exists = session.query(Car.idCar).filter_by(brand=data['brand']).first()
    if exists:
        return Response(status=404, response='car with such number already exists.')


    # Create new car
    new_car = Car(brand=data['brand'], model=data['model'], year=data['year'], seatsNum=data['seatsNum'], status=data['status'], price=data['price'])

    # Add new article to db
    session.add(new_car)
    session.commit()

    return Response(status=200, response='New car was successfully created!')

# Get car by id
@car.route('/api/v1/Car/<idCar>', methods=['GET'])
def get_car(CarID):
    # Check if supplied userId correct
    if int(CarID)<1:
        return Response(status=400, response='Invalid CarId supplied')
    # Check if user exists
    db_car = session.query(Car).filter_by(idCar=CarID).first()
    if not db_car:
        return Response(status=404, response='A car with provided ID was not found.')

    # Return user data
    car_data = {'idCar': db_car.CarID, 'brand': db_car.brand,'model': db_car.model, 'year': db_car.year, 'number of seats': db_car.seatsNum, 'status': db_car.status, 'price': db_car.price}
    return jsonify({"Car": car_data})


# Delete article by id
@car.route('/api/v1/Car/<idCar>', methods=['DELETE'])
def delete_car(CarId):
    # Check if supplied carId correct
    if int(CarId)<1:
        return Response(status=400, response='Invalid carId supplied')

    # Check if car exists
    db_car = session.query(Car).filter_by(idCar=CarId).first()
    if not db_car:
        return Response(status=404, response='A car with provided ID was not found.')

    # Delete car
    session.delete(db_car)
    session.commit()
    return Response(status=200, response='Car was deleted.')