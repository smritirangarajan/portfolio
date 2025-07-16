import unittest
from peewee import *
from app import TimelinePost

MODELS = [TimelinePost]
# Use proper in-memory SQLite string (no space)
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        self.assertEqual(first_post.id, 1)

        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        self.assertEqual(second_post.id, 2)

        posts = TimelinePost.select()
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0].id, 1)
        self.assertEqual(posts[1].id, 2)

        second_post.delete_instance()
    
