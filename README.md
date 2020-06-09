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
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViZjg0MjRlZDQwYmVlMzZjZjhhIiwiYXVkIjoiY2FzcHRvbmUiLCJpYXQiOjE1OTE3MjI5NjQsImV4cCI6MTU5MTgwOTM2NCwiYXpwIjoibHlDWExNb3hVWUxCeVFXNFVXOE0zMUl0UUVqTmFHclIiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.jRpdT8JrsiDjcYs0mBEBu1Za-IoSc_Qx2q_o1MmdwGA6yx6dMEy9z-EA8Gbp0QXzeyUKOu4AUKwDf2PE7jJP6eJU4N6FYDGMCxaH_E05ILrKufEYiy1ANpMF8_98AWD7jQZpeHCmtzqumtA2mxaZaUgkn-uBmTkd33vlnKyqvq_X81Lf9mzR7cUqX_eKS5sHU5izFHcihCBOKZBlciF-gG0UJFhJO5bfj8FI_cB9innBpmDsG8gzzOjUetdBIpXgMem0lPJNmYs2xRF2rPyYZMiGqv6xn99PCJQd8WPolOwGCiclJ-zZXH4VHHgTJ524qaTsirzY4SEeHLMnUqRMBw","expires_in":86400,"token_type":"Bearer"}

Casting director permission: get:movies get:actors post:actors delete:actors patch:actors patch:movies
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViZDA0ZTFiYzcwYmYyZjA4Zjg3IiwiYXVkIjoiY2FzcHRvbmUiLCJpYXQiOjE1OTE3MjMwMDIsImV4cCI6MTU5MTgwOTQwMiwiYXpwIjoibHlDWExNb3hVWUxCeVFXNFVXOE0zMUl0UUVqTmFHclIiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.JHW_oC6myPo9KvSaB57wlb1t2PdGuPq0j53lW1wM31lCJvz14R7cvhAY07DpmZcS7xwYme7yWAleSumglDwFdE8vSkFy9ZKWIT8cv9p_zPdBqXrqX6mgsfkrmXPdbC1WEzyWjZw8abZtQzZeUzWhUN94l6ILUNy8qsFm69sPEeBHmDyufmQd7lP3z3iNcLgh7VCDb432f4k4dWBu5tXqpHkhUJ3fY9w4J0S-GEKH2FFYAoDY2uirUsl0pLoOhwulwYet8tnoRbuybRZKZb26eQvfRBJD7UEdaNuQof560p5bzco-XuIreB0Yo8ABeL-oOilazj83fs42zHvMCns7dQ","expires_in":86400,"token_type":"Bearer"}

Executive producer permission: get:movies get:actors post:actors post:movies delete:actors delete:movies patch:actors patch:movies
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpHYnNWOHFnVEJxdXV2a2NaUWxSRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FtaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNWViOWQyNjYxNGEwYmU0YjQwNGFhIiwiYXVkIjoiY2FzcHRvbmUiLCJpYXQiOjE1OTE3MjMwMzMsImV4cCI6MTU5MTgwOTQzMywiYXpwIjoibHlDWExNb3hVWUxCeVFXNFVXOE0zMUl0UUVqTmFHclIiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.nW4ArExMJkwfTOgCsnNcDav1kGPOhcGtk0FXY55cJdwXSTU6vYhOGhxQPSiS701Uf9s5MFWLo5HiwYGOvUUEROdk2zWG1JvfiriuSBItZtWEOAzra6UAKRzvOW-OB98mBAHe_SNJFAfX3fhcaAxZZdlEyM-b8DFRFwzSFfkqhfH97wZFmC5EE3x36XJ6vDvTvQQw2c9FILX_fKxWFh9iIvtM148yKSO2Bh1rIMq6XMW67b5E4qk-xsXQVYxSlD3YkdUxRVID9hzfytVNTk6XdXYsr67rOIfDJMFdmpV9cr_097iCQLVPwhxlqYNcakYiYppx-VECU_pA82H9s-Qzgg","expires_in":86400,"token_type":"Bearer"}

