#!/usr/bin/python3
"""A python script to gather data from an API"""
import requests
import sys

api = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    try:
        emp_id = int(sys.argv[1])
        emp_url = requests.get("{}/users/{}".format(api, emp_id))
        todo_url = requests.get("{}/todos".format(api)).json()
        emp_name = emp_url.json().get('name')
        done_todo = []
        undone_todo = []
        for items in todo_url:
            if items["userId"] == emp_id:
                if items["completed"]:
                    done_todo.append(items['title'])
                else:
                    undone_todo.append(items['title'])
        done = len(done_todo)
        undone = len(undone_todo)
        print("Employee {} is done with tasks({}/{}):"
              .format(emp_name, done, done+undone))
        for line in done_todo:
            print(f"\t "+line)
    except Exception:
        pass
