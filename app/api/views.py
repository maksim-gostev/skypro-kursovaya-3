import os
from flask import Blueprint, jsonify
import logging


from app.posts.dao.posts_dao import Posts_dao
import config

api_bluprint = Blueprint('api_bluprint', __name__, url_prefix='/api')

posts_dao = Posts_dao(config.POSTS_WAY)

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                    level=logging.INFO,
                    handlers=[logging.FileHandler(filename=os.path.join('logs', 'api.log'),
                                                  encoding='utf-8',
                                                  mode='a+')
                              ]
                    )

@api_bluprint.route('/')
def get_all_post():
    all_posts = posts_dao.get_all_posts()
    logging.info(f'Запрос /api/posts')
    if all_posts:
        return jsonify(all_posts)
    else:
        return 'ошибка на сервере'


@api_bluprint.route('/posts/<int:post_id>')
def get_post(post_id):
    post = posts_dao.get_post_by_pk(post_id)
    logging.info(f'Запрос /api/posts/{post_id}')
    if post:
        return jsonify(post)
    else:
        'ошибка на сервере'
