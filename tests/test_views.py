from django.test import TestCase
from django.urls import reverse
from datetime import datetime, timedelta
from ThoughtsApp.models import Thoughts
from django.contrib.auth.models import User


class IndexViewTestCase(TestCase):
    def setUp(self):
        # Create some thoughts objects for testing
        self.thought1 = Thoughts.objects.create(
            title='Thought 1',
            text='This is the first thought.',
            pub_date=datetime.now()
        )
        self.thought2 = Thoughts.objects.create(
            title='Thought 2',
            text='This is the second thought.',
            pub_date=datetime.now() - timedelta(days=1)
        )

    def test_index_view(self):
        # Make a GET request to the index view
        response = self.client.get(reverse('index'))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'ThoughtsApp/index.html')

        # Check that the thoughts are ordered by pub_date descending
        thoughts_list = response.context['thoughts_list']
        self.assertEqual(list(thoughts_list), [self.thought1, self.thought2])


class MyThoughtsViewTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.username = 'tester'
        self.password = 'password'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

        # Create some thoughts objects for testing
        self.thought1 = Thoughts.objects.create(
            title='Thought 1',
            text='This is the first thought.',
            pub_date=datetime.now(),
            author=self.user
        )
        self.thought2 = Thoughts.objects.create(
            title='Thought 2',
            text='This is the second thought.',
            pub_date=datetime.now() - timedelta(days=1),
            author=self.user
        )

    def test_my_thoughts_view(self):
        # Log in the user
        self.client.login(username=self.username, password=self.password)

        # Make a GET request to the myThoughtsView
        response = self.client.get(reverse('my_thoughts'))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'ThoughtsApp/myThoughts.html')

        # Check that the thoughts are ordered by pub_date descending
        thoughts_list = response.context['thoughts_list']
        self.assertEqual(list(thoughts_list), [self.thought1, self.thought2])

