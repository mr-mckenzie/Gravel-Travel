# import flask
from flask import Flask, render_template, Blueprint
from models.location import Location
import repositories.location_repository as location_repo
import repositories.country_repository as country_repo

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route('/locations')
def locations():
    all_locations = location_repo.select_all()
    print(all_locations)
    return render_template('location/index.jinja', input_locations = all_locations)