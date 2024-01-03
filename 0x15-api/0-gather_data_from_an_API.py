#!/usr/bin/python3
"""
    Using REST API, returns information about TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed_task = [i.get(
        "title") for i in todo if i.get(
            "completed_task") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        users.get("name"), len(completed), len(todo)))
    [print("i {}".format(c)) for c in completed_task]
