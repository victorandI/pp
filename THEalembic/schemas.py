from marshmallow import Schema, fields
from marshmallow.validate import Length, Range
from werkzeug.security import generate_password_hash

from models import Base


class UserSchema(Schema):

    idUser = fields.Integer(strict=True, required=True, validate=Range(min=0))
    Email = fields.String(required=True, validate=Length(min=3))
    Password = fields.Function(
        deserialize=lambda obj: generate_password_hash(obj), load_only=True
    )
    FirstName = fields.String(required=True, validate=Length(min=3))
    LastName = fields.String(required=True, validate=Length(min=3))
    Role = fields.String(required=True, validate=Length(min=3))

class BookingSchema(Schema):

    IdBooking = fields.Integer(strict=True, required=True, validate=Range(min=0))
    name = fields.String(required=True, validate=Length(min=3))
    User = fields.Integer(strict=True, required=True, validate=Range(min=0))
    Car = fields.Integer(strict=True, required=True, validate=Range(min=0))
    bfrom = fields.Date(required=True)
    buntil = fields.Date(required=True)

class CarSchema(Schema):

    idCar = fields.Integer(strict=True, required=True, validate=Range(min=0))
    brand = fields.String(required=True, validate=Length(min=3))
    model = fields.String(required=True, validate=Length(min=3))
    year = fields.Integer(strict=True, required=True, validate=Range(min=0))
    seatsNum = fields.Integer(strict=True, required=True, validate=Range(min=0))
    status =  fields.String(required=True, validate=Length(min=3))
    Price = fields.Float(strict=True, required=True, validate=Range(min=0))
