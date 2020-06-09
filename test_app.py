import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import APP
from models import Movie, Actor, db

TOKEN_PRODUCER = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViOWQyNjYxNGEwYmU0YjQwNGFhIiwiYXVkIjoiY2FzcHRvbmUiLCJpYXQiOjE1OTE3MjMwMzMsImV4cCI6MTU5MTgwOTQzMywiYXpwIjoibHlDWExNb3hVWUxCeVFXNFVXOE0zMUl0UUVqTmFHclIiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.nW4ArExMJkwfTOgCsnNcDav1kGPOhcGtk0FXY55cJdwXSTU6vYhOGhxQPSiS701Uf9s5MFWLo5HiwYGOvUUEROdk2zWG1JvfiriuSBItZtWEOAzra6UAKRzvOW-OB98mBAHe_SNJFAfX3fhcaAxZZdlEyM-b8DFRFwzSFfkqhfH97wZFmC5EE3x36XJ6vDvTvQQw2c9FILX_fKxWFh9iIvtM148yKSO2Bh1rIMq6XMW67b5E4qk-xsXQVYxSlD3YkdUxRVID9hzfytVNTk6XdXYsr67rOIfDJMFdmpV9cr_097iCQLVPwhxlqYNcakYiYppx-VECU_pA82H9s-Qzgg'
TOKEN_ASSISTANT = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViZjg0MjRlZDQwYmVlMzZjZjhhIiwiYXVkIjoiY2FzcHRvbmUiLCJpYXQiOjE1OTE3MjI5NjQsImV4cCI6MTU5MTgwOTM2NCwiYXpwIjoibHlDWExNb3hVWUxCeVFXNFVXOE0zMUl0UUVqTmFHclIiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.jRpdT8JrsiDjcYs0mBEBu1Za-IoSc_Qx2q_o1MmdwGA6yx6dMEy9z-EA8Gbp0QXzeyUKOu4AUKwDf2PE7jJP6eJU4N6FYDGMCxaH_E05ILrKufEYiy1ANpMF8_98AWD7jQZpeHCmtzqumtA2mxaZaUgkn-uBmTkd33vlnKyqvq_X81Lf9mzR7cUqX_eKS5sHU5izFHcihCBOKZBlciF-gG0UJFhJO5bfj8FI_cB9innBpmDsG8gzzOjUetdBIpXgMem0lPJNmYs2xRF2rPyYZMiGqv6xn99PCJQd8WPolOwGCiclJ-zZXH4VHHgTJ524qaTsirzY4SEeHLMnUqRMBw'
default_path='postgresql://postgres:1234@localhost:5432/casting_test'

database_path=os.getenv('DATABASE_URL', default_path)

