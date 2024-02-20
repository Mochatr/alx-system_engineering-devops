#!/usr/bin/python3
"""
This script uses REST API,
fetches and exports tasks data for all
employees to a JSON file named todo_all_employees.json
"""

import json
import requests


def fetch_and_export_all_tasks():
    base_api_url = "https://jsonplaceholder.typicode.com/"
    users_url = f"{base_api_url}users"
    users_response = requests.get(users_url).json()

    all_tasks = {}

    for user in users_response:
        user_id = user.get("id")
        username = user.get("username")

        todos_url = f"{base_api_url}todos?userId={user_id}"
        todos_response = requests.get(todos_url).json()

        user_tasks = []
        for task in todos_response:
            task_info = {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
            }
            user_tasks.append(task_info)

        all_tasks[str(user_id)] = user_tasks

    # Exports to JSON
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    fetch_and_export_all_tasks()
