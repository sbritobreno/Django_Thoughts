from django.test import TestCase, Client
from django.utils import timezone
from ThoughtsApp.models import Thoughts
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='tester',
            email='tester@example.com',
            password='password'
        )
        self.thought1 = Thoughts.objects.create(
            user=self.user,
            thought_text='Test thought 1',
            pub_date=timezone.now()
        )
        self.thought2 = Thoughts.objects.create(
            user=self.user,
            thought_text='Test thought 2',
            pub_date=timezone.now() - timezone.timedelta(days=1)
        )

    def test_index_view(self):
        response = self.client.get(reverse('ThoughtsApp:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ThoughtsApp/index.html')
        thoughts_list = response.context['thoughts_list']
        self.assertQuerysetEqual(
            thoughts_list,
            [self.thought1, self.thought2],
            ordered=True
        )


class MyThoughtsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='tester', password='password')
        self.thought1 = Thoughts.objects.create(user=self.user, thought_text='Test thought 1', pub_date=datetime.now())
        self.thought2 = Thoughts.objects.create(user=self.user, thought_text='Test thought 2', pub_date=datetime.now() + timedelta(days=1))

    def test_my_thoughts_view(self):
        # Login the user
        self.client.login(username='tester', password='password')

        # Get the URL for the MyThoughtsView
        url = reverse('ThoughtsApp:mythoughts')

        # Make a GET request to the view
        response = self.client.get(url)

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is being used
        self.assertTemplateUsed(response, 'ThoughtsApp/myThoughts.html')

        # Check that the thoughts list contains only the thoughts created by the user
        thoughts = response.context['thoughts_list']
        expected_thoughts = Thoughts.objects.filter(user=self.user).order_by('-pub_date')
        expected_thoughts_str = [str(thought) for thought in expected_thoughts]
        self.assertQuerysetEqual(thoughts, expected_thoughts_str, transform=str)


