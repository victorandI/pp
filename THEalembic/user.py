from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError
from flask_bcrypt import Bcrypt
from models import User, Session
from schemas import UserSchema

user = Blueprint('user', __name__)
bcrypt = Bcrypt()

session = Session()

# Register new user
@user.route('/api/v1/user', methods=['POST'])
def registerUser():
    # Get data from request body
    data = request.get_json()

    # Validate input data
    try:
        UserSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if user already exists
    exists = session.query(User.user_id).filter_by(username=data['username']).first()
    if exists:
        return Response(status=404, response='User with such username already exists.')

    # Hash user's password
    hashed_password = bcrypt.generate_password_hash(data['password'])
    # Create new user
    new_user = User(email=data['email'], password=hashed_password, LastName=data['LastName'], FirstName=data['FirstName'],role=data['role'])

    # Add new user to db
    session.add(new_user)
    session.commit()

    return Response(status=200, response='New user was successfully created!')

# Get user by id
@user.route('/api/v1/user/<idUser>', methods=['GET'])
def get_user(userId):
    # Check if supplied userId correct
    if int(userId)<1:
        return Response(status=400, response='Invalid userID supplied')
    # Check if user exists
    db_user = session.query(User).filter_by(idUser=userId).first()
    if not db_user:
        return Response(status=404, response='A user with provided ID was not found.')

    # Return user data
    user_data = {'idUser': db_user.userId, 'FirstName': db_user.FirstName,
                 'LastName': db_user.LastName,  'email': db_user.email, 'role': db_user.role}
    return jsonify({"user": user_data})


# Delete user by id
@user.route('/api/v1/user/<idUser>', methods=['DELETE'])
def delete_user(userId):
    # Check if supplied userId correct
    if int(userId)<1:
        return Response(status=400, response='Invalid username supplied')

    # Check if user exists
    db_user = session.query(User).filter_by(idUser=userId).first()
    if not db_user:
        return Response(status=404, response='A user with provided ID was not found.')

    # Delete user
    session.delete(db_user)
    session.commit()
    return Response(response='User was deleted.')