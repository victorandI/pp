from models import User, Order, Car
from user import Session

def test():
    session = Session()

    #user = User(id=2,  name="Orest", surname="Chukla",username="Oliver", password="1234", role=1);

    #session.add(user)

    session.commit()

    session.close()