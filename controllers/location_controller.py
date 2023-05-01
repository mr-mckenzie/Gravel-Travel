# import flask
from flask import Flask, render_template, Blueprint
from models.location import Location
import repositories.location_repository as location_repo
import repositories.country_repository as country_repo

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route('/locations')
def locations():
    all_locations = location_repo.select_all()
    #print(all_locations)
    return render_template('locations/index.jinja', input_locations = all_locations)

@locations_blueprint.route('/locations/<id>')
def single_location(id):
    one_location = [location_repo.select_one(id)]
    #print(one_location)
    return render_template('locations/index.jinja', input_locations = one_location)