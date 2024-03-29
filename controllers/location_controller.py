from flask import Flask, render_template, Blueprint, redirect, request
from models.location import Location
from random import randint
import repositories.location_repository as location_repo
import repositories.country_repository as country_repo
import repositories.trip_repository as trip_repo
import repositories.flag_repository as flag_repo

from datetime import timedelta

locations_blueprint = Blueprint("locations", __name__)

#display all locations
@locations_blueprint.route('/locations')
def locations():
    all_locations = location_repo.select_all()

    total_locations = len(all_locations)
    visited_locations_counter = 0

    location_with_visit_and_wishlist = []

    for location in all_locations:
        has_visited = trip_repo.has_visited(location.id)
        has_logged_trip = trip_repo.has_logged_trip(location.id)
        number_of_trips = trip_repo.number_of_trips(location.id)

        location_with_visit_and_wishlist.append(
            {'name': location.name,
            'country':location.country,
            'id':location.id,
            'has_visited':has_visited,
            'has_logged_trip': has_logged_trip,
            'number_of_trips': number_of_trips,
            'rand_bg_pos_x': randint(0,100),
            'rand_bg_pos_y': randint(0,100),
            'flag': flag_repo.get_flag(location.country.name)
            }
        )
        
        if has_visited == True:
            visited_locations_counter += 1

    visited_percentage = 0

    if total_locations > 0 :
        visited_percentage = round((visited_locations_counter/total_locations)*100, 2)
    
    all_countries = country_repo.select_all()

    return render_template('locations/index.jinja', input_locations = location_with_visit_and_wishlist, input_countries = all_countries, visited_locations = visited_locations_counter, total_locations = total_locations, visited_percentage = visited_percentage)

#display single location record
@locations_blueprint.route('/locations/<id>')
def single_location(id):
    one_location = location_repo.select_one(id)
    has_visited = trip_repo.has_visited(id)
    has_logged_trip = trip_repo.has_logged_trip(id)
    on_wishlist = trip_repo.on_wishlist(id)
    all_trips = trip_repo.select_by_location(id)
    flag = flag_repo.get_flag(one_location.country.name)

    trips_with_random_position = []
        
    for trip in all_trips:

        i = 0
        dates_list = []

        while i < trip.length:
            date = trip.date + timedelta(days=i)
            dates_list.append({'date':date, 'x_pos': randint(0,100),'y_pos': randint(0,100), 'month':date.strftime("%B")})
            i += 1
    
        trips_with_random_position.append(
            {'location': trip.location,
            'date':trip.date,
            'length':trip.length,
            'id':trip.id,
            'rand_bg_pos_x': randint(0,100),
            'rand_bg_pos_y': randint(0,100),
            'month': trip.date.strftime("%B"),
            'dates_list': dates_list
            }
        )
    return render_template('locations/single_location.jinja', input_location = one_location, has_visited = has_visited, has_logged_trip=has_logged_trip, on_wishlist = on_wishlist, trips = trips_with_random_position, flag = flag)

#delete location record
@locations_blueprint.route('/locations/<id>/delete', methods=['POST'])
def delete_location(id):
    country_id = location_repo.select_one(id).country.id
    location_repo.delete_by_id(id)
    path = '/countries/'+str(country_id)
    return redirect(path)

#submit 'add location' form
@locations_blueprint.route('/locations/add', methods=['POST'])
def add_country():
    new_location_name = request.form['name']
    new_country_id = (request.form['country_id'])
    new_country = country_repo.select_one(new_country_id)
    new_location = Location(new_location_name, new_country)
    location_repo.save(new_location)
    trip_repo.save_without_trip_data(new_location.id, False)
    return redirect('/locations')

#mark location as visited / on wishlist
@locations_blueprint.route('/locations/<id>/toggle_visited', methods=['POST'])
def toggle_visited(id):

    if trip_repo.on_wishlist(id) == True:
        trip_repo.delete_wishlist_by_location_id(id)
        trip_repo.save_without_trip_data(id, True)
    else:
        trip_repo.delete_wishlist_by_location_id(id)
        trip_repo.save_without_trip_data(id,False)

    path = '/locations/'+str(id)
    return redirect(path)

#delete trip record
@locations_blueprint.route('/locations/<location_id>/trips/<trip_id>/delete', methods=['POST'])
def delete_trip(location_id, trip_id):
    trip_repo.delete_by_id(trip_id)
    path = '/locations/'+str(location_id)

    if trip_repo.number_of_trips(location_id) == 0:
        trip_repo.save_without_trip_data(location_id, False)

    return redirect(path)

#add a trip record
@locations_blueprint.route('/locations/<location_id>/trips/add', methods=['POST'])
def add_trip(location_id):
    location_id = request.form['location_id']
    date_visted = request.form['date']
    trip_length = request.form['length']
    location_visited = location_repo.select_one(location_id)
    trip_repo.save(location_visited, date_visted, trip_length, True)
    
    trip_repo.delete_wishlist_by_location_id(location_id)

    return redirect('/locations/' + location_id)

#change country name
@locations_blueprint.route('/locations/<id>/edit', methods=['POST'])
def edit_location_name(id):
    new_name = request.form['name']
    location_repo.update_name(id, new_name)
    path = '/locations/'+str(id)
    return redirect(path)