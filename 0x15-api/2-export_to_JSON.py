#!/usr/bin/python3
"""
This script uses REST API for a given employee ID,
returns information about his/her TODO list progress
and exports the task data to a JSON file.
"""

import requests
import sys
import json


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

    # Structure data for JSON export
    tasks_list = []
    for task in todos_response:
        task_dictionary = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
        }
        tasks_list.append(task_dictionary)

    tasks_json = {employee_id: tasks_list}

    # File to save the tasks in JSON format
    file_name = f"{employee_id}.json"

    with open(file_name, mode='w') as file:
        json.dump(tasks_json, file)

    print("""Tasks for employee ID {} have been saved to {}"""
          .format(employee_id, file_name))
