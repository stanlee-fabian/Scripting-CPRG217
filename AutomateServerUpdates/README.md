# AutomateServerUpdates

## Description

This repository contains the `AutomateServerUpdates` script developed as part of the CPRG-217 course. The course introduced us to computer system scripting concepts and techniques. Through this project, we gained competencies in:

- **Automating server updates**: The script is designed to streamline the process of updating servers, ensuring they are always running the latest software versions. <br>
- **Producing a script with basic functionality**: We created functions to check for updates, download and install them, and verify the update status.<br>
- **Demonstrating error handling techniques**: The script includes error handling for network issues, download failures, and installation errors.<br>
- **Applying data types to process and organize data**: We used lists and dictionaries to manage update information and server statuses.<br>
- **Creating tools to standardize and script system tasks**: The script automates routine server maintenance tasks, reducing manual intervention and improving efficiency.<br>

Additionally, we learned how to use programming languages like Python in conjunction with IT platforms like Ansible. This project reflects the needs of the industry by providing a practical tool for server maintenance and updates.

## Usage

### Check for Updates

To check for available updates, run the script with the appropriate command:<br>
python AutomateServerUpdates.py check<br>

### Download and Install Updates
To download and install updates, run the script with the appropriate command:<br>
python AutomateServerUpdates.py update<br>

### Verify Update Status
To verify the status of the updates, run the script with the appropriate command:<br>
python AutomateServerUpdates.py status<br>

## Functions
CheckForUpdates(): Checks for available updates for the server.<br>
DownloadUpdates(): Downloads the updates from the specified source.<br>
InstallUpdates(): Installs the downloaded updates on the server.<br>
VerifyUpdateStatus(): Verifies the status of the updates after installation.<br>

## Error Handling
The script includes error handling for network issues, download failures, and installation errors, ensuring robustness and reliability.
