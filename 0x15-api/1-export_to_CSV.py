#!/usr/bin/python3
"""Python script to export data in the CSV format."""

import re
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            user_id = int(sys.argv[1])
            user_request = requests.get('{}/users/{}'.format(API_URL, user_id)).json()
            todos_request = requests.get('{}/todos'.format(API_URL)).json()
            user_name = user_request.get('username')
            todos = list(filter(lambda x: x.get('userId') == user_id, todos_request))
            with open('{}.csv'.format(user_id), 'w') as file:
                for todo in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            user_id,
                            user_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