class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.database_path = "postgres://postgres:1234@{}/{}".format('localhost:5432', self.database_name)
        #setup_db(self.app, self.database_path)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = self.database_path
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        self.movie = {
            'title': 'Sicario 2',
            'release_date': '2017'
        }

        self.new_movie = {
            'title': 'Guardians of the Galaxy',
            'release_date': '2014'
        }

        self.actor = {
            'name': 'Anne hathaway',
            'age': '38',
            'gender': 'Female'
        }

        self.new_actor = {
            'name': 'Matt Deamon',
            'age': '49',
            'gender': 'Male'
        }


        # binds the app to the current context
        with self.app.app_context():
            self.db = db
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    #def tearDown(self):
    #    """Executed after reach test"""
    #    self.db.drop_all()
    #    pass

    # Test GET Actors
    def test_get_actors_public(self):
        res = self.client().get('/actors')

        self.assertEqual(res.status_code, 401)

    def test_get_actors_executive_producer(self):
        res = self.client().get('/actors', headers={
                        'Authorization': TOKEN_PRODUCER}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['actors']))

    def test_get_actors_assistant(self):
        res = self.client().get('/actors', headers={
                        'Authorization': TOKEN_ASSISTANT}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['actors']))



    # Test GET Movies
    def test_get_movies_public(self):
        res = self.client().get('/movies')

        self.assertEqual(res.status_code, 401)

    def test_get_movies_executive_producer(self):
        res = self.client().get('/movies', headers={
           'Authorization': TOKEN_PRODUCER}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['movies']))

    def test_get_movies_assistant(self):
        res = self.client().get('/movies', headers={
           'Authorization': TOKEN_ASSISTANT}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['movies']))

    # Test POST Actor
    def test_post_actors_public(self):
        res = self.client().post('/actors/add', json=self.new_actor)

        self.assertEqual(res.status_code, 401)

    def test_post_actors_executive_producer(self):
        #original_count = len(Actor.query.all())

        res = self.client().post('/actors/add', json=self.new_actor, headers={
            'Authorization': TOKEN_PRODUCER}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
#        self.assertGreater(len(Actor.query.all()), original_count)
        self.assertGreater(data['id'], 0)

    def test_post_actors_assistant(self):
        #original_count = len(Actor.query.all())

        res = self.client().post('/actors/add', json=self.new_actor, headers={
            'Authorization': TOKEN_ASSISTANT}
        )

        self.assertEqual(res.status_code, 401)
#        self.assertGreater(len(Actor.query.all()), original_count)

    # Test POST Movie
    def test_post_movies_public(self):
        res = self.client().post('/movies/add', json=self.new_movie)

        self.assertEqual(res.status_code, 401)

    def test_post_movies_executive_producer(self):
#        original_count = len(Movie.query.all())

        res = self.client().post('/movies/add', json=self.new_movie, headers={
            'Authorization': TOKEN_PRODUCER}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
#        self.assertGreater(len(Movie.query.all()), original_count)
        self.assertGreater(data['id'], 0)

    # Test PATCH Actor
    def test_patch_actors_public(self):
        res = self.client().patch('/actors/1', json={'age': "43"})

        self.assertEqual(res.status_code, 401)

    def test_patch_actors_executive_producer(self):
        res = self.client().patch('/actors/2', json={'age': "69"}, headers={
            'Authorization': TOKEN_PRODUCER}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actors_assistant(self):
        res = self.client().patch('/actors/2', json={'age': "69"}, headers={
            'Authorization': TOKEN_ASSISTANT}
        )

        self.assertEqual(res.status_code, 401)

    def test_patch_actors_does_not_exist(self):
        res = self.client().patch('/actors/1000', json={'age': "49"}, headers={
            'Authorization': TOKEN_PRODUCER}
        )
        
        self.assertEqual(res.status_code, 404)

    def test_patch_actors_no_data(self):
        res = self.client().patch('/actors/1', headers={
            'Authorization': TOKEN_PRODUCER}
        )
        
        self.assertEqual(res.status_code, 404)

    # Test PATCH Movie
    def test_patch_movies_executive_producer(self):
        res = self.client().patch('/movies/2', json={'title': "Updated Title 2"}, headers={
            'Authorization': TOKEN_PRODUCER}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movies_does_not_exist(self):
        res = self.client().patch('/movies/1000', json={'title': "Updated Title"}, headers={
            'Authorization': TOKEN_PRODUCER}
        )
        
        self.assertEqual(res.status_code, 404)

    def test_patch_movies_no_data(self):
        res = self.client().patch('/movies/2', headers={
            'Authorization': TOKEN_PRODUCER}
        )
        
        self.assertEqual(res.status_code, 404)

    # Test DELETE Actor
    def test_delete_actors_public(self):
        res = self.client().delete('/actors/1')

        self.assertEqual(res.status_code, 401)

    def test_delete_actors_executive_producer(self):
        res = self.client().delete('/actors/1', headers={
            'Authorization': TOKEN_PRODUCER}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actors_assistant(self):
        res = self.client().delete('/actors/1', headers={
            'Authorization': TOKEN_ASSISTANT}
        )

        self.assertEqual(res.status_code, 401)


    def test_delete_actors_does_not_exist(self):
        res = self.client().delete('/actors/1000', headers={
            'Authorization': TOKEN_PRODUCER}
        )
        
        self.assertEqual(res.status_code, 404)

    # Test DELETE Movie
    def test_delete_movies_public(self):
        res = self.client().delete('/movies/1')

        self.assertEqual(res.status_code, 401)

    def test_delete_movies_executive_producer(self):
        res = self.client().delete('/movies/1', headers={
            'Authorization': TOKEN_PRODUCER}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movies_does_not_exist(self):
        res = self.client().delete('/movies/1000', headers={
            'Authorization': TOKEN_PRODUCER}
        )
        
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()