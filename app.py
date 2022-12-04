from flask import Flask, render_template

import utils

app = Flask(__name__)

@app.route("/")
def get_all_post():
    all_post = utils.get_posts_all()
    return render_template('index.html', all_post=all_post)


@app.route("/posts/<int:postid>")
def get_posts(postid):
    post = utils.get_post_by_pk(postid)
    all_comments = utils.get_comments_by_post_id(postid)
    return render_template('post.html', post=post, all_comments=all_comments, count_comment=len(all_comments))


@app.route("/search/<search>")
def get_search(search):
    all_post = utils.search_for_posts(search)
    return render_template('search.html', posts=all_post, count_post=len(all_post), search=search)

@app.route("/users/<username>")
def get_post_username(username):
    all_post_username = utils.get_posts_by_user(username)
    return render_template('user-feed.html', posts=all_post_username)


app.run()