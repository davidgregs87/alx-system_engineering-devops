#!/usr/bin/python3
"""A script to export to a csv file"""

import csv
import requests
import sys

url = 'https://jsonplaceholder.typicode.com'
if __name__ == '__main__':
    user_id = sys.argv[1]
    emp_url = requests.get(f"{url}/users/{user_id}").json()
    todo_url = requests.get(f"{url}/todos", params={"userId": user_id}).json()
    emp_uname = emp_url.get('username')

    with open(f"{user_id}.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todo_url:
            writer.writerow([user_id, emp_uname,
                             t.get("completed"), t.get("title")])
