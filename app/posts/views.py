from flask import Blueprint, render_template, request

from app.posts.dao.posts_dao import Posts_dao
from app.posts.dao.comments_dao import Comments_dao
import config

post_bluprint = Blueprint('post_bluprint', __name__)

posts_dao = Posts_dao(config.POSTS_WAY)
comments_dao = Comments_dao(config.COMMENTS_WAY)


@post_bluprint.route("/")
def get_all_post():
    all_post = posts_dao.get_all_posts()
    if all_post:
        return render_template('index.html', all_post=all_post)
    else:
        'ошибка на сервере'


@post_bluprint.route("/posts/<int:postid>")
def get_posts(postid):
    post = posts_dao.get_post_by_pk(postid)
    all_comments = comments_dao.get_comments_by_post_id(postid)
    return render_template('post.html', post=post, all_comments=all_comments, count_comment=len(all_comments))


@post_bluprint.route("/search")
def get_search():
    string_search = request.args['s']

    all_post = posts_dao.search_for_posts(string_search)
    return render_template('search.html', posts=all_post, count_post=len(all_post), search=string_search)

@post_bluprint.route("/users/<username>")
def get_post_username(username):
    all_post_username = posts_dao.get_posts_by_user(username)
    return render_template('user-feed.html', posts=all_post_username)

