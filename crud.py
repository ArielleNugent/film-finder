"""CRUD operations."""
from model import db, Movie, User, Preference, Location, User_Preference, User_Movie, Movie_Location, User_Location, connect_to_db
    
# from server import app

def create_user(fname, lname, email, password, fav_movie=None, pref_genre=None, fav_director=None, fav_writer=None):
    """Create and return a new user."""

    user = User(fname=fname, 
                lname=lname, 
                email=email, 
                password=password)


    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Returns all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Returns a user by their id(primary key)."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Returns a user by email."""

    return User.query.filter(User.email == email).first()


def get_user_by_full_name(fname, lname):
    """Returns a user by their full name(first name & last name)."""

    return User.query.get(fname, lname)


def get_user_by_fname(fname):
    """Returns a user by their first name."""

    return User.query.get(fname, lname)


def get_user_by_lname(lname):
    """Returns a user by their first name."""

    return User.query.get(lname)


def create_movie(title, overview, release_date, poster_path, location):
    """Create and return a new movie."""

    # with app.app_context():

    movie = Movie(title=title,
                    overview=overview,
                    release_date=release_date,
                    poster_path=poster_path,
                    location=location)
                    # genre=genre,
                    # director=director,
                    # writer=writer,
                    # actor=actor)
    #release_date in format: YYYY-MM-DD
    #poster_path=image

    # print("********************************************")
    # print(movie)

    db.session.add(movie)
    db.session.commit()

    return movie


def get_movies():
    """Returns all movies."""

    return Movie.query.all()


def get_movies_on_netflix():
    """Returns movies on Netflix."""

    return Movie.query.filter_by(location="Netflix").all()


def get_movies_on_hulu():
    """Returns movies on Hulu."""

    return Movie.query.filter_by(location="Hulu").all()


def get_movies_on_amazon():
    """Returns movies on Amazon."""

    return Movie.query.filter_by(location="Amazon").all()


def get_movies_on_disney():
    """Returns movies on Disney."""

    return Movie.query.filter_by(location="Disney").all()


def get_movies_on_hbo():
    """Returns movies on HBO."""

    return Movie.query.filter_by(location="HBO").all()


def get_movie_by_id(movie_id):
    """Returns a movie by id(primary key)."""

    return Movie.query.get(movie_id)   


def get_movie_by_title(title):
    """Returns a movie by title."""

    return Movie.query.get(title)    


def get_movie_by_release_date(release_date):
    """Returns a movie by release date."""

    return Movie.query.get(release_date)     


# def create_rating(user, movie, score):
#     """Create and return a new rating."""

#     rating = Rating(user=user, movie=movie, score=score)

#     db.session.add(rating)
#     db.session.commit()

#     return rating


# if __name__ == '__main__':
#     from server import app
#     connect_to_db(app)