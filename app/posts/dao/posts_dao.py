import json

from json import JSONDecodeError

import config

class Posts_dao:
    def __init__(self, way_posts):
        self.way_posts = way_posts


    def get_all_posts(self) -> list[dict]:
        """
        получает данные всех постов из json файла
        :return: список словарей
        """

        with open(self.way_posts, 'r', encoding='utf-8') as file:
            json_file:[list] = json.load(file)
        return json_file


    def get_posts_by_user(self, user_name: str) -> list[dict]:
        """
        ищет посты определённого юзера
        :param user_name: имя юзера
        :return: список постов
        """
        all_posts = self.get_all_posts()
        # списов куда будут добовлятся посты
        posts_username = []
        # цикл поиска и добовления постов
        for post in all_posts:
            if user_name.lower() in post["poster_name"].lower():
                posts_username.append(post)
        # вывод если постов не найдено
        if not posts_username:
            return False

        return posts_username

    def search_for_posts(self, query: str) -> list[dict]:
        """
        поиск постов по ключевому слову
        :param query: ключевое слово
        :return: список постов
        """
        # знаки припинания
        punctuations = '''!()—[]{};:'"\,<>./?@#$%^&*_~'''
        all_posts = self.get_all_posts()
        # список постов
        search_posts = []
        #цикл поиска и добовления постов
        if all_posts:
            for post in all_posts:
                content_post = self.strip_punctuation_ru(post["content"])
                if query.lower() in content_post.lower().split():
                    search_posts.append(post)
            if not search_posts:
                return False
            return search_posts
        else:
            False


    def get_post_by_pk(self, pk: int) -> dict:
        """
        поиск поста по его номеру
        :param pk: номер
        :return: данные поста
        """
        all_posts = self.get_all_posts()
        for post in all_posts:
            if post['pk'] == pk:
                return post
            else:
                False

    def strip_punctuation_ru(seif, string: str) -> str:
        """
        удаление знаков припинания из строки
        :param string: текст
        :return: строку без знаков припинания
        """
        # знаки припинания
        punctuations = '''!()—[]{};:'"\,<>./?@#$%^&*_~'''
        # пустая строка
        new_string = ""
        # цикл удаления знаков припинания
        for char in string:
            if char in punctuations:
                new_string += ' '
            else:
                new_string += char
        new_string = new_string.replace(" - ", " ")
        return " ".join(new_string.split())


#all_posts = Posts_dao('../../../data/posts.json')
#with open('../../../data/posts.json')

#print(all_posts.search_for_posts('ага'))





