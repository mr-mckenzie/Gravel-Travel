from flask import Flask, render_template, Blueprint, request, redirect
from models.location import Location
from models.location import Country
from random import randint
import repositories.continent_repository as continent_repo
import repositories.location_repository as location_repo
import repositories.country_repository as country_repo
import repositories.trip_repository as trip_repo
import repositories.flag_repository as flag_repo

countries_blueprint = Blueprint("countries", __name__)

#show all countries
@countries_blueprint.route('/countries')
def view_all_countries():
    all_countries = continent_repo.all_by_continent()
    continents = continent_repo.select_all()
    return render_template('countries/index.jinja', input_countries = all_countries, continents = continents)

#add a country
@countries_blueprint.route('/countries', methods=['POST'])
def add_a_country():
    new_country_name =request.form['name']
    continent_id = request.form['continent_id']
    continent = continent_repo.select_one(continent_id)
    new_country = Country(new_country_name, continent)
    country_repo.save(new_country)
    return redirect('/countries')

#show a single country and list all locations in country
@countries_blueprint.route('/countries/<id>')
def view_single_country(id):
    current_country = country_repo.select_one(id)
    all_locations = country_repo.get_locations(id)
    continents = continent_repo.select_all()

    locations_with_visit_and_wishlist_data = []

    locations_visited_counter = 0
    days_travelled_counter = 0
    trips_counter = 0

    for location in all_locations:
        has_visited = trip_repo.has_visited(location.id)
        has_logged_trip = trip_repo.has_logged_trip(location.id)
        number_of_trips = trip_repo.number_of_trips(location.id)
        on_wishlist = trip_repo.on_wishlist(location.id)
        
        locations_with_visit_and_wishlist_data.append(
            {'name':location.name,
            'country':location.country,
            'id': location.id,
            'has_visited':has_visited,
            'has_logged_trip': has_logged_trip,
            'number_of_trips': number_of_trips,
            'on_wishlist':on_wishlist,
            'rand_bg_pos_x': randint(0,100),
            'rand_bg_pos_y': randint(0,100)
            }
        )
        if has_visited == True:
            locations_visited_counter += 1
            days_travelled_counter += trip_repo.days_travelled_in_location(location.id)
            trips_counter += trip_repo.number_of_trips(location.id)
        
    total_locations = len(all_locations)
    percentage_visited = 0

    if total_locations > 0 :
        percentage_visited = round((locations_visited_counter/total_locations)*100, 2)
    
    trip_data = {
        'total_locations': total_locations,
        'locations_visited': locations_visited_counter,
        'percentage_visited': percentage_visited,
        'trip_total': trips_counter,
        'days_travelled': days_travelled_counter
    }
    
    flag = flag_repo.get_flag(current_country.name)

    return render_template('/countries/single_country.jinja', input_locations = locations_with_visit_and_wishlist_data, input_country = current_country, trip_data = trip_data, flag=flag, continents = continents)

#delete a country
@countries_blueprint.route('/countries/<id>/delete', methods=['POST'])
def delete_country(id):
    country_repo.delete_by_id(id)
    return redirect('/countries')

#update country name and/or continent
@countries_blueprint.route('/countries/<id>/edit', methods=['POST'])
def edit_country(id):
    new_name = request.form['name']
    country_repo.update_name(id, new_name)
    new_continent_id = request.form['continent_id']
    country_repo.update_continent(id, new_continent_id)
    path = '/countries/'+str(id)
    return redirect(path)

#add a location to a country
@countries_blueprint.route('/countries/<id>/add_location', methods=['POST'])
def add_location(id):
    new_location_name = request.form['name']
    new_country_id = (request.form['country_id'])
    new_country = country_repo.select_one(new_country_id)
    new_location = Location(new_location_name, new_country)
    location_with_id = location_repo.save(new_location)
    trip_repo.add_to_wishlist(location_with_id.id)
    
    path = '/countries/'+str(id)
    return redirect(path)