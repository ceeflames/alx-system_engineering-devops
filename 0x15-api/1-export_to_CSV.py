#!/usr/bin/python3
"""
    Export data in the CSV format
"""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writes = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerrow(
            [user_id, username, t.get("completed"), t.get("title")]
            ) for t in todo]
