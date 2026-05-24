from flask import request,flash,redirect,url_for,session,render_template
from models.models import User,db,ParkingLot,ParkingSpot,Reservation
from datetime import datetime


def handle_login():
    email=request.form.get('email')
    password=request.form.get('password')
    if email=="" or password=="":
        flash('Email and password cannot be empty','danger')
        return redirect(url_for('loginpage'))
    user=User.query.filter_by(email=email).first()
    if not user:
        flash('Plese check details you entered','danger')
        return redirect(url_for('loginpage'))
    if not user.check_password(password):
        flash('Password you entered is wrong','danger')
        return redirect(url_for('loginpage'))
    session['user_id']=user.id
    return redirect(url_for('home'))

def handle_signup():
    email=request.form.get('email')
    password=request.form.get('password')
    full_name=request.form.get('full_name')
    pin_code=request.form.get('pin_code')
    address=request.form.get('address')
    if email=="" or password=="":
        flash('Email and password cannot be empty','danger')
        return redirect(url_for('signuppage'))
    user=User.query.filter_by(email=email).first()
    if user:
        flash('User with this Email already exist','info')
        return redirect(url_for('signuppage'))
    user=User(email=email,password=password,full_name=full_name,address=address,pin_code=pin_code)
    db.session.add(user)
    db.session.commit()
    flash('User registered successfuly','success')
    return redirect(url_for('loginpage'))
def edit_profile_handle():
    user=User.query.get(session['user_id'])
    user.email=request.form.get('email')
    user.full_name=request.form.get('full_name')
    user.pin_code=request.form.get('pin_code')
    user.address=request.form.get('address')
    db.session.commit()
    flash('Profle Updated Sucessfuly','success')
    return redirect(url_for('profile'))

def handle_booking(id):
    spot_id=request.form.get('SpotId')
    lot_id=request.form.get('LotId')
    user_id=request.form.get('UserId')
    vehical_no=request.form.get('VehicalNo')
    cost_per_unit=ParkingLot.query.get(lot_id).price
    reservation=Reservation(spot_id=spot_id,user_id=user_id,vehical_no=vehical_no,cost_per_unit=cost_per_unit)
    spot=ParkingSpot.query.filter_by(id=spot_id).first()
    spot.status='O'
    db.session.add(reservation)
    db.session.commit()
    flash('Your Spot Is Booked Successfuly','success')
    return redirect(url_for('home'))

def handle_logout():
    session.pop('user_id',None)
    return redirect(url_for('loginpage'))
    
def handle_release_parking(id):
    reservation=Reservation.query.get(id)
    reservation.leaving_timestamp=datetime.utcnow() 
    duration=((reservation.leaving_timestamp-reservation.parking_timestamp).total_seconds())/3600
    reservation.total_cost = round(duration * reservation.cost_per_unit, 2)
    if reservation.user_id != session['user_id']:
        flash("You are not authorized to release this reservation.", "danger")
        return redirect(url_for('home'))
    spot = ParkingSpot.query.get(reservation.spot_id)
    spot.status = 'A'
    db.session.commit()
    flash(f"Parking released Successfuly", "success")
    return redirect(url_for('home'))

def handle_summary():
    user_id=session.get('user_id')
    used_spots_data = (
        db.session.query(ParkingLot.prime_location_name, db.func.count(Reservation.id))
        .join(ParkingSpot, ParkingSpot.lot_id == ParkingLot.id)
        .join(Reservation, Reservation.spot_id == ParkingSpot.id)
        .filter(Reservation.user_id == user_id)
        .group_by(ParkingLot.prime_location_name)
        .all()
    )
    chart_data = [{'location': loc, 'used': count} for loc, count in used_spots_data]
    return render_template('user_summary.html', chart_data=chart_data) 
     