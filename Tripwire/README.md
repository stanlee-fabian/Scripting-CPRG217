# TripWire.py

## Description

This script, `TripWire.py`, was developed as part of the CRPG-217-D course in May 2024 by Stanlee, Warren, Tim, Roed, and Nelvic. The course introduced us to computer system scripting concepts and techniques. Through this project, we gained competencies in:

- **Collecting, sorting, and filtering data**: The script lists files in a specified folder, calculates their hashes, and records them for future integrity checks.
- **Producing a script with basic functionality**: We created functions to list files, calculate hashes, write records, and check file integrity.
- **Demonstrating error handling techniques**: The script includes error handling for file reading and writing operations.
- **Applying data types to process and organize data**: We used lists and tables to manage file data and hashes.
- **Creating tools to standardize and script system tasks**: The script automates the process of monitoring file changes in a folder.

Additionally, we learned how to use programming languages like Python in conjunction with IT platforms like Ansible. This project reflects the needs of the industry by providing a practical tool for file integrity monitoring.

## Usage
### Part 1: Create Record File

To create a record file, run the script with the folder path and record file name as arguments:

```bash
python TripWire.py /path/to/your/folder TripwireRecord.txt
