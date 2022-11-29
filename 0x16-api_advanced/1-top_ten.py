#!/usr/bin/python3
'''function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
'''


def top_ten(subreddit):
    '''Retrieves the title of the top ten posts from a given subreddit.
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
    sort_param = 'top'
    limit = 10
    res = requests.get(
        'https://www.reddit.com/r/{}/.json?sort={}&limit={}'.format(
            subreddit,
            sort_param,
            limit
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        for post in res.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
