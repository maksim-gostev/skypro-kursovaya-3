def tag_replace(posts: list[dict]) -> list[dict]:
    if type(posts) == list:
        for post in posts:
            content = post['content'].split()
            for tag_words in content:
                if tag_words[0] == '#':
                    words = tag_words.replace('#', '')
                    post['content'] = post['content'].replace(tag_words,
                                                              f'<a href="/tag/{words}">{tag_words}</a>')
        return posts
    elif type(posts) == dict:
        content = posts['content'].split()
        for tag_words in content:
            if tag_words[0] == '#':
                posts['content'] = posts['content'].replace(tag_words, f'<a href="/tag/{tag_words[1, len(tag_words)]}">{tag_words}</a>')
                print(posts['content'])
        return posts
    else:
        return False