import urllib

import flask
from flask import render_template, request
from API.Base_API import BaseAPI
from API.offline_Data import OfflineData

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Global variable
INTERNETCONNECTION = False


@app.route('/', methods=["POST", "GET"])
def home(output=""):
    if request.method == "POST":
        category = request.form.get("CategoryMenu")
        country = request.form.get("CountryMenu")

        baseAPI = BaseAPI()

        countryInfo = None
        if INTERNETCONNECTION:
            countryInfo = baseAPI.get_country_info(country)
        else:
            o = OfflineData()
            countryInfo = o.GetData(country)

        if countryInfo is not None:
            output = countryInfo[0]
        else:
            output = "Not Found"
        screenData = output[str(category)]

        return render_template("home.html", OUTPUT=screenData)
    else:
        return render_template("home.html", OUTPUT="")


def CheckInternetConnection(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


if __name__ == '__main__':
    INTERNETCONNECTION = CheckInternetConnection()
    app.run(debug=True)
