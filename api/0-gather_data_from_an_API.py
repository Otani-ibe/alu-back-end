#!/usr/bin/python3
"""
This module fetches and displays the TODO list progress for a given employee ID
from a public API. It retrieves employee data and their associated tasks, 
calculating the number of completed tasks and displaying them in a formatted output.

"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Parameters:
    employee_id (int): The ID of the employee whose TODO list is to be fetched.

    Returns:
    None: Prints the employee's TODO list progress to standard output.
    """
    # API endpoints
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch employee data
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("Employee not found.")
        return

    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch TODOs data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate completed and total tasks
    completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    # Print the results in the required format
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    # Check if the script is run with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        # Convert the employee ID from command line argument to an integer
        employee_id = int(sys.argv[1])
        fetch_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for employee ID.")
