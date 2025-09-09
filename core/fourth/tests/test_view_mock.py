from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse
import requests

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



    # the test of the hard coded view 
    @patch('fourth.views.requests.get')
    def test_request_view_success_post2(self, mock_get):
        # making the mock ready 
        mock_get.return_value.status_code = 200
        return_data = {'id':1}
        mock_get.return_value.json.return_value = return_data

        # sending the request
        response = self.client.get(reverse('fourth:post2'))

        # start testing 
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, return_data)

        # validation of the mock 
        mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts/1')

    # the test of the hard coded view 
    @patch('fourth.views.requests.get')
    def test_request_view_fail_post2(self, mock_get):
        # making the mock ready 
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {}

        # sending the request
        response = self.client.get(reverse('fourth:post2'))

        # start testing 
        self.assertEqual(response.status_code, 503)

        # start validation 
        mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts/1')   
