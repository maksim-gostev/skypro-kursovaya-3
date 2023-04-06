from flask import Blueprint, render_template, redirect

from app.bookmarks.dao.bookmarks_dao import Bookmarks_dao
from app.posts.dao.posts_dao import Posts_dao
from app.posts.dao.utils import tag_replace

import constant

bookmarks_bluprint = Blueprint('bookmarks_bluprint', __name__, url_prefix='/bookmarks')

posts = Posts_dao(constant.POSTS_WAY)

bookmarks_dao =Bookmarks_dao(constant.BOOKMARKS_WAY)

@bookmarks_bluprint.route('/')
def get_all_bookmarks():
    """
    выводит ленту закладок
    :return: список словарей закладок
    """
    all_bookmarks = bookmarks_dao.get_all_bookmarks()
    if all_bookmarks:
        all_tag_bookmarks = tag_replace(all_bookmarks)
        return render_template('bookmarks.html', all_bookmarks=all_tag_bookmarks)
    else:
        'ошибка на сервере'


@bookmarks_bluprint.route('/add/<int:post_id>')
def add_bookmarks(post_id):
    """
    добовляет пост в закладки
    :param post_id: pk поста
    :return: перенаправляет на страницу ленты закладок
    """
    all_posts = posts.get_all_posts()
    bookmarks_dao.add_bookmarks(post_id, all_posts)
    return redirect("/bookmarks", code = 302)

@bookmarks_bluprint.route('/remove/<int:post_id>')
def delite_bookmarks(post_id):
    """
    удаляет пост из списка закладок
    :param post_id: pk номер поста
    :return: перенаправляет на страницу ленты закладок
    """
    bookmarks_dao.delete_bookmarks(post_id)
    return redirect("/bookmarks", code = 302)
