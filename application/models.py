from application import db

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(30), nullable=False)
    author_name = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(100), nullable=False, unique=True)
    short_content = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'User: ', self.book_name, ' ', self.author_name, '\r\n',
            'Title: ', self.genre, '\r\n', self.short_content
            ])


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(30), nullable=False)
    director_name = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(100), nullable=False, unique=True)
    short_content = db.Column(db.String(500), nullable=False, unique=True)
    
    def __repr__(self):
        return ''.join([
            'User: ', self.movie_name, ' ', self.director_name, '\r\n',
            'Title: ', self.genre, '\r\n', self.short_content
            ])








