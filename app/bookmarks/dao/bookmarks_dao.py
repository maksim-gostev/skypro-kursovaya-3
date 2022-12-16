
import json

from json import JSONDecodeError

from app.posts.dao.posts_dao import Posts_dao

import config



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


    def save_booksmarks_to_json(self,bookmarks) ->[list]:
        """
        записывает данные всех закладок
        :param bookmarks: список закладок
        """
        with open(self.way_bookmarks, 'w', encoding='utf-8') as file:
            json.dump(bookmarks, file, ensure_ascii=False)


    def add_bookmarks(self, bookmarks_pk: int, all_posts):
        """
        добовляет новую закладку в список
        :param bookmarks_pk: номер поста
        :return: ничего
        """
        all_bookmarks = self.get_all_bookmarks()
        print(all_posts)
        for post in all_posts:
            if post["pk"] == bookmarks_pk:
                all_bookmarks.append(post)
        return all_bookmarks
        #self.save_booksmarks_to_json(all_bookmarks)


    def delete_bookmarks(self,bookmarks_pk: int):
        """
        удаляет закладку из списка
        :param bookmarks_pk: номер поста
        :return: ничего
        """
        all_bookmarks = self.get_all_bookmarks()
        for index, bookmarks in enumerate(all_bookmarks):
            if bookmarks['pk'] == bookmarks_pk:
                del bookmarks[index]
                break
        self.save_booksmarks_to_json(all_bookmarks)









