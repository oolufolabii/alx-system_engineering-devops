#!/usr/bin/python3
'''A python script for an employee, returns information
about his/her To-do list progress.
'''

if __name__ == "__main__":

    import re
    import requests
    import sys

    API_URL = 'https://jsonplaceholder.typicode.com'

    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            user_id = int(sys.argv[1])

        user = requests.get('{}/users/{}'.format(API_URL, user_id)).json()
        name = user.get('name')
        todos_req = requests.get('{}/todos'.format(API_URL)).json()

        todos = list(filter(lambda x: x.get('userId') == id, todos_req))
        todos_done = list(filter(lambda x: x.get('completed'), todos))
        print(
            'Employee {} is done with tasks({}/{}):'.format(
                name,
                len(todos_done),
                len(todos)
            )
        )
        for todo_done in todos_done:
            print('\t {}'.format(todo_done.get('title')))
