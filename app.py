from flask import Flask, render_template

import utils

app = Flask(__name__)

@app.route("/")
def get_all_post():
    all_post = utils.get_posts_all()
    return render_template('index.html', all_post=all_post)


@app.route("/posts/<int:postid>")
def get_posts(postid):
    post_id = utils.get_post_by_pk(postid)
    all_comments = utils.get_comments_by_post_id(postid)
    return render_template('post.html', all_comments=all_comments, post_id=post_id, count_comment=len(all_comments))



app.run()