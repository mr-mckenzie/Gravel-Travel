from flask import Flask, render_template, Blueprint, redirect, request
import repositories.location_repository as location_repo
import repositories.trip_repository as trip_repo
import repositories.flag_repository as flag_repo
from random import randint
from datetime import timedelta

trips_blueprint = Blueprint("trips", __name__)

#display all trip records
@trips_blueprint.route('/trips')
def show_all_trips():
    all_trips = trip_repo.select_all_trips()
    all_locations = location_repo.select_all()

    trips_with_random_position = []

    country_counter = []
    location_counter = []

    for trip in all_trips:

        end_date = trip.date + timedelta(days=trip.length)

        trips_with_random_position.append(
            {'location': trip.location,
            'start_date':trip.date,
            'end_date': end_date,
            'length':trip.length,
            'id':trip.id,
            'rand_bg_pos_x': randint(0,100),
            'rand_bg_pos_y': randint(0,100),
            'start_month': trip.date.strftime("%B"),
            'end_month': end_date.strftime("%B"),
            'random_int': randint(1,5)
            }
        )

        location_counter.append(trip.location.id)
        country_counter.append(trip.location.country.id)
    
    days_travelled = trip_repo.days_travelled()
    countries_visited = len(set(country_counter))
    locations_visited = len(set(location_counter))
    trips_taken = len(all_trips)

    return render_template('trips/index.jinja', input_trips = trips_with_random_position, input_locations = all_locations, days_travelled = days_travelled, locations_visited = locations_visited, countries_visited = countries_visited, trips_taken = trips_taken)

#delete a trip
@trips_blueprint.route('/trips/<id>/delete', methods=['POST'])
def delete_entry(id):
    trip = trip_repo.get_single_trip(id)
    trip_repo.delete_by_id(id)

    if trip_repo.number_of_trips(trip.location.id) == 0:
        trip_repo.save_without_trip_data(trip.location.id, False)
        
    return redirect('/trips')


#save a new trip 
@trips_blueprint.route('/trips/add', methods=['POST'])
def add_trip():
    location_id = request.form['location_id']
    date_visited = request.form['date']
    trip_length = request.form['length']
    location_visited = location_repo.select_one(location_id)
    trip_repo.save(location_visited, date_visited, trip_length, True)
    trip_repo.delete_wishlist_by_location_id(location_id)
    return redirect('/trips')

@trips_blueprint.route('/wishlist')
def show_wishlist():
    wishlist = trip_repo.select_all_wishlist()
    total_locations = len(wishlist)

    wishlist_with_random_position = []

    for location in wishlist:
        wishlist_with_random_position.append(
            {'name': location.name,
             'country':location.country,
            'id': location.id,
            'rand_bg_pos_x': randint(0,100),
            'rand_bg_pos_y': randint(0,100),
            'flag': flag_repo.get_flag(location.country.name)
            }
        )
    
    return render_template('wishlist/index.jinja', wishlist = wishlist_with_random_position, total_locations = total_locations)

#update trip
@trips_blueprint.route('/locations/<location_id>/trips/<trip_id>/edit', methods=['POST'])
def update_trip(location_id, trip_id):
    new_departure_date = request.form['date']
    new_trip_length = request.form['length']
    trip_repo.update_trip(new_departure_date, new_trip_length, trip_id)
    path = '/locations/'+str(location_id)
    return redirect(path)