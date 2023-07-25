#!/usr/bin/python3
"""This script returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_dict = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo_dict = requests.get(url + "todos",
                             params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in
                 todo_dict if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_dict.get("name"), len(completed), len(todo_dict)))
    [print("\t {}".format(c)) for c in completed]
