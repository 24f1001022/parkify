from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app

db=SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    passhash = db.Column(db.String(120), nullable=False)
    full_name=db.Column(db.String(100))
    pin_code=db.Column(db.String(6))
    address=db.Column(db.String(120))
    is_admin=db.Column(db.Boolean,nullable=False,default=False)
    reservations = db.relationship('Reservation', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.passhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passhash, password)

class ParkingLot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prime_location_name = db.Column(db.String(100),nullable=False)
    address = db.Column(db.String(200))
    pincode = db.Column(db.String(6))
    price = db.Column(db.Float)
    max_spots = db.Column(db.Integer)
    spots = db.relationship('ParkingSpot', backref='lot', lazy=True, cascade='all, delete-orphan')

class ParkingSpot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lot_id = db.Column(db.Integer, db.ForeignKey('parking_lot.id'), nullable=False)
    status = db.Column(db.String(1),default='A')
    reservations=db.relationship('Reservation',backref='spot',lazy=True, cascade='all, delete-orphan')

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spot_id= db.Column(db.Integer, db.ForeignKey('parking_spot.id'), nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehical_no=db.Column(db.String(15))
    parking_timestamp = db.Column(db.DateTime,default=datetime.utcnow)
    leaving_timestamp = db.Column(db.DateTime)
    cost_per_unit = db.Column(db.Float)
    total_cost=db.Column(db.Float)

with app.app_context():
    db.create_all()
    admin=User.query.filter_by(is_admin=True).first()
    if not admin:
        admin=User(email='admin@parkify.com',password='admin',full_name='admin',is_admin=True)
        db.session.add(admin)
        db.session.commit()
