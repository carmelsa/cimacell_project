"""
The application routing handler
"""

from flask import Flask, jsonify, request
from db_handler import DBHandler

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Welcome to carmel weather searcher"


@app.route('/weather/data')
def get_weather_by_location():
    lon = request.args.get("lon")
    lat = request.args.get("lat")
    db_handler = DBHandler()
    result = db_handler.get_weather_by_location(lon, lat)
    return jsonify(result)


@app.route('/weather/summarize')
def get_weather_summarize():
    lon = request.args.get("lon")
    lat = request.args.get("lat")
    db_handler = DBHandler()
    result = db_handler.get_max_from_db(lon, lat)
    return jsonify(result)


def main():
    app.run(port=5000)


if __name__ == '__main__':
    main()
