# import flask & render template
from flask import Flask, render_template

#import controllers
from controllers.location_controller import locations_blueprint
from controllers.country_controller import countries_blueprint
from controllers.holidays_controller import holidays_blueprint
from controllers.wishlist_controller import wishlist_blueprint

app = Flask(__name__)

app.register_blueprint(locations_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(holidays_blueprint)
app.register_blueprint(wishlist_blueprint)

@app.route('/')
def home():
    return render_template('home.jinja')

if __name__ == '__main__':
    app.run(debug=True)