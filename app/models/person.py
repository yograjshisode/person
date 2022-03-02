from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)


    def __init__(self, name, address, email, mobile_number):
        self.name = name
        self.address = address
        self.email = email
        self.mobile_number = mobile_number

    def __repr__(self):
        return '<Person %r>' % self.id

    @property
    def serialize(self):
       return {
           'person_id': self.id,
           'name': self.name,
           'address': self.address,
           'email': self.email,
           'mobile_number': self.mobile_number
       }
