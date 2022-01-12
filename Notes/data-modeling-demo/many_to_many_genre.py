"""Example of SQLAlchemy Many-To-Many."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


class Book(db.Model):
    """Book."""

    __tablename__ = "books"

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

    genres = db.relationship("Genre", secondary="books_genres", backref="books")
    # !end Book attributes

    def __repr__(self):
        return f"<Book title={self.title}>"


class Genre(db.Model):
    """Genre of book."""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(50), unique=True)
    # !end Genre attributes

    def __repr__(self):
        return f"<Genre id={self.genre_id} {self.genre}>"


class BookGenre(db.Model):
    """Genre of a specific book."""

    __tablename__ = "books_genres"

    book_genre_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.genre_id"), nullable=False)
    # !end BookGenre attributes

    def __repr__(self):
        return f"<BookGenre book_id={self.book_id} genre_id={self.genre_id}>"


def connect_to_db(app):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///many-to-many-genre"

    # this would output the raw SQL, currently off as it can be noisy
    # app.config["SQLALCHEMY_ECHO"] = True

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    import os

    os.system("dropdb many-to-many-genre --if-exists")
    os.system("createdb many-to-many-genre")

    connect_to_db(app)

    # Make our tables
    db.create_all()

    # Add books and genres
    hamlet = Book(title="Hamlet")
    hobbit = Book(title="The Hobbit")
    fantasy = Genre(genre="Fantasy")
    theater = Genre(genre="Theater")

    # Can add using relationships
    hamlet.genres.append(fantasy)
    theater.books.append(hamlet)
    fantasy.books.append(hobbit)

    # Can also create a BookGenre and pass it an existing book id and genre id
    # but this is a lot clunkier

    # Add the two Books
    # Genres will be added automatically by SQLAlchemy because of their relationships
    db.session.add(hamlet)
    db.session.add(hobbit)
    db.session.commit()

    # Test that this worked
    print(BookGenre.query.all())
    number_bookgenres = BookGenre.query.count()
    assert number_bookgenres == 3
