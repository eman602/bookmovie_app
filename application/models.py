from application import db
from sqlalchemy.orm import relationship

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(30), nullable=False)
    author_name = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(100), nullable=False, unique=False)
    short_content = db.Column(db.String(500), nullable=False, unique=False)
    child=relationship("Movies", uselist=False, back_populates="parent")

    def __repr__(self):
        return ''.join([
            'User: ', self.book_name, ' ', self.author_name, '\r\n',
            'Title: ', self.genre, '\r\n', self.short_content
            ])


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(30), nullable=False)
    director_name = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(100), nullable=False, unique=False)
    short_content = db.Column(db.String(500), nullable=False, unique=False)
    book_id=db.Column(db.Integer, db.ForeignKey('books.id'))
    parent=relationship("Books", back_populates="child", cascade="all,delete")
    def __repr__(self):
        return ''.join([
            'User: ', self.movie_name, ' ', self.director_name, '\r\n',
            'Title: ', self.genre, '\r\n', self.short_content
            ])