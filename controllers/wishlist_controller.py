# import flask
from flask import Flask, render_template, Blueprint, redirect
from models.location import Location
import repositories.location_repository as location_repo
import repositories.country_repository as country_repo
import repositories.holiday_repository as holiday_repo
import repositories.wishlist_repository as wishlist_repo

wishlist_blueprint = Blueprint("wishlist", __name__)

@wishlist_blueprint.route('/wishlist')
def show_wishlist():
    wishlist = wishlist_repo.select_all()
    #print(wishlist)
    return render_template('wishlist/index.jinja', wishlist = wishlist)

@wishlist_blueprint.route('/wishlist/<location_id>/delete', methods=['POST'])
def delete_entry(location_id):
    wishlist_repo.delete_by_location_id(location_id)
    return redirect('/wishlist')


# @locations_blueprint.route('/holidays/<id>')
# def single_holiday(id):
#     one_location = location_repo.select_one(id)
#     has_visited = holiday_repo.has_visited(id)
#     on_wishlist = wishlist_repo.on_wishlist(id)
#     print(f'THIS IS ONE LOCATION: {one_location}')
#     return render_template('locations/single_location.jinja', input_location = one_location, has_visited = has_visited, on_wishlist = on_wishlist)
#     #return render_template('locations/index.jinja', input_locations = one_location)