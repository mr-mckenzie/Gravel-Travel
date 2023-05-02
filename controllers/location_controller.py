# import flask
from flask import Flask, render_template, Blueprint
from models.location import Location
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
    print(f'THIS IS ONE LOCATION: {one_location}')
    return render_template('locations/single_location.jinja', input_location = one_location, has_visited = has_visited, on_wishlist = on_wishlist)
    #return render_template('locations/index.jinja', input_locations = one_location)