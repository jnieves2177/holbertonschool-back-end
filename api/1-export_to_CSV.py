#!/usr/bin/python3
"""
This script retrieves information from the JSONPlaceholder 
API and create a CSV file containing tasks related to a 
specific user.
"""
import csv
import requests

if __name__ == "__main__":
    from sys import argv

    USER_ID = int(argv[1])

    ROOT_URL = "https://jsonplaceholder.typicode.com/"

    TODOS = requests.get(f'{ROOT_URL}todos/').json()
    USERNAMES = requests.get(f'{ROOT_URL}users/').json()

    USERNAME = USERNAMES[USER_ID - 1]['username']

    USER_TASKS = tuple(
        task
        for task in TODOS
        if task['userId'] == USER_ID
    )

    with open(f"{USER_ID}.csv", "w") as output_file:
        csv_writer = csv.writer(output_file, quoting=1)

        for task in USER_TASKS:
            csv_writer.writerow(
                (
                    USER_ID,
                    USERNAME,
                    task['completed'],
                    task['title']
                )
            )