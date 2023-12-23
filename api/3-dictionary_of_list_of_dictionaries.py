#!/usr/bin/python3
"""
This Python script fetches data from the JSONPlaceholder
 API, specifically the "todos" and "users" endpoints. 
 It retrieves a list of tasks (TODOS) and a list of 
 users (USERS) from the JSONPlaceholder API. Then, it processes 
 this data to create a new JSON file named "todo_all_employees.json."

The resulting JSON file contains information 
about tasks assigned to 
each user, including the user's username, 
the task title, and whether the task is completed. 
The structure of the output JSON file is organized 
by user ID, with each user having a list of 
tasks associated with them. The script uses the requests 
library to make API requests and the json library to 
handle JSON data.
"""
import json
import requests

ROOT_URL = "https://jsonplaceholder.typicode.com/"

TODOS = requests.get(f'{ROOT_URL}todos/').json()
USERS = requests.get(f'{ROOT_URL}users/').json()

if __name__ == "__main__":
    with open("todo_all_employees.json", "w") as output_file:
        result = {
            user['id']: [
                {
                    'username': user['username'],
                    'task': task['title'],
                    'completed': task['completed']
                }
                for task in TODOS
                if task['userId'] == user['id']
            ]
            for user in USERS
        }

        json.dump(result, output_file)