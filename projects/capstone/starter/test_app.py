import os
import unittest
import json
import random
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor
from settings import DB_NAME, DB_USER, DB_PASSWORD, \
    CASTING_ASSISTANT_TOKEN, CASTING_DIRECTOR_TOKEN, EXECUTIVE_PRODUCER_TOKEN


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the Casting Agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.casting_assistant_token = CASTING_ASSISTANT_TOKEN
        self.casting_director_token = CASTING_DIRECTOR_TOKEN
        self.executive_producer_token = EXECUTIVE_PRODUCER_TOKEN

        setup_db(self.app)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

        self.app = create_app()
        self.client = self.app.test_client
        self.db_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER,
                                                         DB_PASSWORD,
                                                         'localhost:5432',
                                                         DB_NAME)

        setup_db(self.app, self.db_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    '''
    RBAC TEST
    '''

    def test_get_movies_by_casting_assistant_with_auth_200(self):
        response = self.client().get(
            '/movies',
            headers={
                "Authorization": "Bearer {}".format(
                    self.casting_assistant_token)
            })
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_actors_by_casting_assistant_with_auth_200(self):
        response = self.client().get(
            '/actors',
            headers={
                "Authorization": "Bearer {}".format(
                    self.casting_assistant_token)
            })
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_movies_by_casting_assistant_without_auth_401(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)

    def test_get_actors_by_casting_assistant_without_auth_401(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)

    def test_post_movies_by_casting_assistant_without_auth_403(self):
        response = self.client().post(
            '/movies',
            headers={
                "Authorization": "Bearer {}".format(
                    self.casting_assistant_token)
            },
            json={
                "title": "American Made",
                "release_date": "05/12/2018",
            })

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)

    def test_post_actors_by_casting_assistant_without_auth_403(self):
        response = self.client().post(
            '/actors',
            headers={
                "Authorization": "Bearer {}".format(
                    self.casting_assistant_token)
            },
            json={
                "name": "Brandon",
                "gender": "Male",
                "age": 16
            })
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)

    def test_patch_movies_by_casting_assistant_without_auth_403(self):
        random_id = random.choice([movie.id for movie in Movie.query.all()])
        response = self.client().patch(
            '/movies/{}'.format(random_id),
            headers={"Authorization": "Bearer {}".format(
                self.casting_assistant_token)
            },
            json={
                "title": "Joker",
                "release_date": "10/01/2019"
            })

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)

    def test_patch_actors_by_casting_assistant_without_auth_403(self):
        random_id = random.choice([actor.id for actor in Actor.query.all()])
        response = self.client().patch('/actors/{}'.format(random_id),
                                       headers={
            "Authorization": "Bearer {}".format(self.casting_assistant_token)
        },
            json={
            "name": "David",
            "gender": "other",
            "age": 10
        })

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)

    def test_delete_movies_by_casting_assistant_without_auth_403(self):
        random_id = random.choice([movie.id for movie in Movie.query.all()])
        response = self.client().delete(
            'movies/{}'.format(random_id),
            headers={
                "Authorization": "Bearer {}".format(
                    self.casting_assistant_token)
            }
        )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)

    def test_delete_actors_by_casting_assistant_without_auth_403(self):
        random_id = random.choice([actor.id for actor in Actor.query.all()])
        response = self.client().delete(
            'actors/{}'.format(random_id),
            headers={
                "Authorization": "Bearer {}".format(
                    self.casting_assistant_token)
            }
        )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)

    def test_post_actors_by_executive_producer_with_auth_200(self):
        response = self.client().post(
            '/actors',
            headers={
                "Authorization": "Bearer {}"
                .format(self.executive_producer_token)
            },
            json={
                "name": "Lio Messi",
                "gender": "Male",
                "age": 25,
            })
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_movies_by_executive_producer_with_auth_200(self):
        response = self.client().post(
            '/movies',
            headers={
                "Authorization": "Bearer {}".format(
                    self.executive_producer_token)
            },
            json={
                'title': 'Prestige',
                'release_date': '01/01/2005'
            })

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movies_by_casting_director_with_auth_200(self):
        random_id = random.choice([movie.id for movie in Movie.query.all()])
        response = self.client().patch(
            '/movies/{}'.format(random_id),
            headers={
                "Authorization": "Bearer {}".format(
                    self.casting_director_token)
                },
            json={
                'title': 'Joker',
                'release_date': '10/01/2019'
                })

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actors_by_casting_director_with_auth_200(self):
        random_id = random.choice([actor.id for actor in Actor.query.all()])
        response = self.client().patch(
            '/actors/{}'.format(random_id),
            headers={
                "Authorization": "Bearer {}".format(
                    self.casting_director_token)
                    },
            json={
                'name': 'Jamal Mashburn',
                'gender': "Male",
                'age': 50
                })

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movies_by_executive_producer_with_auth_200(self):
        random_id = random.choice([movie.id for movie in Movie.query.all()])
        response = self.client().delete(
            'movies/{}'.format(random_id),
            headers={
                "Authorization": "Bearer {}".format(
                    self.executive_producer_token)
                    })
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actors_by_executive_producer_with_auth_200(self):
        random_id = random.choice([actor.id for actor in Actor.query.all()])
        response = self.client().delete(
            'actors/{}'.format(random_id),
            headers={
                "Authorization": "Bearer {}".format(
                    self.executive_producer_token)
                    })
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
