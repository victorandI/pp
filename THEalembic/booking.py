from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError
from flask_bcrypt import Bcrypt
from models import User, Session, Booking
from schemas import UserSchema, BookingSchema

booking = Blueprint('booking', __name__)
bcrypt = Bcrypt()

session = Session()

# Register new user
@booking.route('/api/v1/booking', methods=['POST'])
def createBooking():
    # Get data from request body
    data = request.get_json()

    # Validate input data
    try:
        BookingSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if user already exists
    exists = session.query(Booking.idCar).filter_by(Car=data['Car']).first()
    if exists:
        return Response(status=404, response='This car is already taken.')

    # Create new user
    new_booking = Booking(User=data['user'], Car=data['user'], dfrom=data['from'], duntil=data['until'])

    # Add new user to db
    session.add(new_booking)
    session.commit()

    return Response(status=200, response='New booking was successfully created!')

@booking.route('/api/v1/booking/<bookingId>', methods=['GET'])
def get_booking(bookingId):
    # Check if supplied bookingId correct
    if int(bookingId)<1:
        return Response(status=400, response='Invalid bookingId supplied')
    # Check if booking exists
    db_booking = session.query(Booking).filter_by(idBooking=bookingId).first()
    if not db_booking:
        return Response(status=404, response='A booking with provided ID was not found.')

    # Return booking data
    booking_data = {'bookingId': db_booking.idBooking, 'car': db_booking.car, 'user': db_booking.user, 'dfrom': db_booking.dfrom, 'duntil': db_booking.until}
    return jsonify({"booking": booking_data})

# Delete car by id
@booking.route('/api/v1/booking', methods=['PUT'])
def put_article():
    data = request.get_json()
    # Check if supplied userId correct
    if data['bookingId'] < 1:
        return Response(status=404, response='Invalid bookingId supplied')

    # Check if user exists
    db_booking = session.query(User).filter_by(password=data['password']).first()
    if not db_booking:
        return Response(status=400, response='Wrong password supplied')

    db_user2 = session.query(Booking).filter_by(dfrom=data['dfrom']).first()
    if not db_user2:
        return Response(status=402, response='A bad date was supplied')

    db_user2.status = "accepted"
    session.commit()

    return Response(status=200, response='Booking was asccepted successfully')

