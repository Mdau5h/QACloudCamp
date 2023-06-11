from api import BaseAPI

api = BaseAPI()


class TestInit:

    def test_first(self):
        response = api.get_posts()
        assert response.status_code == 200
        assert response.json()[0]['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
