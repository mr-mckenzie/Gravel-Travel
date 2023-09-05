# Gravel Travel

Gravel Travel is a travel wish list app.

- Track countries and locations you want to visit 
- Log trips to locations you have visited.

## Installing the app

System requirements

You will need Python3 (with Flask and psycopg2) and PostgreSQL to run Gravel Travel.

When downloaded run the following command (from the root project file) to install the correct packages (Flask & psycopg2):

    pip install requirements.txt


## Running the app

Run the following command on the terminal to create the sql database.

    createdb travel_tracker

Next (from the root project file) run the following command to initiate the database tables and demo data.

    psql -d travel_tracker -f db/travel_tracker.sql

Run the app (again from the root project file) with the following command.

    Flask run

The terminal will tell you the port the app is running on. For example:

    * Running on http://127.0.0.1:5001

Navigate to this page with your browser of choice and you can start using the app. 

Note that Gravel Travel is optimised for use with Google Chrome, however it should still run on alternative browsers such as Safari or Edge.

## Exiting the app

To stop the app running press the following keys on the terminal.

    CTRL+C