from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your tests here.

class TestAuthentication(TestCase):
    def test_dashboard_is_not_accessible_for_anonymous_users(self):
        response = self.client.get(reverse('fourth:dashboard'))
        self.assertRedirects(response, expected_url=reverse('fourth:login'))

    def test_dashboard_is_accessible_for_authenticated_users(self):

        # create the user
        User = get_user_model()
        User.objects.create_user(username='test1235', password='nima7176')

        # log the user in 
        self.client.login(username='test1235', password='nima7176')

        # check if the username is in the template
        response = self.client.get(reverse('fourth:dashboard'))
        self.assertContains(response, 'test1235')
