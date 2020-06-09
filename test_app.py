import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import APP
from models import Movie, Actor, db

TOKEN_PRODUCER = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViOWQyNjYxNGEwYmU0YjQwNGFhIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTkxNzExODg5LCJleHAiOjE1OTE3OTgyODksImF6cCI6Ikk1Z1VlNExmb1FZNTNhS0RmWVdjelRPVG91MXYzb0FkIiwiZ3R5IjoicGFzc3dvcmQiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.va1mhqh4gClNH-1QIa4hb5-XH1_OgI-i30sBOpP_trhu-fwzo4FFIr_2Xgt-Z_SQS6YgYmqu3vaYvMg3l6hDx3nRsBlme5ibE5aboFfJ-oiVJxXczFXDJdrdZT9myM9suES6McFB306fnr7o75fxPhz_LlMJd-7p0B752s50XqjG4lFc3JalR6FuF0-wcmZOEAPcUKVESvvIviNHpwUccmwwXl6s3rvT2bRcldSYugyQXLH_BVBAK0zqh_YVQ36Qz09_e_fqyJDl_DAQlAGkEntkhrd3uD9iG5MA5RWQvnLK1ojaztddQE6w68i3kLaEI6u3elF_VyMzfqs1eQFsOQ'
TOKEN_ASSISTANT = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViZjg0MjRlZDQwYmVlMzZjZjhhIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTkxNzExNjk3LCJleHAiOjE1OTE3OTgwOTcsImF6cCI6Ikk1Z1VlNExmb1FZNTNhS0RmWVdjelRPVG91MXYzb0FkIiwiZ3R5IjoicGFzc3dvcmQiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.eZIErm0_qURCx0qDWobJZF8pv5FC5XDaB8g1Ug45hFjGxV-4YGbbWsvb_TyLNSzhK6vz3O0HEH7nDWNr8f6MHggwJldx5khsdAlTEeTQ-_kmVG6a4DFZ1dcDCwXEsO03sgMGfRPsBGsXWOQbfk7EUvLG_w2pMYy173wynuY1O23rpZENkMwa_m5nXqgbz69cjVpjrOruAGrotx55GlhXOQy-hZOqtMCdRRHr7P0kL1JmTA7Xfh4bcurcaEso78mLN4aPUmK9XXIxf0oy1HVC8XUehg_gZNbftw5w62eWPpAE6g_OUAc5ZAsa8kcBE_1TcEcJzQu23bRfWEKEuMjrgg'
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