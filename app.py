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

app = Flask(__name__)
setup_db(app)
CORS(app)
cors = CORS(app, resource={r"/*": {"origins": "*"}})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,PUT,DELETE,OPTIONS')
    # header('Access-Control-Allow-Origin: *')
    return response
'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)

#db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /actors
'''
@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def get_actors(token):
  try:
    all_actors = Actor.query.all()

    if len(actors) == 0:
      abort(404)

    formatted_actors = [actor.format() for actor in all_actors]
    return jsonify({
      'actors': formatted_actors,
      'success': True
    }), 200

  except Exception:
    abort(422)

@app.route('/movies', methods=['GET'])
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

@app.route('/actors/<id>', methods=['PATCH'])
@requires_auth('patch:actor')
def update_actor(token, id):
    body = request.get_json()
    actor = Actor.query.get(id)

    if body == None:
      abort(404)

    if actor == None:
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


@app.route('/movies/<id>', methods=['PATCH'])
@requires_auth('patch:movie')
def update_movie(token, id):
  body = request.get_json()
  movie = Movie.query.get(id)

  if body == None:
      abort(404)

  if movie == None:
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

@app.route('/actors', methods=['POST'])
@requires_auth('post:actor')
def add_actor(token):
  body = request.get_json()

  if body == None:
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


@app.route('/actors/<id>', methods=['DELETE'])
@requires_auth('delete:actor')
def delete_actor(token, id):
  actor = Actor.query.get(id)

  if actor == None:
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

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def notfound(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "not found"
    }), 404


@app.errorhandler(AuthError)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "unauthorized"
    }), 401

