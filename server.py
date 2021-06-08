"""Server for movie finder app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

app = Flask(__name__)


@app.route("/")
def homepage():
    """View main homepage."""

    return render_template("homepage.html")


@app.route("/sign_up")
def sign_up():
    """View sign up page."""

    return render_template("sign_up.html")


@app.route("/login")
def login():
    """View log-in page."""

    return render_template("login.html")


@app.route("/movies")
def all_movies():
    """View all of the movies."""

    movies = crud.get_movies()

    return render_template("all_movies.html", movies=movies)


@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show complete details of a particular movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)


@app.route("/users")
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template("all_users.html", users=users)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
