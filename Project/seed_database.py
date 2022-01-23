"""Script to seed database."""

import os
import json
from random import choice
from datetime import datetime

import crud
import model
import server

os.system("dropdb market")
os.system('createdb market')


model.connect_to_db(server.app)
model.db.create_all()


# Load movie data from JSON file
stock_data = open('data/Sample_stocks.txt')

# Create movies, store them in list so we can use them
# to create fake ratings later
stocks_in_db = []
for line in stock_data:
    line = line.rstrip()
    data = line.split(',')

    symbol, company = (
        data[0],
        data[1]
    )
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    # title, overview, poster_path = (
    #     movie["title"],
    #     movie["overview"],
    #     movie["poster_path"],
    # )
    # release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")


    db_stock = crud.create_stock(symbol, company)
    stocks_in_db.append(db_stock)

model.db.session.add_all(stocks_in_db)
model.db.session.commit()


for n in range(5):
    first_name = f'John{n}'
    last_name = f'Doe{n}'
    email = f'user{n}@test.com'
    password = 'test'

#create a user
    user = crud.create_user(first_name, last_name, email, password)
    model.db.session.add(user)

    # save 10 stocks for the user
    for _ in range (10):
        random_stock = choice(stocks_in_db)
        date_saved = datetime
        user_stock = crud.create_user_stock(user, random_stock, date_saved)
        model.db.session.add(user_stock)

model.db.session.commit()