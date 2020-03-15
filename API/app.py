import flask
from flask import jsonify, render_template, request, url_for
from werkzeug.utils import redirect
from API.Base_API import BaseAPI
from API.DataHandler import DataHandler

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/', methods=["POST", "GET"])
def home(output=""):
    if request.method == "POST":
        category = request.form.get("CategoryMenu")
        country = request.form.get("CountryMenu")
        try:
            baseAPI = BaseAPI()
        except:
            print("Error")

        countryInfo = baseAPI.get_country_info(country)

        if countryInfo is not None:
            output = countryInfo[0]
        else:
            output = ""
        screenData = output[str(category)]

        return render_template("home.html", OUTPUT=screenData)
    else:
        return render_template("home.html", OUTPUT="")


if __name__ == '__main__':
    app.run(debug=True)
