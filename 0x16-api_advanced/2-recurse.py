#!/usr/bin/python3
'''recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
'''


def recurse(subreddit, hot_list=[], n=0, after=None):
    '''Retrieves a list of hot posts from a given subreddit.
    '''
    import requests

    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    sort_param = 'hot'
    limit = 30
    res = requests.get(
        'https://www.reddit.com/r/{}/.json?sort={}&limit={}&count='
        '{}&after={}'.format(
            subreddit,
            sort_param,
            limit,
            n,
            after if after else ''
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        data = res.json()['data']
        posts = data['children']
        count = len(posts)
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))
        if count >= limit and data['after']:
            return recurse(subreddit, hot_list, n + count, data['after'])
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
