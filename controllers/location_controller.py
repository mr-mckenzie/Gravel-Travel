from flask import Flask, render_template, Blueprint, redirect, request
from models.location import Location
from random import randint
import repositories.location_repository as location_repo
import repositories.country_repository as country_repo
import repositories.holiday_repository as holiday_repo
import repositories.trip_repository as trip_repo
import repositories.wishlist_repository as wishlist_repo

locations_blueprint = Blueprint("locations", __name__)

#display all locations
@locations_blueprint.route('/locations')
def locations():
    all_locations = location_repo.select_all()

    location_with_visit_and_wishlist = []

    for location in all_locations:
        has_visited = trip_repo.has_visited(location.id)
        on_wishlist = trip_repo.on_wishlist(location.id)
        location_with_visit_and_wishlist.append(
            {'location':location, 
            'has_visited':has_visited,
            'on_wishlist':on_wishlist,
            'rand_bg_pos_x': randint(0,100),
            'rand_bg_pos_y': randint(0,100)
            }
            )

    return render_template('locations/index.jinja', input_locations = location_with_visit_and_wishlist)

#display single location record
@locations_blueprint.route('/locations/<id>')
def single_location(id):
    one_location = location_repo.select_one(id)
    has_visited = trip_repo.has_visited(id)
    on_wishlist = trip_repo.on_wishlist(id)
    holidays = trip_repo.select_by_location(id)
    # print(f'THIS IS ONE LOCATION: {one_location}')
    return render_template('locations/single_location.jinja', input_location = one_location, has_visited = has_visited, on_wishlist = on_wishlist, holidays = holidays)

#delete location record
@locations_blueprint.route('/locations/<id>/delete', methods=['POST'])
def delete_location(id):
    country_id = location_repo.select_one(id).country.id
    location_repo.delete_by_id(id)
    path = '/countries/'+str(country_id)
    return redirect(path)

#go to 'add location' form
@locations_blueprint.route('/locations/add', methods=['GET'])
def show_form():
    all_countries = country_repo.select_all()
    return render_template('/locations/add.jinja', input_countries = all_countries)

#submit 'add location' form
@locations_blueprint.route('/locations/add', methods=['POST'])
def add_country():
    new_location_name = request.form['name']
    #print(f'THIS IS NEW COUNTRY NAME: {new_location_name}')
    new_country_id = (request.form['country_id'])
    #print(f'THIS IS NEW COUNTRY INSTANCE: {new_country_id}')
    new_country = country_repo.select_one(new_country_id)
    new_location = Location(new_location_name, new_country)
    location_repo.save(new_location)
    return redirect('/locations')

#add/remove location from wishlist
@locations_blueprint.route('/locations/<id>/toggle_wishlist', methods=['POST'])
def toggle_wishlist(id):

    if trip_repo.on_wishlist(id) == True:
        trip_repo.delete_wishlist_by_location_id(id)
    else:
        trip_repo.add_to_wishlist(id)

    path = '/locations/'+str(id)
    return redirect(path)

#delete holiday record
@locations_blueprint.route('/locations/<location_id>/holiday/<holiday_id>/delete', methods=['POST'])
def delete_trip(location_id, holiday_id):
    trip_repo.delete_by_id(holiday_id)
    path = '/locations/'+str(location_id)
    return redirect(path)