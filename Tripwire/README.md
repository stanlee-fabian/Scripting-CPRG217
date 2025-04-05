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
python TripWire.py /path/to/your/folder TripwireRecord.txt

### Part 2: Check File System Integrity
To check the file system integrity, run the script with the record file name as an argument:
python TripWire.py TripwireRecord.txt

The script will output lists of missing, added, and modified files.

## Functions
GetFileList(): Lists files in the specified folder.
GetHash(fileName): Calculates the MD5 hash of a file.
WriteRecordFile(): Writes the folder path and file hashes to the record file.
CreateTable(): Reads the record file and organizes data into a table.
SortBuckets(): Sorts files into missing, added, and possibly modified categories.
CheckIfModified(): Checks if files have been modified based on their hashes.
GetFolderPath(): Retrieves the folder path from the record file.
Error Handling
The script includes error handling for file reading and writing operations, ensuring robustness and reliability.
