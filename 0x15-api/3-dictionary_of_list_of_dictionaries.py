#!/usr/bin/python3
"""Python script to export data in the JSON format."""


API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    import json
    import requests

    users = requests.get("{}/users".format(API_URL)).json()
    todos = requests.get('{}/todos'.format(API_URL)).json()
    all_todos = {}

    for user in users:
        task_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                task_list.append(task_dict)
        all_todos[user.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(all_todos, file)
