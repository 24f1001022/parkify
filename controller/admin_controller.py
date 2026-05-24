from flask import request,flash,redirect,url_for,render_template
from sqlalchemy import func
from models.models import ParkingLot,db,ParkingSpot,User,Reservation


def add_parking_lot():
    prime_location_name=request.form.get('location_name')
    if prime_location_name=="":
        flash('Location name is required','danger')
        return redirect(url_for('add_lot'))
    address=request.form.get('address')
    pincode=request.form.get('pin_code')
    price=request.form.get('price_per_hour')
    max_spots=request.form.get('max_spots')
    parkinglot=ParkingLot(prime_location_name=prime_location_name,address=address,pincode=pincode,price=price,max_spots=max_spots)
    db.session.add(parkinglot)
    db.session.commit()
    for _ in range(int(max_spots)):
        spot = ParkingSpot(lot_id=parkinglot.id)
        db.session.add(spot)
    db.session.commit()
    flash('Parking lot added sucessfuly','success')
    return redirect(url_for('add_lot'))


def edit_lot_handle(id):
    parkinglot=ParkingLot.query.get(id)
    inital_spots=parkinglot.max_spots
    parkinglot.prime_location_name=request.form.get('location_name')
    if parkinglot.prime_location_name=="":
        flash('Location name is required','danger')
        return redirect(url_for('edit_lot', id=id))
    parkinglot.address=request.form.get('address')
    parkinglot.pincode=request.form.get('pin_code')
    parkinglot.price=request.form.get('price_per_hour')
    parkinglot.max_spots=request.form.get('max_spots')
    db.session.commit()
    flash('Detail Updated Successfully','success')
    return redirect(url_for('admin'))


def delete_lot_handle(id):
    parkinglot=ParkingLot.query.get(id)
    for x in parkinglot.spots:
        if x.status != 'A':
            flash('ALL SPOTS OF THIS LOT ARE NOT EMPTY','warning')
            return redirect(url_for('admin'))
    db.session.delete(parkinglot)
    db.session.commit()
    flash('PARKING LOT DELETED SUCESSFULY','success')
    return redirect(url_for('admin'))
    
def delete_spot_handle(id):
    parkingspot=ParkingSpot.query.get(id)
    if parkingspot.status=='O':
        flash('Occupied Parking Spot Not Allow To Delete','warning')
        return redirect(url_for('admin'))
    db.session.delete(parkingspot)
    db.session.commit()
    flash('Parking Spot Deleted Succesfully','success')
    return redirect(url_for('admin'))

def handle_search():
    filter_by=request.args.get('filter_by','Location')
    query=request.args.get('query','').strip()
    results=[]
    if filter_by=='user_id':
        user_secnd = User.query.filter_by(id=int(query)).first()
        if user_secnd:
            lot_ids = [res.spot.lot_id for res in user_secnd.reservations]
            results = ParkingLot.query.filter(ParkingLot.id.in_(lot_ids)).all()
    elif filter_by == "location":
        results = ParkingLot.query.filter(ParkingLot.prime_location_name.ilike(f"%{query}%")).all()
    elif filter_by == "pincode":
        results = ParkingLot.query.filter(ParkingLot.pincode.ilike(f"%{query}%")).all()
    return render_template('admin_search.html',results=results) 

def handle_admin_summary():
    revenue_data = (
        db.session.query(ParkingLot.prime_location_name, func.sum(Reservation.total_cost))
        .join(ParkingSpot, ParkingSpot.lot_id == ParkingLot.id)
        .join(Reservation, Reservation.spot_id == ParkingSpot.id)
        .group_by(ParkingLot.id)
        .all()
    )
    availability_data = []
    lots = ParkingLot.query.all()
    for lot in lots:
        spots = ParkingSpot.query.filter_by(lot_id=lot.id).all()
        occupied = sum(1 for spot in spots if spot.status == 'O')
        available = sum(1 for spot in spots if spot.status == 'A')
        availability_data.append({
            'location': lot.prime_location_name,
            'available': available,
            'occupied': occupied
        })

    return render_template("admin_summary.html", revenue_data=revenue_data, availability_data=availability_data)
    