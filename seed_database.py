"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    format = "%Y-%m-%d"
    title, overview, poster_path, release_date, location = (
        movie["title"], 
        movie["overview"],
        movie["poster_path"],
        datetime.strptime(movie["release_date"],format),
        movie["location"])
        #movie["genre"],
        #movie["director"],
        #movie["writer"],
        #movie["actor"])
                                                  
    print("*"*10)
    print(title)
    print("*"*10)

    db_movie = crud.create_movie(title, overview, release_date, poster_path, location)

    # movie_to_add = crud.create_movie(title,
    #                                  overview,
    #                                  release_date, 
    #                                  poster_path,
    #                                  location)
                                     #genre,
                                     #director,
                                     #writer,
                                     #actor)
    
    # movies_in_db.append(movie_to_add)

    movies_in_db.append(db_movie)
    
    
# for n in range(10):
#     fname = f'firstname{n}'
#     lname = f'lastname{n}'
#     email = f'user{n}@test.com'
#     password = 'test'

# user = crud.create_user(fname, lname, email, password)

# for _ in range(10):
#     random_movie = choice(movies_in_db)