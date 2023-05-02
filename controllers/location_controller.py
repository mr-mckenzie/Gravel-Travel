# import flask
from flask import Flask, render_template, Blueprint, redirect, request
from models.location import Location
from models.country import Country
import repositories.location_repository as location_repo
import repositories.country_repository as country_repo
import repositories.holiday_repository as holiday_repo
import repositories.wishlist_repository as wishlist_repo

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route('/locations')
def locations():
    all_locations = location_repo.select_all()
    all_holidays = holiday_repo.select_all()
    wishlist = wishlist_repo.select_all()
    #print(all_locations)
    #print(all_holidays)
    return render_template('locations/index.jinja', input_locations = all_locations, input_all_holidays = all_holidays, input_wishlist = wishlist)

@locations_blueprint.route('/locations/<id>')
def single_location(id):
    one_location = location_repo.select_one(id)
    has_visited = holiday_repo.has_visited(id)
    on_wishlist = wishlist_repo.on_wishlist(id)
    holidays = holiday_repo.select_by_location(id)
    print(f'THIS IS ONE LOCATION: {one_location}')
    return render_template('locations/single_location.jinja', input_location = one_location, has_visited = has_visited, on_wishlist = on_wishlist, holidays = holidays)
    #return render_template('locations/index.jinja', input_locations = one_location)

@locations_blueprint.route('/locations/<id>/delete', methods=['POST'])
def delete_location(id):
    #country_id = location_repo.select_one(id).country.id
    location_repo.delete_by_id(id)
    return redirect('/locations')

@locations_blueprint.route('/locations/add', methods=['GET'])
def show_form():
    all_countries = country_repo.select_all()
    return render_template('/locations/add.jinja', input_countries = all_countries)

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

@locations_blueprint.route('/locations/<id>/toggle_wishlist', methods=['POST'])
def toggle_wishlist(id):

    if wishlist_repo.on_wishlist(id) == True:
        wishlist_repo.delete_by_location_id(id)
    else:
        wishlist_repo.save(id)

    path = '/locations/'+str(id)

    return redirect(path)