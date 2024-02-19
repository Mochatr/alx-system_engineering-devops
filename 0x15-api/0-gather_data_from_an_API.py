#!/usr/bin/python3
"""
This script uses REST API for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    base_api_url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    # Fetch user information
    user_info_url = "{}users/{}".format(base_api_url, employee_id)
    user_info_response = requests.get(user_info_url).json()

    # Fetch TODOs for the user
    todos_url = "{}todos?userId={}".format(base_api_url, employee_id)
    todos_response = requests.get(todos_url).json()

    # Filter completed TODO tasks
    completed_todos = [todo for todo in todos_response
                       if todo.get("completed") is True]

    # Display the progress
    print("Employee {} is done with tasks({}/{}):"
          .format(user_info_response.get("name"),
                  len(completed_todos),
                  len(todos_response)))

    # Print titles of completed tasks
    for todo in completed_todos:
        print("\t {}".format(todo.get("title")))
