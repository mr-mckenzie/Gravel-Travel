# import flask
from flask import Flask, render_template, Blueprint, redirect
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


# @locations_blueprint.route('/holidays/<id>')
# def single_holiday(id):
#     one_location = location_repo.select_one(id)
#     has_visited = holiday_repo.has_visited(id)
#     on_wishlist = wishlist_repo.on_wishlist(id)
#     print(f'THIS IS ONE LOCATION: {one_location}')
#     return render_template('locations/single_location.jinja', input_location = one_location, has_visited = has_visited, on_wishlist = on_wishlist)
#     #return render_template('locations/index.jinja', input_locations = one_location)