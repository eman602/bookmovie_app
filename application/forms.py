from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Optional

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

    book_id = IntegerField('Book ID if movie is based on a book!',
        validators=[Optional()]
       
    )

    submit = SubmitField('Submit')


class BookUpdate(FlaskForm):
    search_book=StringField("Book name",
        validators =[
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )

    submit = SubmitField('Search')






















