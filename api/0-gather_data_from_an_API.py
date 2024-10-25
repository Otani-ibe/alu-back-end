#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys


def main():
    """Main function to retrieve and display employee TODO list progress"""
    # Ensure employee ID is passed and is an integer
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Please provide a valid employee ID.")
        return
    
    user_id = int(sys.argv[1])

    # Define the API endpoints
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        return
    
    user_name = user_response.json().get('name')

    # Fetch TODO list and filter by user ID
    response = requests.get(todo_url)
    todos = response.json()
    total_tasks = sum(1 for todo in todos if todo['userId'] == user_id)
    completed_tasks = [todo['title'] for todo in todos if todo['userId'] == user_id and todo['completed']]

    # Display the required output
    print(f"Employee {user_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == '__main__':
    main()

