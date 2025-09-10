from unittest.mock import Mock

def post_view_3_url_fake_data(url, *args, **kwargs):
    if url == 'https://jsonplaceholder.typicode.com/posts/1':
        mock = Mock()
        mock.status_code = 200
        mock.json.return_value = {"id":1}
        return mock

    if url == 'https://jsonplaceholder.typicode.com/posts/2':
        mock = Mock()
        mock.status_code = 200
        mock.json.return_value = {"id":2}
        return mock

    if url == 'https://jsonplaceholder.typicode.com/posts/3':
        mock = Mock()
        mock.status_code = 200
        mock.json.return_value = {"id":3}
        return mock
    
    else:
        mock = Mock()
        mock.status_code = 404
        mock.return_value = {}
        return mock
