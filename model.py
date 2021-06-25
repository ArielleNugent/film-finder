from flask_sqlalchemy import SQLAlchemy
# from DateTime import DateTime

db = SQLAlchemy()


class User(db.Model):
    """Users."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(20))

    def __repr__(self):
        return f'<User user_id={self.user_id} name={self.fname} {self.lname} email={self.email}>'


class Movie(db.Model):
    """Many movies, creates a movie_id, including: title, overview, genre, 
    director, writer, actor, release_date, and poster_path."""

    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String(50))
    overview = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)
    location = db.Column(db.String)
    genre = db.Column(db.String(30),
                        nullable=True)
    director = db.Column(db.String(50),
                        nullable=True)
    writer = db.Column(db.String(50),
                        nullable=True)
    actor = db.Column(db.String(50),
                        nullable=True)

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} title={self.title}>'


class Preference(db.Model):
    """Preferences to choose from--options in the user quiz."""

    __tablename__ = 'preferences'

    preference_id = db.Column(db.Integer,
                                primary_key=True)

    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    genre = db.Column(db.String(30))
    director = db.Column(db.String(50))
    actor = db.Column(db.String(50))

    def __repr__(self):
        return f'<Preference preference_id={self.preference_id}>'


class Location(db.Model):
    """Location/app where the movie lives."""

    __tablename__ = 'locations'
    #loc_id gives us the location as an integer.
    loc_id = db.Column(db.Integer,
                        primary_key=True)
    #location gives us the location as "Netflix", or "Amazon", etc.
    location = db.Column(db.String(30))

    def __repr__(self):
        return f'<Location loc_id={self.loc_id} location={self.location}>'

    
class User_Preference(db.Model):
    """Association table (many-to-many) for a user's preferences.
    Users can have many preferences, and
    preferences can be held to many users."""

    __tablename__ = 'user_preferences' 

    user_preference_id = db.Column(db.Integer,
                            primary_key=True,
                            nullable=False)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)

    preference_id = db.Column(db.Integer,
                                db.ForeignKey('preferences.preference_id'),
                                nullable=False)


class User_Movie(db.Model):
    """Association table (many-to-many) between users and movies.
    Users can follow many movies and 
    each movie can be followed by many users."""

    __tablename__ = 'user_movies'

    user_movie_id = db.Column(db.Integer,
                                primary_key=True,
                                nullable=False)

    movie_id = db.Column(db.Integer,
                        db.ForeignKey('movies.movie_id'),
                        nullable=False)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)


class Movie_Location(db.Model):
    """Association table (many-to-many) between movies and locations.
    Movies can exist in many locations, 
    and each location holds many movies."""

    __tablename__ = 'movie_locations'

    movie_loc_id = db.Column(db.Integer,
                            primary_key=True,
                            nullable=False)

    movie_id = db.Column(db.Integer,
                        db.ForeignKey('movies.movie_id'),
                        nullable=False)

    loc_id = db.Column(db.Integer,
                        db.ForeignKey('locations.loc_id'),
                        nullable=False)


class User_Location(db.Model):
    """Association table (many-to-many) between users and locations.
    Users can watch many locations and 
    each location can have many users watching it."""  

    __tablename__ = 'user_locations'

    user_loc_id = db.Column(db.Integer,
                            primary_key=True,
                            nullable=False)
                        
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)

    loc_id = db.Column(db.Integer,
                        db.ForeignKey('locations.loc_id'),
                        nullable=False)



def connect_to_db(flask_app, db_uri='postgresql:///movies', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)

    # BE SURE TO CREATE ALL TABLES ----> 
    #In this order:
    # python3 -i model.py
    # db.create_all()
    # # test_user = User(email='test@test.test', password='test')
    # # db.session.add(test_user)
    # db.session.commit()