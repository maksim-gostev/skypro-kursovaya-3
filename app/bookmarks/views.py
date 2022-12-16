from flask import Blueprint, render_template, request, redirect

from app.bookmarks.dao.bookmarks_dao import Bookmarks_dao
from app.posts.dao.posts_dao import Posts_dao

import config

bookmarks_bluprint = Blueprint('bookmarks_bluprint', __name__, url_prefix='/bookmarks')

posts = Posts_dao(config.POSTS_WAY)

bookmarks_dao =Bookmarks_dao(config.BOOKMARKS_WAY)

@bookmarks_bluprint.route('/')
def get_all_bookmarks():
    all_bookmarks = bookmarks_dao.get_all_bookmarks()
    if all_bookmarks:
        return render_template('bookmarks.html', all_bookmarks=all_bookmarks)
    else:
        'ошибка на сервере'


@bookmarks_bluprint.route('/add/<int:post_id>')
def add_bookmarks(post_id):
    all_posts = posts.get_all_posts()
    bookmarks_dao.add_bookmarks(post_id, all_posts)
    return redirect("/bookmarks", code = 302)

@bookmarks_bluprint.route('/remove/<int:post_id>')
def delite_bookmarks(post_id):
    bookmarks_dao.delete_bookmarks(post_id)
    return redirect("/bookmarks", code = 302)
