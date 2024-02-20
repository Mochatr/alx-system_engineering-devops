#!/usr/bin/python3
"""
This script uses REST API for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    base_api_url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    # Fetch user information
    user_info_url = "{}users/{}".format(base_api_url, employee_id)
    user_info_response = requests.get(user_info_url).json()
    username = user_info_response.get("username")

    # Fetch TODOs for the user
    todos_url = "{}todos?userId={}".format(base_api_url, employee_id)
    todos_response = requests.get(todos_url).json()

    # File to save the tasks in CSV format
    file_name = f"{employee_id}.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos_response:
            writer.writerow([employee_id, username, task.get("completed"),
                             task.get("title")])

    print("""Tasks for employee ID {} have been saved to {}"""
          .format(employee_id, file_name))
