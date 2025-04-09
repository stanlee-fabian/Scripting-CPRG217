'''
Script that outputs "Project_2_WriteData.py" with proper heading and formatting.  

Reference: Lecture with Mr. Marcel Tozser

Stanlee, Warren, Tim, Roed, Nelvic
CRPG-217-D JUNE 2024
'''

import json

# Formatting Line
LINE = ("================================================")

# Function to read and print data from .json file
def print_data():
    # Reads 'Project_2.json' 
    with open('Project_2.json', 'r') as json_file:
        # Loads file to a Python dictionary
        data = json.load(json_file)

    # Print the machine name
    print(f"Machine Name: {data['machine_name']}")
    print(LINE)
    print()

    # Print the users and their groups
    print("Users and Groups:")
    print(LINE)
    for user in data['users_and_groups']:
        print(f"{user[0]}:")  # Print the username
        for group in user[1]:
            print(f"  {group}")  # Print each group
        print()

    # Print CPU information
    print("CPU Information:")
    print(LINE)
    for key, value in data['cpu_info'].items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print()

    # Print services status
    print("Services Status:")
    print(LINE)
    for service in data['services_status']:
        print(f"Service: {service['name']}, Status: {service['status']}")
    print()

if __name__ == "__main__":
    print_data()