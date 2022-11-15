#!/usr/bin/python3
"""Python script to export data in the JSON format."""


API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    import json
    import requests
    import sys

    users = requests.get("{}/users".format(API_URL)).json()
    todos = requests.get('{}/todos'.format(API_URL)).json()
    todoAll = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(todoAll, file)
