# import flask
from flask import Flask, render_template, Blueprint
from models.location import Location
from models.location import Country
import repositories.location_repository as location_repo
import repositories.country_repository as country_repo

countries_blueprint = Blueprint("countries", __name__)

#show all countries
@countries_blueprint.route('/countries')
def view_all_countries():
    all_countries = country_repo.select_all()
    return render_template('countries/index.jinja', input_countries = all_countries)

#show single country listing all locations
@countries_blueprint.route('/countries/<id>')
def view_single_country(id):
    current_country = country_repo.select_one(id)
    all_locations = country_repo.get_locations(id)
   #print(all_locations)


    return render_template('/countries/locations.jinja', input_locations = all_locations, input_country = current_country)