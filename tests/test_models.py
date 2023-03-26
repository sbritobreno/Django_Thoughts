from django.test import TestCase
from django.contrib.auth.models import User
from ThoughtsApp.models import Thoughts
from datetime import datetime


class ThoughtsModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester',
            email='tester@example.com',
            password='password'
        )
        self.thought_text = 'This is a test thought.'
        self.pub_date = datetime.now()

    def test_create_thought(self):
        thought = Thoughts.objects.create(
            user=self.user,
            thought_text=self.thought_text,
            pub_date=self.pub_date
        )
        self.assertEqual(thought.user, self.user)
        self.assertEqual(thought.thought_text, self.thought_text)
        self.assertEqual(thought.pub_date, self.pub_date)

    def test_thought_str(self):
        thought = Thoughts.objects.create(
            user=self.user,
            thought_text=self.thought_text,
            pub_date=self.pub_date
        )
        # Returns a positive test result
        self.assertEqual(str(thought), self.thought_text)

        # Returns an error because the values are not exactly the same
        # self.assertEqual(str(thought), 'This is a failed test.')

