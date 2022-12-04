import json

def get_posts_all():
    """
    возвращает посты
    :return: список постов
    """
    result_file = []

    with open('data/posts.json', 'r', encoding='utf-8') as file:
        json_file = json.load(file)


    for file in json_file:
        if len(file["content"]) > 50:
            file['min_comment'] = file["content"][0: 47] + '...'
            result_file.append(file)
        else:
            file['min_comment'] = file["content"]
            result_file.append(file)
    return result_file

def get_all_comments():
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        json_comment_file = json.load(file)
        return json_comment_file


def get_posts_by_user(user_name):
    all_posts = get_posts_all()
    posts_username = []
    for post in all_posts:
        if user_name.lower() in post["poster_name"].lower():
            posts_username.append(post)
    return posts_username


def get_comments_by_post_id(post_id):
    all_comments = get_all_comments()
    comments = []
    for comment in all_comments:
        if comment["post_id"] == post_id:
            comments.append(comment)
    return comments

def search_for_posts(query):
    all_post = get_posts_all()
    search_posts = []
    for post in all_post:
        siring = strip_punctuation_ru(post["content"])
        if query.lower() in siring.lower().split():
            search_posts.append(post)
    return search_posts




def get_post_by_pk(pk):
    all_post = get_posts_all()
    for post in all_post:
        if post["pk"] == pk:
            return post


def strip_punctuation_ru(string):
    punctuations = '''!()—[]{};:'"\,<>./?@#$%^&*_~'''
    new_string = ""
    for char in string:
        if char in punctuations:
            new_string += ' '
        else:
            new_string += char
    new_string = new_string.replace(" - ", " ")
    return " ".join(new_string.split())

