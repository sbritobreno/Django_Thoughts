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
        self.assertEqual(str(thought), self.thought_text)

    def test_thought_admin_display(self):
        thought = Thoughts.objects.create(
            user=self.user,
            thought_text=self.thought_text,
            pub_date=self.pub_date
        )
        self.assertTrue(thought._meta.get_field('pub_date').admin_order_field)
        self.assertTrue(thought._meta.get_field('pub_date').boolean)
        self.assertEqual(thought._meta.get_field('pub_date').verbose_name, 'date published')
