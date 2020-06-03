import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
#from . import models
#from .models import db, setup_db, Actor, Movie
from models import db, setup_db, Actor, Movie
from flask_cors import CORS
from flask import Flask, session, redirect
from flask_session import Session

#from .auth import AuthError, requires_auth
from auth import AuthError, requires_auth

AUTH0_DOMAIN = 'fsnd-sami.auth0.com'

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    cors = CORS(app, resource={r"/*": {"origins": "*"}})

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)

@APP.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PATCH,POST,PUT,DELETE,OPTIONS')
    # header('Access-Control-Allow-Origin: *')
    return response
'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''

#db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /actors
'''

#token='bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQxOTczOTI3Mzc2ODI0MDk1NTQiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE1OTExOTkyOTUsImV4cCI6MTU5MTIwNjQ5NSwiYXpwIjoiSTVnVWU0TGZvUVk1M2FLRGZZV2N6VE9Ub3UxdjNvQWQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.nlQWzoKNVOTk5p9C6Z8oxZ8rJqxxuCjoZYG-kF4bTpRNT1mOYTEWbtLwm5Am9YEOcH-cRLEe4-m423F8FQTOmXbRkIY47WWVZgsYwhxCG2zOEjmJykp8SDz3eHGxcFqqqeqRfbMUeWUAcue9zKKYMEBnMAuZpbMCc6tPdJ12NS378nxQyZqqtg2kWldyZZjT2QEDX_KaufgJhQ9FDcKhH09d5WyJkj3S3nOkPXpj7uHk7z1fcWJalH--Ip7RlwT4UmEUKsjPJ1x6uOwiisVOf_1ySzcLWPl1BZaZCOdfGZbdMvm6sWRT3RqQ9uBfv1D03wP2wRZQB2khd4bjN1apCQ&scope=&expires_in=7200&token_type=Bearer&state=g6Fo2SBmRXdSLWpDSzhmRVZzTGRWV3NMbzk0RzZBcklUQ1MzdKN0aWTZIE9meGhRc0FCb01DM1dWc29XTEhqak01TWljcVd1NnFao2NpZNkgSTVnVWU0TGZvUVk1M2FLRGZZV2N6VE9Ub3UxdjNvQWQ'

@APP.route('/actors')
@requires_auth('get:actors')
def get_actors(token):
  try:
    all_actors = Actor.query.all()

    if len(all_actors) == 0:
      abort(404)
    
    print (all_actors)

    formatted_actors = [actor.format() for actor in all_actors]
    return jsonify({
      'actors': formatted_actors,
      'success': True
    }), 200

  except Exception:
    abort(422)

@APP.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def get_movies(token):
  try:
    movies = Movie.query.all()

    if len(movies) == 0:
      abort(404)

    formatted_movies = [movie.format() for movie in movies]
    return jsonify({
      'movies': formatted_movies,
      'success': True
    }), 200

  except Exception:
    abort(422)

@APP.route('/actors/<id>', methods=['PATCH'])
@requires_auth('patch:actor')
def update_actor(token, id):
    body = request.get_json()
    actor = Actor.query.get(id)

    if body is None:
      abort(404)

    if actor is None:
        abort(404)

    try:
      if 'name' in body:
        actor.name = body['name']
     
      if 'age' in body:
        actor.age = body['age']

      if 'gender' in body:
        actor.gender = body['gender']

      db.session.commit()

    except:
      db.session.rollback()
      abort(422)

    finally:
      db.session.close()

    return jsonify({
      'success': True
    }), 200


@APP.route('/movies/<id>', methods=['PATCH'])
@requires_auth('patch:movie')
def update_movie(token, id):
    body = request.get_json()
    movie = Movie.query.get(id)

    if body is None:
      abort(404)

    if movie is None:
      abort(404)

    try:
      if 'title' in body:
        movie.title = body['title']

      if 'release_date' in body:
        movie.release_date = body['release_date']

      db.session.commit()

    except:
      db.session.rollback()
      abort(422)

    finally:
      db.session.close()

    return jsonify({
      'success': True
    }), 200

@APP.route('/actors', methods=['POST'])
@requires_auth('post:actor')
def add_actor(token):
    body = request.get_json()

    if body is None:
      abort(404)

    name = body['name']
    age = body['age']
    gender = body['gender']
  
    try:
      new_actor = Actor(name=name, age=age, gender=gender)
      db.session.add(new_actor)
      db.session.commit()
      new_id = new_actor.id

    except:
      db.session.rollback()
      abort(422)

    finally:
      db.session.close()

    return jsonify({
      'id': new_id,
      'success': True
    }), 201


@APP.route('/actors/<id>', methods=['DELETE'])
@requires_auth('delete:actor')
def delete_actor(token, id):
    actor = Actor.query.get(id)

    if actor is None:
      abort(404)

    try:
      db.session.delete(actor)
      db.session.commit()

    except:
      db.session.rollback()
      abort(422)

    finally:
      db.session.close()

    return jsonify({
      'success': True
    }), 200

# Error Handling


@APP.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@APP.errorhandler(404)
def notfound(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "not found"
    }), 404


@APP.errorhandler(AuthError)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "unauthorized"
    }), 401
