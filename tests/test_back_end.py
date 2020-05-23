import unittest

from flask import url_for
from flask_testing import TestCase
from flask_wtf import FlaskForm
from application import app, db, forms
from application.models import Movies, Books
from application.forms import BookForm, MovieForm, BookDelete, MovieDelete, BookUpdate2
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test Books
        
        booke = Books(book_name="test", author_name="emmanuel", genre="history", short_content="testing project")

        # create test for Movies
       
        moviese = Movies(movie_name="test2", director_name="emmanuel2", genre="action", short_content="testing project again")

        # save users to database
        db.session.add(booke)
        db.session.add(moviese)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)



    def test_bookpage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('book'))
        self.assertEqual(response.status_code, 200)

    def test_movepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('movie'))
        self.assertEqual(response.status_code, 200)

    def test_postpage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('post'))
        self.assertEqual(response.status_code, 200)

    def test_dostpage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('dost'))
        self.assertEqual(response.status_code, 200)

    #def test_addingupdatespage_view(self):
      #  """
       # Test that homepage is accessible without login
        #"""
        #response = self.client.get(url_for('addingupdates'))
        #self.assertEqual(response.status_code, 200)

    def test_Movie_deletepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('Movie_delete'))
        self.assertEqual(response.status_code, 200)

    
    def testbook_deletepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('book_delete'))
        self.assertEqual(response.status_code, 200)

    def testbook_updatepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code, 200)



class TestPosts(TestBase):
    def test_add_new_book(self):
        
        with self.client:
            response = self.client.post(
                url_for('post'),
                data=dict(
                    book_name ="mytest",
                    author_name ="emmanuel",
                    genre = "history",
                    short_content = "describing here"
                ),
                follow_redirects = True
            )
    
            self.assertIn(b'mytest', response.data)

    
    def test_add_new_movie(self):
        
        with self.client:
            response = self.client.post(
                url_for('dost'),
                data=dict(
                    movie_name ="mytest",
                    director_name ="emmanuel",
                    genre = "history",
                    short_content = "describing here"
                ),
                follow_redirects = True
            )
    
            self.assertIn(b'mytest', response.data)

    def test_update_new_book(self):
        
        with self.client:
            response = self.client.post(
                url_for('update'),
                data=dict(
                    book_name ="test",
                    author_name ="daniel",
                    genre = "history",
                    short_content = "describing here"
                ),
                follow_redirects = True
            )
    
            self.assertIn(b'daniel', response.data)

    def test_add_new_movie_relationship(self):
        
        with self.client:
            response = self.client.post(
                url_for('dost'),
                data=dict(
                    movie_name ="mytest",
                    director_name ="emmanuel",
                    genre = "history",
                    short_content = "describing here",
                    book_id=1
                ),
                follow_redirects = True
            )
    
            self.assertIn(b'mytest', response.data)

    def test_delete_a_book(self):
        
        with self.client:
            response = self.client.post(
                url_for('book_delete'),
                data=dict(
                    search_book ="tejkkst"
                    
                ),
                follow_redirects = False
            )
            self.assertIn(b'tejkkst', response.data)
    
    def test_homepage(self):
        response = self.client.post(
            url_for('home')
        )
        self.assertNotIn(b'book name', response.data)

    def test_bookprint_homepage(self):
        booke = Books(book_name="test", author_name="emmanuel", genre="history", short_content="testing project")
        print(repr(booke))

    def test_movieprint_homepage(self):
        moviese = Movies(movie_name="test2", director_name="emmanuel2", genre="action", short_content="testing project again")
        return repr(moviese)



    def test_invalid_update_func(self):
        response = self.client.post(
            url_for('update'),
            data=dict(
                author_name="hello"
            ),
            follow_redirects=False
        )
        self.assertIn(b'hello', response.data)

    def test_invalid_book_delete(self):
        response = self.client.post(
            url_for('book_delete'),
            data=dict(
                search_book="hello"
            ),
            follow_redirects=False
        )
        self.assertIn(b'hello', response.data)

    def test_valid_book_delete(self):
        response = self.client.post(
            url_for('book_delete'),
            data=dict(
                search_book="test"
            ),
            follow_redirects=True
        )
        self.assertNotIn(b'test', response.data)

    def test_valid_movie_delete(self):
        response = self.client.post(
            url_for('Movie_delete'),
            data=dict(
                search_movie="test2"
            ),
            follow_redirects=True
        )
        self.assertNotIn(b'test2', response.data)


    def test_delete_no_input(self):
        response = self.client.post(
            url_for('update'),
            data=dict(
                book_name="thetest"
            ),
        follow_redirects=False
        )
        self.assertIn(b'thetest', response.data)

    def test_error_page(self):
        response = self.client.post(
            url_for('Movie_delete')
            
        )
        self.assertRaises(Exception, response.data)
       