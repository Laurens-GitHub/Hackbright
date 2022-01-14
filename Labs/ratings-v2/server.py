"""Server for movie ratings app."""

from flask import Flask

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import db, connect_to_db, Movie
import crud

from jinja2 import StrictUndefined
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
# Replace this with routes and view functions!

#Create Homepage
@app.route("/")
def homepage():
    """Show the Homepage"""
    return render_template("homepage.html")

@app.route("/movies")
def all_movies():
    """Show a list of all movies"""

    all_movies = crud.get_movies()

    return render_template("all_movies.html", movies=all_movies)

@app.route("/movies/<movie_id>")
def movie_details(movie_id):
    """Show the details of one movie"""

    movie_details = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie_details)


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")

@app.route("/users", methods=["POST"])
def login_user(user_id):
    """Log in a returning user."""

    # get the user's entered email and password from the form
    email = request.form.get("email")
    password = request.form.get("password")

    #Query the database for the entered email, and get the associated password
    user_pass = crud.get_user_by_password(email)
    #If the password in the form matches the queried password, log the user in
    if password == user_pass:
        name = crud.get_user_by_id(user_id)
        session['user_id'] = user_id
    #Flash a logged in message and redirect to the homepage
        flash("Log In Successful!")
        return redirect("/")

    #Otherwise, flash a message that the account information is incorrect
    else:
        flash("The account information is incorrect")


@app.route("/users")
def all_users():
    """Show a list of all users"""

    all_users = crud.get_users()

    return render_template("all_users.html", users=all_users)


@app.route("/users/<user_id>")
def user_details(user_id):
    """Show the details of one user"""

    user_details = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user_details)



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
