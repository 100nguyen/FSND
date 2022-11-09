# Backend - Casting Agency API

## Casting Agency Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Models:

Movies with attributes title and release date
Actors with attributes name, age and gender
Endpoints:
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/
Roles:
Casting Assistant
Can view actors and movies
Casting Director
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies
Executive Producer
All permissions a Casting Director has and…
Add or delete a movie from the database
Tests:
One test for success behavior of each endpoint
One test for error behavior of each endpoint
At least two tests of RBAC for each role


Document project description in README file, including the following information:
Motivation for the project
URL location for the hosted API
Project dependencies, local development and hosting instructions,
Detailed instructions for scripts to set up authentication, install any project dependencies and run the development server.
Documentation of API behavior and RBAC controls
## Setting up the Backend

### Motivation
Use all of the concepts and the skills taught in the courses to build an API from start to finish and host it:

Coding in Python 3
Relational Database Architecture
Modeling Data Objects with SQLAlchemy
Internet Protocols and Communication
Developing a Flask API
Authentication and Access
Authentication with Auth0
Authentication in Flask
Role-Based Access Control (RBAC)
Testing Flask Applications
Deploying Applications

### URL location for the hosted API

### Install Dependencies

1. **Python 3.10** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `capstone` database:

```bash
createdb capstone
```

### Run the Server

First ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Endpoints documentation

#### `GET '/movies'`
- Fetches a dictionary of movies
- Required URL Arguments: None
- Required Data Arguments: None
- Returns: Returns JSON data about movies 
- Success Response:
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "01/01/2012",
            "title": "Lion King",
        },
        {
            "id": 2,
            "release_date": "08/12/2019",
            "title": "Joker",
        }
    ],
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

#### `POST '/movies'`
- Post a new movie in a database.
- Required URL Arguments: None 
- Required Data Arguments:  JSON data                
- Success Response:
```
{
    "movie": {
        "id": 6,
        "release_date": "08/01/2002",
        "title": "Toy Story",
    },
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

#### `PATCH '/movies/<int:movie_id>'`
- Updates the `movie_id` of movie
- Required URL Arguments: `movie_id: movie_id_integer` 
- Required Data Arguments: None
- Returns: JSON data about the updated movie 
- Success Response:
```
{
    "movie": {
        "id": 5,
        "release_date": "12/05/2018",
        "title": "Thor"
    },
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

#### `DELETE '/movies/<int:movie_id>'`
- Deletes the `movie_id` of movie
- Required URL Arguments: `movie_id: movie_id_integer` 
- Required Data Arguments: None
- Returns: JSON data about the deleted movie's ID 
- Success Response:
```
{
    "id": 5,
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

#### `GET '/actors'`
- Fetches a dictionary of actors
- Required Data Arguments: None
- Returns: JSON data about actors
- Success Response:
```
  {
    "actors": [
        {
            "age": 36,
            "gender": "male",
            "id": 1,
            "name": "Edward",
        },
        {
            "age": 25,
            "gender": "other",
            "id": 2,
            "name": "David",
        },
        {
            "age": 35,
            "gender": "female",
            "id": 3,
            "name": "Jeff",
        }
    ],
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

#### `POST '/actors'`
- Post a new actor in a database.
- Required URL Arguments: None 
- Required Data Arguments:  JSON data   

- Success Response:
```
{
    "actor": {
        "age": 18,
        "gender": "other",
        "id": 4,
        "name": "Penny",
    },
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

#### `PATCH '/actors/<int:actor_id>'`
- Updates the `actor_id` of actor
- Required URL Arguments: `actor_id: actor_id_integer` 
- Required Data Arguments: None
- Returns: JSON data about the deleted actor's ID 
- Success Response:
```
{
    "actor": {
        "age": 28,
        "gender": "other",
        "id": 4,
        "name": "Penny"
    },
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

#### `DELETE '/actors/<int:actor_id>'`
- Deletes the `actor_id` of actor
- Required URL Arguments: `actor_id: actor_id_integer` 
- Required Data Arguments: None
- Returns: JSON data about the deleted actor's ID 
- Success Response:
```
{
    "id_deleted": 4,
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

## Testing
For testing, required JWT for each role is included for each role.

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```
python3 test_app.py
```
