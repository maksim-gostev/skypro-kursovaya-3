from flask import Flask
from app.posts.views import post_bluprint


app = Flask(__name__)

app.register_blueprint(post_bluprint)




@app.errorhandler(404)
def error404(error):
    return 'статус код 404'


@app.errorhandler(500)
def error500(erroe):
    return 'статус код 500'

if __name__ == '__main__':
    app.run()
