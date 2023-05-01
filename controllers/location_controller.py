# import flask
from flask import Flask, render_template, Blueprint
from models.location import Location
import repositories.location_repository as location_repo

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route('/locations')
def locations():
    all_locations = location_repo.select_all
    render_template('locations.jinja', input_locations = all_locations)