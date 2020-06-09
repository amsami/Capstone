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
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViZjg0MjRlZDQwYmVlMzZjZjhhIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTkxNjM1MjY5LCJleHAiOjE1OTE3MjE2NjksImF6cCI6Ikk1Z1VlNExmb1FZNTNhS0RmWVdjelRPVG91MXYzb0FkIiwiZ3R5IjoicGFzc3dvcmQiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.kSjRMaJqFummUaXDHHI4ppuhK-YDzYPtlZ48N_9NDdcYctlsjHmYaQ8PI7ix9Adm1HrS9jCcmWqu5ccVvBC1rfzSa-NILAbhm5-lsHNg5dDRkNzREr34eJEkhY2V202u6cvomuSVALle2_E7n6cWJK_pHD10KnBs4GQE8IV_fwNzL8sksXYkYf3YoQ-rQO-XL17mO83FTTHeClmpx8A0j0hENcC2DJ5d-iKzx14q92wZ2A81gOSzgEzvksen9s9FO_tb9GUX0-scQ0PbigAdOhrSiyggU6FBynrtlzTD5ZLxY_rgMlNS2UIIB4dncRbmXIRpe-8lwf8H27PP4GBPeQ","expires_in":86400,"token_type":"Bearer"}

Casting director permission: get:movies get:actors post:actors delete:actors patch:actors patch:movies
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViZDA0ZTFiYzcwYmYyZjA4Zjg3IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTkxNjM1MjM0LCJleHAiOjE1OTE3MjE2MzQsImF6cCI6Ikk1Z1VlNExmb1FZNTNhS0RmWVdjelRPVG91MXYzb0FkIiwiZ3R5IjoicGFzc3dvcmQiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.FX9DPyJPbXg_BQaRQIqQ7K1ChIuV2pdstzCIuzC0_eKEg470DPOT8D_Nce_r8kPTxpHN0oCO1dVZvngjAbTDuhSsWFFWVkNGPpGusKBjTYkGBOuq-m8sYX032beyQYVIm87rS_xKqzBBzWKL_jW8sAXpvQKr9_ITeE8cx2r2aziUx5uRMDDMbCc45LxvC83EBcB5NZyMNwWZnKV1ONhv5c4YN98pLV53KHVvulHRSz1bBOmIg8kIccKknSL2EC23Ijt-kg6j91abbZnLe7hKOBMtxeCWLTiOQQLDGMTjOrjEu0YgDjPhjA_KHPHxUglBqYzBQUrpRsE4rsA9cBtstw","expires_in":86400,"token_type":"Bearer"}

Executive producer permission: get:movies get:actors post:actors post:movies delete:actors delete:movies patch:actors patch:movies
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViOWQyNjYxNGEwYmU0YjQwNGFhIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTkxNjM1MjA0LCJleHAiOjE1OTE3MjE2MDQsImF6cCI6Ikk1Z1VlNExmb1FZNTNhS0RmWVdjelRPVG91MXYzb0FkIiwiZ3R5IjoicGFzc3dvcmQiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.msXPYYiUrPTDnpDNSofIGqXoBYFkpB09857tpQsjYMTndAm3szFafPn5hVEy0W7hYSU7xb_FY5TPqs8ksDc-aviPprZJXLUHUH57rBh8MXe4o66sE45zE-UmHJcQJC4rFk-W3sYJT64_TCu_ux07KF4Y24rDdWVBNnLq5ORiBBEcBUy1cEamvadrfw29zabyrAOpBc4UEY_s3o2IiejWk9ueZGjG6aSr6Zmse4_vXsavEN1NU-s-A560vENBfRJLhua64ApFovOGo552PNB1mzC5aEI-I27IIszb-FMk573qoXMd3T_RsAzYqHJDb50yh5H7Au2BR6gS2g2XY5wrOQ","expires_in":86400,"token_type":"Bearer"}



