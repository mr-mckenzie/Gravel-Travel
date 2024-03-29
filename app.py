# import flask & render template
from flask import Flask, render_template

#import controllers
from controllers.location_controller import locations_blueprint
from controllers.country_controller import countries_blueprint
from controllers.trip_controller import trips_blueprint

app = Flask(__name__)

app.register_blueprint(locations_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(trips_blueprint)

@app.route('/')
def home():
    return render_template('home.jinja')

if __name__ == '__main__':
    app.run(debug=True)