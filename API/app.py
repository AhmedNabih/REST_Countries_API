import flask
from flask import jsonify

# Global Variables
from API.Base_API import BaseAPI

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/', methods=['GET'])
def home():
    baseAPI = BaseAPI()
    try:
        info = baseAPI.get_country_info('name', 'egypt')

        if info is not None:
            return jsonify(info)
        else:
            return page_not_found
    except:
        return page_not_found


if __name__ == '__main__':
    app.run()
