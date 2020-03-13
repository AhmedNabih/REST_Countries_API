import flask
from flask import jsonify, render_template

# Global Variables
from API.Base_API import BaseAPI

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
