
import json

from json import JSONDecodeError


class Bookmarks_dao:
    def __init__(self, way_bookmarks):
        self.way_bookmarks = way_bookmarks

    def get_all_bookmarks(self) -> list[dict]:
        """
        получает данные всех закладок из json файла
        :return: список закладок
        """
        try:
            with open(self.way_bookmarks, 'r', encoding='utf-8') as file:
                json_file:[list] = json.load(file)
            return json_file
        except (FileNotFoundError, JSONDecodeError):
            return False


    def save_booksmarks_to_json(self,bookmarks) ->list[dict]:
        """
        записывает данные всех закладок
        :param bookmarks: список закладок
        """
        with open(self.way_bookmarks, 'w', encoding='utf-8') as file:
            json.dump(bookmarks, file, ensure_ascii=False, sort_keys=True, indent=4)


    def add_bookmarks(self, bookmarks_pk: int, all_posts:list[dict]):
        """
        добовляет новую закладку в список
        :param bookmarks_pk: номер поста
        :return: ничего
        """
        all_bookmarks = self.get_all_bookmarks()
        for post in all_posts:
            if post["pk"] == bookmarks_pk:
                all_bookmarks.append(post)
        self.save_booksmarks_to_json(all_bookmarks)


    def delete_bookmarks(self,bookmarks_pk: int):
        """
        удаляет закладку из списка
        :param bookmarks_pk: номер поста
        :return: ничего
        """
        all_bookmarks = self.get_all_bookmarks()
        for index, bookmarks in enumerate(all_bookmarks):
            if bookmarks['pk'] == bookmarks_pk:
                del all_bookmarks[index]
                break
        self.save_booksmarks_to_json(all_bookmarks)
