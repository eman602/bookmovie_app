from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class BookForm(FlaskForm):
    book_name = StringField('Book Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    author_name = StringField('Authors Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    genre = StringField('Genre',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    short_content = StringField('Description',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
    submit = SubmitField('Submit')


class MovieForm(FlaskForm):
    movie_name = StringField('Movie Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    director_name = StringField('Directors Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    genre = StringField('Genre',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    short_content = StringField('Description',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
    submit = SubmitField('Submit')




