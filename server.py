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

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")
    fav_movie = request.form.get("fav_movie")
    pref_genre = request.form.get("pref_genre")
    fav_director = request.form.get("fav_director")
    fav_writer = request.form.get("fav_writer")

    new_user = crud.create_user(fname, lname, email, password)

    return redirect("/profile")


@app.route("/login")
def login():
    """View log-in page."""

    return render_template("login.html")


###NEWLY ADDED###
# @app.route("/handle-login", methods=["POST"])
# def handle_login():
#     "Logs user into app."

#     email = request.form["email"]
#     password = request.form["password"]

#     if password ...
#         session["current_user"] = email
#         flash(f"Logged in as {email}"))
#         return redirect ("/")

#     else:
#         flash(f"Incorrect email and password combination entered. 
#         Please try again.")
#         return redirect("/login")
###CHECK THIS###



# create another /login route with POST methods activated 
# once the user logs in, a session should be created
# use a post request to grab the user logging in's email 
    # check that the email/password match what's in your db by query
        # user = User.query.filter_by(email=user_email).first()
        # if user (meaning that if a user is returned then you can verify its accurate)
    # if it's valid -> create the session
# session['user_id'] = user.user_id


@app.route("/profile")
def display_profile():
    """Shows a profile page to the user."""

    return render_template("profile.html")


@app.route("/login", methods=["POST"])
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


@app.route("/netflix")
def get_netflix_movies():
    """View all movies on Netflix."""

    movies = crud.get_movies_on_netflix()

    return render_template("all_movies.html", movies=movies)


@app.route("/hulu")
def get_hulu_movies():
    """View all movies on Hulu."""

    movies = crud.get_movies_on_hulu()

    return render_template("all_movies.html", movies=movies)


@app.route("/amazon")
def get_amazon_movies():
    """View all movies on Amazon."""

    movies = crud.get_movies_on_amazon()

    return render_template("all_movies.html", movies=movies)


@app.route("/disney")
def get_disney_movies():
    """View all movies on Disney."""

    movies = crud.get_movies_on_disney()

    return render_template("all_movies.html", movies=movies)


@app.route("/hbo")
def get_hbo_movies():
    """View all movies on HBO."""

    movies = crud.get_movies_on_hbo()

    return render_template("all_movies.html", movies=movies)


# step 1: add location to movies #DONE
# step 2: seed "movies" database with movies.json
# step 3: populate the page with the movies in your database 
 
# BUTTONS AT THE TOP OF THE /MOVIES PAGE: netflix hulu amazon disney hbo
# need a movies route with get request capabilites 
# user clicks "netflix" button, this route will be called through js
# @app.route("/movies/netflix.json") 
# def get_netflix_movies():
#    """Returns json of all movies found on netflix""""
#   ## in crud.py make functions that get movies based on location
#   data = {}
#   netflix_movies = crud.get_movie_by_loc("netflix") => [<Movie id=92> , <Movie id=24>, <Movie id=76> ]
        # Movies.query.filter_by(loc=loc).all()
#   we're going to want to create a dictionary  of the information that JS  needs (which is everything)
#   for movie in netflix_movies:
#       data[movie.title] = [movie.overview, movie.release_date, movie.poster_path]
#      >> data => {"Die Hard": ["Bruce Willis almost dies on xmas", 2002-08-19, "https://diehard.com"],
 #               "Scooby Doo": ["Great Dane and friend do things", 2008-07-05]}
#   return jsonify(data)
# 


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
    connect_to_db(app)
    app.run(debug=True,
            host='0.0.0.0')
