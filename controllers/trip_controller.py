from flask import Flask, render_template, Blueprint, redirect, request
import repositories.location_repository as location_repo
import repositories.trip_repository as trip_repo
import repositories.wishlist_repository as wishlist_repo
from random import randint
from datetime import datetime

trips_blueprint = Blueprint("trips", __name__)

#display all trip records
@trips_blueprint.route('/trips')
def show_all_trips():
    all_trips = trip_repo.select_all_trips()

    trips_with_random_position = []

    for trip in all_trips:

        trips_with_random_position.append(
            {'trip':trip,
            'rand_bg_pos_x': randint(0,100),
            'rand_bg_pos_y': randint(0,100),
            'month': trip[1].strftime("%B")
            }
        )
    
    days_travelled = trip_repo.days_travelled()


    return render_template('trips/index.jinja', input_trips = trips_with_random_position, days_travelled = days_travelled)

#delete a holiday
@trips_blueprint.route('/trips/<id>/delete', methods=['POST'])
def delete_entry(id):
    trip_repo.delete_by_id(id)
    return redirect('/trips')

#go to add trip form
@trips_blueprint.route('/trips/add', methods=['GET'])
def show_form():
    all_locations = location_repo.select_all()
    return render_template('/trips/add.jinja', input_locations = all_locations)

#save a trip via 'add trip' form
@trips_blueprint.route('/trips/add', methods=['POST'])
def add_trip():
    location_id = request.form['location_id']
    date_visited = request.form['date']
    trip_length = request.form['length']
    location_visited = location_repo.select_one(location_id)
    trip_repo.save(location_visited, date_visited, trip_length, False)
    return redirect('/trips')

@trips_blueprint.route('/wishlist')
def show_wishlist():
    wishlist = trip_repo.select_all_wishlist()
    #print(wishlist)
    return render_template('wishlist/index.jinja', wishlist = wishlist)

#delete a wishlist record
@trips_blueprint.route('/wishlist/<location_id>/delete', methods=['POST'])
def delete_wishlist(location_id):
    trip_repo.delete_wishlist_by_location_id(location_id)
    return redirect('/wishlist')