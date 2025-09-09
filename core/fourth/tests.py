from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from unittest.mock import Mock, patch
import requests

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


# net ninja mocking way
class TestPostView(TestCase):
    @patch('fourth.views.requests.get')
    def test_request_view_success(self, mock_get):
        mock_get.return_value.status_code = 200
        return_data = {
            'userId':1,
            'id':1,
            'title':"test title",
            'body':'test body'
        }
        mock_get.return_value.json.return_value = return_data

        # sending a request to the view
        response = self.client.get(reverse('fourth:post'))

        # stat testing
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, return_data)

        # ensure the mock api call was made once with the correct argument
        mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts/1')


    @patch('fourth.views.requests.get')
    def test_request_view_fail(self, mock_get):
        
        # creating the mock
        mock_get.side_effect = requests.exceptions.RequestException

        # sending the request
        response = self.client.get(reverse('fourth:post'))

        # stating test
        self.assertEqual(response.status_code, 503)

        # ensure the mock api call was made once with the correct argument
        mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts/1')









    

