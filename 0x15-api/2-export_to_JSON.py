#!/usr/bin/python3
"""A script to export to a json file"""

import json
import requests
import sys

url = 'https://jsonplaceholder.typicode.com'
if __name__ == '__main__':
    user_id = sys.argv[1]
    emp_url = requests.get(f"{url}/users/{user_id}").json()
    todo_url = requests.get(f"{url}/todos", params={"userId": user_id}).json()
    emp_uname = emp_url.get('username')

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump({user_id: [{"text": t.get('title'),
                              "completed": t.get("completed"),
                              "username": emp_uname} for t in todo_url]},
                  jsonfile)
