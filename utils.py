import json

def get_posts_all():
    """
    возвращает посты
    :return: список постов
    """
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        json_file = json.load(file)
        return json_file


def get_all_comments():
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        json_comment_file = json.load(file)
        return json_comment_file


def get_posts_by_user(user_name):
    """
    возвращает посты определенного пользователя.
    Функция должна вызывать ошибку ValueError если такого пользователя нет
    и пустой список, если у пользователя нет постов.
    :param user_name:
    :return:
    """
    pass


def get_comments_by_post_id(post_id):
    all_comments = get_all_comments()
    comments = []
    for comment in all_comments:
        if comment["post_id"] == post_id:
            comments.append(comment)
    return comments

def search_for_posts(query):
    """
    возвращает список постов по ключевому слову
    :param query:
    :return:
    """
    pass


def get_post_by_pk(pk):
    all_post = get_posts_all()
    post_id = []
    for post in all_post:
        if post["pk"] == pk:
            post_id.append(post)
    return post_id
get_post_by_pk(1)

