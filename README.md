# Capstone
This is the final project of the Udacity Full Stack Developer Nanodegree course, it combines several skills, including:

* SQL and Data Modeling for the Web
* API Development and Documentation
* Auth0, Identity and Access Management
* Server Deployment, Containerization and Testing using Heorku

## Installing Dependencies
Python 3.7.2
Follow instructions to install the version of python for your platform in the python docs

Virtual Enviornment
It's good practise to work within a virtual environment whenever using Python. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

PIP Dependencies
pip install -r requirements.txt
This will install all of the required packages we selected within the requirements.txt file.

## Key Dependencies
Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

SQLAlchemy is the Python SQL toolkit and ORM.

Flask-CORS is the extension we use to handle cross origin requests from the frontend server.

## Running the server
From within the root directory, each time you open a new terminal session, run:

export FLASK_APP=app.py
To run the server, execute:

flask run --reload
The --reload flag will detect file changes and restart the server automatically.

## Testing
To run the unit tests, execute:
python test_app.py

## Live server can be found on Heroku
URL https://casting-sami.herokuapp.com/
DATABASE_URL: postgres://ljcujrcjekgmuj:cf7a535c6e9517e724f069ca88d01be6f1028ac25c689e853fa01b2df18abc29@ec2-34-195-169-25.compute-1.amazonaws.com:5432/d5nt9hlv1r6cdd

## RESTful APIs Endpoints
GET '/' welcome message
GET '/actors'
GET '/movies'
PATCH '/actors/<id>'
PATCH '/movies/<id>'
POST '/actors/add'
POST '/movies/add'
DELETE '/actors/<id>'
DELETE '/movies/<id>'

### GET /actors
Returns a list of all actors
Requires auth permission (a token) get:actors
Request: None
Response:
{
  "actors": [
    {
      "age": 35,
      "gender": "F",
      "id": 1,
      "name": "Scarlett"
    },
    {
      "age": 60,
      "gender": "M",
      "id": 3,
      "name": "Jhonny Depp"
    },
  ],
  "success": true
}

### GET /movies
Returns a list of all movies
Requires auth permission get:movies
Request: None
Response:
{
  "movies": [
    {
      "id": 1,
      "release_date": "1998",
      "title": "Titanic"
    },
    {
      "id": 2,
      "release_date": "2015",
      "title": "Sicario"
    },
  ],
  "success": true
}

### PATCH /actors/<id>
Updates a selected actor by id
Requires auth permission patch:actor
Request:
{
    "name": "Updated Name",
    "age": 50,
    "gender": "Male"
}
Response:
{
    "success": true
}

### PATCH /movies/<id>
Updates a selected movie by id
Requires auth permission patch:movie
Request:
{
    "title": "Updated Title",
    "release_date": "2018"
}
Response:
{
    "success": true
}

### POST /actors
Adds a new actor
Requires auth permission post:actor
Request:
{
   "name":"Sean Connery",
   "age":"70",
   "gender":"M"
}
Response:
{
  "id": 8,
  "success": true
}
### POST /movies
Adds a new movie
Requires auth permission post:movie
Request:
{
  "title":"Avatar 2",
  "release_date":"2020"
}
Response:
{
  "id": 8,
  "success": true
}
### DELETE /actors/<id>
Deletes an actor by id
Requires auth permission delete:actor
Request: None
Response:
{
    "success": true
}

### DELETE /movies/<id>
Deletes a movie by id
Requires auth permission delete:movie
Request: None
Response:
{
    "success": true
}

## Auth0 configuration settings
AUTH0_DOMAIN = 'fsnd-sami.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'http://localhost:5000'


## Test tokens: Bearer method
Casting assistant permission: get:movies get:actors 
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViZjg0MjRlZDQwYmVlMzZjZjhhIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTkxNzE5NzM0LCJleHAiOjE1OTE4MDYxMzQsImF6cCI6Ikk1Z1VlNExmb1FZNTNhS0RmWVdjelRPVG91MXYzb0FkIiwiZ3R5IjoicGFzc3dvcmQiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.zMTSO3xADKO1d8J5iymK-WSG-aF7j7vATwd4f5bOqzuV2Ows5YfBoAi9ecLYl3niqBbbhxHbD_tYrTrg7jkzGEYpn4ZxbS7CIbtWS5Bhdn5OBs6VQbq-l2tN4BL4f0uQkAEIMXh2xHJbgBdHVL8aC6FMQh6WX5qxjFN2xI-XukL7z5r6oZoMG85bTcZlcPNZABWZ8bjF3Lr539oosLrM8r6YdcRx-FNWWnSMVcJPpfjC0Du2oFYbuhvI7mrlPf4uW5qLZz9eP5m1f6nBrwgHmozFo0I2zh6GOA3hBXKSQwauzKp_sJxW_SzDJJ44UMky54oDbZG2vkEZmUWRD9c14Q","expires_in":86400,"token_type":"Bearer"} 

Casting director permission: get:movies get:actors post:actors delete:actors patch:actors patch:movies
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViZDA0ZTFiYzcwYmYyZjA4Zjg3IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTkxNzE5NzEyLCJleHAiOjE1OTE4MDYxMTIsImF6cCI6Ikk1Z1VlNExmb1FZNTNhS0RmWVdjelRPVG91MXYzb0FkIiwiZ3R5IjoicGFzc3dvcmQiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.uuE3j0lduvZ7VzsVHWLzxEecRSeWHdhIClLsatkfphS1IP6vA-8US7ymeRBT2zsLjT8R3kVtj9tUFhoga12V0nMdry_6h0DCV-723ZVCqQDSYeTZl8W6012Ml9kfheD9KMhU-pb3_3fsgDYcRy0WqZxbB9Wse_ZAGM1r914e1FI0ZY9rxrMEHzMks9I0im-INR1DlJvqqAHHptyH7cNt39MJ_EG5g32QV6LqEPN-psErhiiN6o7Lju3qdOJN4W7xebr0XlDqHrQ3y5t9h52QnLjBXbaZzpp7UiWtxm2bM0KrOWhGZh5g0oFWYVq95RBr5ykbw96fgL0nxkk1D-vyOA","expires_in":86400,"token_type":"Bearer"}

Executive producer permission: get:movies get:actors post:actors post:movies delete:actors delete:movies patch:actors patch:movies
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViOWQyNjYxNGEwYmU0YjQwNGFhIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTkxNzE5Njg5LCJleHAiOjE1OTE4MDYwODksImF6cCI6Ikk1Z1VlNExmb1FZNTNhS0RmWVdjelRPVG91MXYzb0FkIiwiZ3R5IjoicGFzc3dvcmQiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.HClF6XNE3-1vzI8fOFGs8uNdqZKBYN6omkdkrrH9Ia2owSY9ozcJC728EpOfxP5jsi17iH3FPYSxpHBZ14eokvPTFmgAJHFSJbKGaAAbdo9VEfFoihXfSVXMu5IHzTmWCBgDxsF4Xf_bJ94TE_2o3Fr7FgCKa3YPzSuG3HJzswli5NaPgJQKh56AdHYllolhpVQObbHJsC3ifk_x5k9B-rEsILm1BUAkh9UyF0jpFkKDoakwD0KRGP6mx33kcQ4eomjmAwQNfN06DPEXMSbiVZ3KqFXNrOLU_bW9Ft5u5Kg7-7GxvuuhHi_eHE13wQn_DaRYKeIOIeR6G2iXaDBz_Q","expires_in":86400,"token_type":"Bearer"}


