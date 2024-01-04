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

    completed_task = [t.get(
        "title") for t in todos if t.get(
            "completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        users.get("name"), len(completed_task), len(todos)))
    [print("\t {}".format(c)) for c in completed_task]
