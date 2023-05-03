# import flask
from flask import Flask, render_template, Blueprint, redirect
import repositories.wishlist_repository as wishlist_repo

wishlist_blueprint = Blueprint("wishlist", __name__)

#display all wishlist locations
@wishlist_blueprint.route('/wishlist')
def show_wishlist():
    wishlist = wishlist_repo.select_all()
    #print(wishlist)
    return render_template('wishlist/index.jinja', wishlist = wishlist)

#delete a wishlist record
@wishlist_blueprint.route('/wishlist/<location_id>/delete', methods=['POST'])
def delete_entry(location_id):
    wishlist_repo.delete_by_location_id(location_id)
    return redirect('/wishlist')