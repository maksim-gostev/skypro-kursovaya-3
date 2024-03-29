from flask import Blueprint, render_template, request, jsonify

from app.posts.dao.posts_dao import Posts_dao
from app.posts.dao.comments_dao import Comments_dao
from app.bookmarks.dao.bookmarks_dao import Bookmarks_dao
from app.posts.dao.utils import tag_replace

import constant

post_bluprint = Blueprint('post_bluprint', __name__)

posts_dao = Posts_dao(constant.POSTS_WAY)
comments_dao = Comments_dao(constant.COMMENTS_WAY)
bookmarks = Bookmarks_dao(constant.BOOKMARKS_WAY)


@post_bluprint.route('/')
def get_all_post():
    """
    вывод ленты постов
    :return: выводит ленту постов
    """
    all_bookmarks = bookmarks.get_all_bookmarks()
    all_post = posts_dao.get_all_posts()
    if all_post and all_bookmarks:
        all_tag_post = tag_replace(all_post)
        return render_template('index.html', all_post=all_tag_post, quantity=len(all_bookmarks))
    else:
        'ошибка на сервере'


@post_bluprint.route("/posts/<int:post_id>")
def get_posts(post_id):
    """
    вывод поста по id
    :param postid: номер поста
    :return: выводит пост
    """
    post = posts_dao.get_post_by_pk(post_id)
    all_comments = comments_dao.get_comments_by_post_id(post_id)
    if post and all_comments:
        tag_post = tag_replace(post)
        return render_template('post.html', post=tag_post, all_comments=all_comments, count_comment=len(all_comments))
    else:
        return 'ошибка на сервере'


@post_bluprint.route("/search")
def get_search():
    """
    вывод поста по ключевому слову
    :return: посты по ключевому слову
    """
    string_search = request.args['s']
    if string_search:
        all_post = posts_dao.search_for_posts(string_search)

        if all_post:
            all_tag_post = tag_replace(all_post)
            if len(all_post) > 10:
                all_post = all_post[10]

            return render_template('search.html', posts=all_tag_post, count_post=len(all_post), search=string_search)
        else:
            return 'ошибка на сервере'
    else:
        'вы не ввели слово'

@post_bluprint.route("/users/<username>")
def get_post_username(username):
    """
    вывод постов юзера
    :param username: имя юзера
    :return: список постов
    """
    all_post_username = posts_dao.get_posts_by_user(username)
    if all_post_username:
        all_tag_post = tag_replace(all_post_username)
        return render_template('user-feed.html', posts=all_tag_post)
    else:
        'ошибка на сервере'

@post_bluprint.route("/tag/<tagname>")
def search_post_tag(tagname):
    """
    вывод постов по тегу
    :param tagname: тег слово
    :return: список словарей
    """
    all_posts = posts_dao.search_for_posts(tagname)
    if all_posts:
        return render_template('tag.html', all_posts=all_posts, tagname=tagname)
    else:
        'ошибка на сервере'
