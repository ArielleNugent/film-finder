"""Server for movie finder app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

app = Flask(__name__)


@app.route("/")
def homepage():
    """View main homepage."""

    return render_template("homepage.html")
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
