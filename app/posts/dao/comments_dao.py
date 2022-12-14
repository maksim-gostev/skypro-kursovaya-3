import json
from json import JSONDecodeError

class Comments_dao:
    def __init__(self, way_comments):
        self.way_comments = way_comments


    def get_all_comments(self) -> list[dict]:
        """
        получает данные всех коментариев из json файла
        :return: список словарей
        """
        try:
            with open(self.way_comments, 'r', encoding='utf-8') as file:
                json_file = json.load(file)
            return json_file
        except (FileNotFoundError, JSONDecodeError):
            return False


    def get_comments_by_post_id(self, post_id) -> list[dict]:
        """
        поиск комента по номеру поста
        :param post_id: pk поста
        :return: список словарей
        """
        all_comments = self.get_all_comments()
        # спивок куда будут добавлятся словари коментов
        comments = []
        if all_comments:
            for comment in all_comments:
                if comment["post_id"] == post_id:
                    comments.append(comment)

            if not comments:
                return False
            return comments
        else:
            return False



