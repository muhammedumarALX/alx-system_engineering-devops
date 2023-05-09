#!/usr/bin/python3
"""script to gather data from an API"""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(sys.argv[1])
    user_endpoint = "{}users/{}".format(base_url, employee_id)
    user = requests.get(user_endpoint).json()
    employee_name = user["name"]

    todo_endpoint = "{}todos?userId={}".format(base_url, employee_id)
    todo_list = requests.get(todo_endpoint).json()

    completed_task = [task for task in todo_list if task["completed"]]
    completed = len(completed_task)
    total = len(todo_list)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed, total))
    for task in completed_task:
        print("\t {}".format(task["title"]))
