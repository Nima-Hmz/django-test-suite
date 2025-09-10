from django.test import SimpleTestCase
from unittest.mock import patch, MagicMock, call
from django.urls import reverse
from .side_effect_functions import post_view_3_url_fake_data
import requests

class TestPostViewNima(SimpleTestCase):
    def test_post_view_success_nima(self):
        # creating the mock object
        with patch('fourth.views.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            return_data = {'name':'nima'}
            mock_get.return_value.json.return_value = return_data

            # sending the request
            response = self.client.get(reverse('fourth:post'))

            # start testing 
            self.assertEqual(response.status_code, 200)

            # ensuring correct mocking 
            mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts/1')


    def test_post_view_fail_nima(self):
        with patch('fourth.views.requests.get') as mock_get:
            # creating the mock object 
            mock_get.side_effect = requests.exceptions.RequestException

            # sending the request 
            response = self.client.get(reverse('fourth:post'))

            # start testing
            self.assertEqual(response.status_code, 503)

            # ensuring correct mocking 
            mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts/1')

    
# multiple api version + custom mock objects + side effect function
class TestPostView3Nima(SimpleTestCase):
    def test_post_view3_success_nima(self):
        # creating the mocks and assign them
        with patch('fourth.views.requests.get', side_effect=post_view_3_url_fake_data) as mock_get:
            
            # sending the request
            response = self.client.get(reverse('fourth:post3'))

            # start testing
            self.assertEqual(response.status_code, 200)

            # ensuring the correct mocking assign 
            mock_get.assert_has_calls([call('https://jsonplaceholder.typicode.com/posts/1'),
                                        call('https://jsonplaceholder.typicode.com/posts/2'),
                                          call('https://jsonplaceholder.typicode.com/posts/3')])


            
