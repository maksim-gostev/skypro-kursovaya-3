import pytest

from run import app

valid_keys = {"poster_name",
              "poster_avatar",
              "pic",
              "content",
              "views_count",
              "likes_count",
              "pk",
              }

class Test_api:

    def test_api_post(self):
        response = app.test_client().get('/api')
        assert response.status_code == 200
        assert type(response.json) == list, 'возвращает не список'
        assert type(response.json[0]) == dict, 'возвращает не словарь'
        for i in range(len(response.json)):
            assert set(response.json[i].keys()) == set(valid_keys), 'неверный список ключей'


    def test_api_post_pk(self):
        response = app.test_client().get('/api/posts/1')
        assert response.status_code == 200
        assert type(response.json) == list, 'возвращает не список'
        assert type(response.json[0]) == dict, 'возвращает не словарь'
        assert set(response.json.keys()) == set(valid_keys), 'неверный список ключей'
