import requests_cache

from flask import render_template, jsonify, Flask
from API.Base_API import BaseAPI
from API.InternetConnection import Connection

# Global variable
INTERNETCONNECTION = False
app = Flask(__name__)
requests_cache.install_cache(cache_name='My_cache', backend='sqlite', expire_after=10)


@app.route("/<countryName>/<category>/")
def outputPage(countryName, category):
    baseAPI = BaseAPI()
    categories = category.split(",")
    countryInfo = []
    for i in categories:
        countryInfo.append(baseAPI.get_country_info(str(countryName), i))

    if countryInfo is None:
        countryInfo = "Not Found Or Invalid Input"

    return jsonify(countryInfo)


@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")


if __name__ == '__main__':
    INTERNETCONNECTION = Connection.CheckInternetConnection()
    app.run(debug=True)
