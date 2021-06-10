"""Server for film finder app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "thisismysecretkey"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View main homepage."""

    return render_template("homepage.html")


@app.route("/signup")
def render_signup():
    """View sign up page."""

    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def form_submission():
    """Grabs form data submitted by user."""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')
    fav_movie = request.form.get('fav_movie')
    pref_genre = request.form.get('pref_genre')
    fav_director = request.form.get('fav_director')
    fav_writer = request.form.get('fav_writer')

    new_user = crud.create_user(fname, lname, email, password, fav_movie, pref_genre, fav_director, fav_writer)

    return redirect("/profile")


@app.route("/login")
def login():
    """View log-in page."""

    return render_template("login.html")


@app.route("/profile")
def display_profile():
    """Shows a profile page to the user."""

    return render_template("profile.html")


@app.route("/profile", methods=["POST"])
def get_login():
    """Grabs the login info from user submission of login form."""

    email = request.form.get("email")

    password = request.form.get("password")

    return redirect("/profile")


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
