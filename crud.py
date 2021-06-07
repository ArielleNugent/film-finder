"""CRUD operations."""
from model import db, Movie, User, Preference, Location, User_Preference, User_Movie, Movie_Location, User_Location, connect_to_db
    
def create_user(fname, lname, email, password):
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


def get_user_by_name(fname):
    """Returns a user by their first name."""

    return User.query.get(fname, lname)


def get_user_by_name(lname):
    """Returns a user by their first name."""

    return User.query.get(lname)


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title,
                    overview=overview,
                    release_date=release_date,
                    poster_path=poster_path)
                    # genre=genre,
                    # director=director,
                    # writer=writer,
                    # actor=actor)
    #release_date in format: YYYY-MM-DD
    #poster_path=image

    db.session.add(movie)
    db.session.commit()

    return movie


def get_movies():
    """Returns all movies."""

    return Movie.query.all()


def get_movie_by_id(movie_id):
    """Returns a movie by id(primary key)."""

    return Movie.query.get(movie_id)   


def get_movie_by_title(title):
    """Returns a movie by title."""

    return Movie.query.get(title)    


def get_movie_by_release_date(release_date):
    """Returns a movie by release date."""

    return Movie.query.get(release_date)     


if __name__ == '__main__':
    from server import app
    connect_to_db(app)