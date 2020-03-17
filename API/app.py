import urllib
import urllib.request
import flask
from flask import render_template, jsonify
from API.Base_API import BaseAPI
from API.offline_Data import OfflineData

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Global variable
INTERNETCONNECTION = False
FilePath = "offline_data/countriesData.json"


@app.route("/<countryName>/<category>/")
def outputPage(countryName, category):
    baseAPI = BaseAPI()

    if INTERNETCONNECTION:
        countryInfo = baseAPI.get_country_info(str(countryName), category)
    else:
        o = OfflineData(FilePath)
        o.OpenFile()
        o.LoadFile()
        o.CloseFile()
        countryInfo = o.GetData(countryName, category)

    try:
        if countryInfo is None:
            countryInfo = "Not Found"
    except:
        countryInfo = "Invalid Input"

    return jsonify(countryInfo)


@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")


def CheckInternetConnection(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


if __name__ == '__main__':
    INTERNETCONNECTION = CheckInternetConnection()
    print(INTERNETCONNECTION)
    app.run(debug=True)
