import os
import csv
from tabulate import tabulate


def clear_console():
    # Check os for correct console command
    if os.name == "nt":
        os.sytem("cls")
    else:
        os.system("clear")


class User:
    pass


class Task:
    def __init__(self, id, name, description, hours, datestamp):

        # Task attributes
        self.id = id
        self.name = name
        self.description = description
        self.hours = hours
        self.datestamp = datestamp

    def display_info(self):
        # Create list for table headers
        headers = ["ID", "Name", "Description", "Hours", "Timestamp"]
        # Create list for table row data
        data = [[self.id, self.name, self.description, self.hours, self.datestamp]]
        # Print table to console
        print("TASK INFORMATION")
        print(tabulate(data, headers, tablefmt="grid"))


class TaskManager:
    def __ini__(self):

        self.tasks = []

    def initialize_system(self):
        pass

    def save_record(self):
        pass

    def add_task(self):
        pass

    def edit_task(self):
        pass

    def view_task(self):
        pass

    def view_days_tasks(self):
        pass

    def view_weeks_tasks(self):
        pass

    def view_months_tasks(self):
        pass

    def view_tasks_by_date_range(self):
        pass


def run_program():
    pass


new_task = Task(1, "New Task", "This is my new task", 1, "14/10/2024")
new_task.display_info()
