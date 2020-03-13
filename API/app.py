import flask
import requests
import json

# Global Variables
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
api_url_base = 'https://restcountries.eu/rest/v2/'


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/', methods=['GET'])
def home():
    info = get_country_info()
    if info is not None:
        return jsonify(info)
    else:
        return page_not_found


def get_country_info():
    api_url = api_url_base + 'name/egypt'
    response = requests.get(api_url)

    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return None


if __name__ == '__main__':
    app.run()
