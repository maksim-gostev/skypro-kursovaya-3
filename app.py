from flask import Flask, render_template

import utils

app = Flask(__name__)

@app.route("/")
def get_all_post():
    all_post = utils.get_posts_all()
    return render_template('index.html', all_post=all_post)



app.run()