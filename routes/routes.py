from flask import render_template, redirect, url_for,request, session, g, flash
from models.models import User,ParkingLot,ParkingSpot,Reservation
from datetime import datetime
from functools import wraps
from sqlalchemy import or_
from app import app
from controller.user_controller import handle_login, handle_signup, handle_booking, edit_profile_handle, handle_release_parking, handle_summary, handle_logout
from controller.admin_controller import add_parking_lot, delete_lot_handle,edit_lot_handle,handle_search, delete_spot_handle, handle_admin_summary

# DECORATOR
def check_auth(func):
    @wraps(func)
    def decorator_func(*args,**kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        user=User.query.get(session['user_id'])
        if user is None:
            session.pop('user_id', None)
            return redirect(url_for('login'))
        g.user=user
        return func(*args,**kwargs)
    return decorator_func

def admin_required(func):
    @wraps(func)
    def decorator_func(*args,**kwargs): 
        if 'user_id' not in session:
            return redirect(url_for('login'))
        user=User.query.get(session['user_id'])
        if user is None:
            session.pop('user_id', None)
            return redirect(url_for('login'))
        g.user=user
        if not user.is_admin:
            flash('YOUR ARE NOT ALLOW DO THIS','info')
            return redirect(url_for('home'))
        return func(*args,**kwargs)
    return decorator_func 

@app.route('/',methods=['POST','GET'])
@check_auth
def home():
    user = User.query.get(session['user_id'])
    if not user:
        return render_template('login.html')
    if user.is_admin:
        return redirect(url_for('admin'))
    search_query = request.args.get('query', '').strip().lower()
    parkinglot = []
    if search_query:
        parkinglot = ParkingLot.query.filter(or_(ParkingLot.prime_location_name.ilike('%' + search_query + '%'),ParkingLot.pincode.ilike('%' + search_query + '%'))).all()
        return render_template('user_dashbord.html',user=user,parkinglot=parkinglot,search_query=search_query)
    return render_template('user_dashbord.html',user=user)




# COMMON ROUTES
@app.route('/login')
def loginpage():
    return render_template('login.html')
 
@app.route('/login',methods=['POST'])
def login():
    return handle_login()

@app.route('/signup')
def signuppage():
    return render_template('signup.html')

@app.route('/signup',methods=['POST'])
def signup():
    return handle_signup()

@app.route('/profile')
@check_auth
def profile():
    return render_template('profile_page.html')


@app.route('/edit_profile',methods=['POST','GET'])
@check_auth
def edit_profile():
    return render_template('edit_profile.html')

@app.route('/save_profile_changes',methods=['POST'])
@check_auth
def save_profile_changes():
    return edit_profile_handle()

@app.route('/logout')
@check_auth
def logout():
    return handle_logout()




# ADMIN ROUTES

@app.route('/admin')
@admin_required
def admin():
    user=User.query.get(session['user_id'])
    if not user.is_admin:
       flash('You are not authorised to access this page')
       return redirect(url_for('home'))
    else:
        return render_template('admin_dashbord.html',parkinglot=ParkingLot.query.all(),user=user)

    

@app.route('/lot/add')
@admin_required
def add_lot():
    return render_template('add_lot.html')

@app.route('/lot/add',methods=['POST'])
@admin_required
def add_lot_post():
    return add_parking_lot()

@app.route('/spotdetails/<int:id>')
@admin_required
def spotdetails(id):
    return render_template('spotdetails.html',parkingspot=ParkingSpot.query.get(id))

@app.route('/lot/<int:id>/edit')
@admin_required
def edit_lot(id):
    return render_template('edit_lot.html',parkinglot=ParkingLot.query.get(id))

@app.route('/lot/<int:id>/edit',methods=['POST'])
@admin_required
def save_edit_lot_changes(id):
    return edit_lot_handle(id)

@app.route('/lot/<int:id>/delete')
@admin_required
def delete_lot(id):
    return render_template('delete_lot.html',parkinglot=ParkingLot.query.get(id))

@app.route('/lot/<int:id>/delete',methods=['POST'])
@admin_required
def delete_lot_post(id):
    return delete_lot_handle(id)

@app.route('/spot/<int:id>/delete',methods=['POST','GET'])
@admin_required
def delete_spot_post(id):
    return delete_spot_handle(id)

@app.route('/search')
@admin_required
def search():
   return handle_search()

@app.route('/admin/summary')
@admin_required
def admin_summary():
    return handle_admin_summary()

@app.route('/users')
@admin_required
def users():
    all_users = User.query.all()
    return render_template('all_users.html', users=all_users)




# USER ROUTES

@app.route('/booking/<int:id>')
@check_auth
def booking(id):
    parkingspot=ParkingSpot.query.filter_by(lot_id=id, status='A').order_by(ParkingSpot.id).first()
    if parkingspot:
        return render_template('booking_page.html',parkinglot=ParkingLot.query.get(id),available_spot=parkingspot)
    else:
        flash('NO SPOTS ARE BOOKED CHOSE ANOTHER LOCATION','info')
        return redirect(url_for('home'))
    
@app.route('/booking/<int:id>',methods=['POST'])
@check_auth
def booking_post(id):
    return handle_booking(id)

@app.route('/release/<int:id>')
@check_auth
def release_parking(id):
    reservation=Reservation.query.get(id)
    if not reservation:
        flash('Reservation not found','danger')
        return redirect(url_for('home'))
    reservation.leaving_timestamp=datetime.utcnow()
    duration=((reservation.leaving_timestamp-reservation.parking_timestamp).total_seconds())/3600
    reservation.total_cost = round(duration * reservation.cost_per_unit, 2)
    return render_template('release_parking.html',reservation=reservation)

@app.route('/release/<int:id>',methods=['POST'])
@check_auth
def release_parking_post(id):
    return handle_release_parking(id)


@app.route('/more/details/<int:id>')
@check_auth
def moredetails(id):
    parkingspot=ParkingSpot.query.get(id)
    if not parkingspot:
        flash('Spot not found','danger')
        return redirect(url_for('admin'))
    reservation=Reservation.query.filter_by(spot_id=id).order_by(Reservation.id.desc()).first()
    if not reservation:
        flash('No reservation found for this spot','danger')
        return redirect(url_for('admin'))
    reservation.leaving_timestamp=datetime.utcnow()
    duration=((reservation.leaving_timestamp-reservation.parking_timestamp).total_seconds())/3600
    reservation.total_cost = round(duration * reservation.cost_per_unit, 2)
    return render_template('moredetails.html',parkingspot=parkingspot,reservation=reservation)

@app.route('/user/summary')
@check_auth
def user_summary():
    return handle_summary()