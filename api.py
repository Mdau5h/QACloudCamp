import requests


class BaseAPI:

    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com'

    def get_posts(self) -> requests.Response:
        return requests.get(self.base_url + '/posts')

    def create_post(self, data: dict) -> requests.Response:
        return requests.post(self.base_url + '/posts', data=data)
