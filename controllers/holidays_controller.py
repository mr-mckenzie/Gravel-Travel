# import flask
from flask import Flask, render_template, Blueprint, redirect, request
from models.location import Location
import repositories.location_repository as location_repo
import repositories.country_repository as country_repo
import repositories.holiday_repository as holiday_repo
import repositories.wishlist_repository as wishlist_repo

holidays_blueprint = Blueprint("holidays", __name__)

@holidays_blueprint.route('/holidays')
def show_all_holidays():
    all_holidays = holiday_repo.select_all()
    print(all_holidays)
    return render_template('holidays/index.jinja', input_all_holidays = all_holidays)

@holidays_blueprint.route('/holidays/<id>/delete', methods=['POST'])
def delete_entry(id):
    holiday_repo.delete_by_id(id)
    return redirect('/holidays')

@holidays_blueprint.route('/holidays/add', methods=['GET'])
def show_form():
    #all_countries = country_repo.select_all()
    all_locations = location_repo.select_all()
    return render_template('/holidays/add.jinja', input_locations = all_locations)

@holidays_blueprint.route('/holidays/add', methods=['POST'])
def add_holiday():

    location_id = request.form['location_id']
    date_visited = request.form['date']

    location_visited = location_repo.select_one(location_id)

    holiday_repo.save(location_visited, date_visited)

    return redirect('/holidays')