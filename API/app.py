import urllib
import urllib.request
from flask import render_template, jsonify, Flask
from API.Base_API import BaseAPI
from API.offline_Data import OfflineData
from API.InternetConnection import Connection

# Global variable
INTERNETCONNECTION = False
FilePath = "offline_data/countriesData.json"
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/<countryName>/<category>/")
def outputPage(countryName, category):
    if INTERNETCONNECTION:
        baseAPI = BaseAPI()
        countryInfo = baseAPI.get_country_info(str(countryName), category)
    else:
        offData = OfflineData(FilePath)
        offData.OpenFile()
        offData.LoadFile()
        offData.CloseFile()
        countryInfo = offData.GetData(countryName, category)

    if countryInfo is None:
        countryInfo = "Not Found"

    return jsonify(countryInfo)


@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")


if __name__ == '__main__':
    INTERNETCONNECTION = Connection.CheckInternetConnection()
    print(INTERNETCONNECTION)
    app.run(debug=True)
