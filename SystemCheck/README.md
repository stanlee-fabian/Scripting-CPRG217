# SystemCheck

## Description

This repository contains the `SystemCheck` script developed as part of the CPRG-217 course. The course introduced us to computer system scripting concepts and techniques. Through this project, we gained competencies in:

- **Collecting, sorting, and filtering data**: The script lists files in a specified folder, calculates their hashes, and records them for future integrity checks. <br>
- **Producing a script with basic functionality**: We created functions to list files, calculate hashes, write records, and check file integrity. <br>
- **Demonstrating error handling techniques**: The script includes error handling for file reading and writing operations.<br>
- **Applying data types to process and organize data**: We used lists and tables to manage file data and hashes.<br>
- **Creating tools to standardize and script system tasks**: The script automates the process of monitoring file changes in a folder.<br>

Additionally, we learned how to use programming languages like Python in conjunction with IT platforms like Ansible. This project reflects the needs of the industry by providing a practical tool for file integrity monitoring.

## Usage

### Part 1: Create Record File

To create a record file, run the script with the folder path and record file name as arguments:<br>
python SystemCheck.py /path/to/your/folder TripwireRecord.txt

### Part 2: Check File System Integrity
To check the file system integrity, run the script with the record file name as an argument:<br>
python SystemCheck.py TripwireRecord.txt

The script will output lists of missing, added, and modified files.

## Functions
GetFileList(): Lists files in the specified folder. <br>
GetHash(fileName): Calculates the MD5 hash of a file.<br>
WriteRecordFile(): Writes the folder path and file hashes to the record file.<br>
CreateTable(): Reads the record file and organizes data into a table.<br>
SortBuckets(): Sorts files into missing, added, and possibly modified categories.<br>
CheckIfModified(): Checks if files have been modified based on their hashes.<br>
GetFolderPath(): Retrieves the folder path from the record file.<br>

## Error Handling
The script includes error handling for file reading and writing operations, ensuring robustness and reliability.
