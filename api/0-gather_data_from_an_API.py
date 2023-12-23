#!/usr/bin/python3
"""
This script interacts with the APIs
at https://jsonplaceholder.typicode.com/
and gets info about the users'
to-do lists and which tasks have they completed.
"""
import requests

if __name__ == "__main__":
    from sys import argv

    EMPLOYEE_ID = int(argv[1])

    ROOT_URL = "https://jsonplaceholder.typicode.com/"

    TODOS = requests.get(f'{ROOT_URL}todos/').json()
    EMPLOYEE_NAMES = requests.get(f'{ROOT_URL}users/').json()

    EMPLOYEE_NAME = EMPLOYEE_NAMES[EMPLOYEE_ID - 1]['name']

    EMPLOYEE_TODOS = tuple(
        task
        for task in TODOS
        if task['userId'] == EMPLOYEE_ID
    )
    TOTAL_NUMBER_OF_TASKS = len(EMPLOYEE_TODOS)

    DONE_TASKS_TITLES = tuple(
        task['title']
        for task in EMPLOYEE_TODOS
        if task['completed'] is True
    )
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS_TITLES)

    print(f"Employee {EMPLOYEE_NAME} is done with\
 tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    for task_title in DONE_TASKS_TITLES:
        print(f"\t {task_title}")