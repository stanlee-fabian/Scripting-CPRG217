'''
Pseudo code for TripWire.py
Stanlee, Warren, Tim, Roed, Nelvic
CRPG-217-D MAY 2024

Import the necessary modules
(hashlib, sys, os)

Constants for folder path and record file
FOLDER_PAtH = path_to_your_folder
RECORD_FILE = tripwire_record

Function to get file list
Execute a command to list files in the give folder path
Read and output into lines
Return the list of file names

Function gethash(filename)
Constructs the full file path with file name and folder path
Try
    to open file and read the file data then close it
Except
    Prints an error message if it cannot be read and returns none

Calculates the md5 hash
Returns the hash results from calculations
Function to write in the record file
Try
    Opens the record file in write mode
    Write the folder path to the record file
    For each file name in the file list
        Get the has results
    If the has result is not none
        write the file name and has result into the record file
    Close record file
Except
    Print error message if the file cannot be written
    Print message that record has been successfully created

Function create table
Try
    open the record file in read
    read and organize file data into lines
    close file
Except
    print error message that file cannot be read
    return empty lists for old file list and record table
    record table as empty list
    first line as true
    For each line in data
        If first line true
        Set first line to false
Else
Separate lines into components
Add it to record table
old file list as a list of first elements from each row in record table
Return the old file list and record table

Function to sort the files into buckets (arrays). Missing, added, and possibly modified
Missing files and possibly modified are empty lists
Get current list of files in folder
Get old file list and record table from record files
For each file name in old file list
    if the filename is in current file list
        add file name to possibly modified
        remove file name from current files list
else
    add file name to missing files
Set added files to remaining items in current file list
Return missing files, added files, possibly modified and record table

Function to check if files have been touched/modified
Modified file as an empty list
For each file name in possibly modified
for each row in record table
    if file name matched first element of row
        if the stored hash doesnt match current hash
            add file name to modified files
            break
    Return modified files

Function for getting folder path from record files
Try
    open the record file in read mode
    read and separate the file data in lines
    close the record file
Except
    print error message if the file cannot be read
    return none
    Return the first line of data as folder path
Set the arglist in the list of command line arguments
If the number of arguments is 3

Part 1 is create record files
Set folder path to the second argument
Set the record file to the third argument
Get the list of files in folder
Write the record file
Else

Part 2 is check the file system intergrity
Set record file to the second argument
Get the folder path from the record file
If the folder path is none
Get the missing, added, and possibly modified file and the record tabl
Get the list of modified files
Print the missing, added and modified files as a list
'''

import hashlib, sys, os

# Constants for folder path and the record file name
FOLDER_PATH = "home/stanlee/testfolder"
RECORD_FILE = "TripwireRecord.txt"

# Function to get the list of files in the specified folder
def GetFileList():
    fileList = os.popen("ls" + FOLDER_PATH).read().splitlines()
    return fileList

# Function to get the hash of a file
def GetHash(fileName):
    filePath = FOLDER_PATH + "/" + fileName
    try:
        with open(filePath, 'rb') as refFile:
            data = refFile.read()
    except:
        print("Could not read the file:", filePath)
        return None
    hashResult = hashlib.md5(data).hexdigest()
    return hashResult

# Function to write the record file
def WriteRecordFile():
    try:
        with open(RECORD_FILE, 'w') as refFile:
            refFile.write(FOLDER_PATH + '\n')
            for fileName in fileList:
                hashResult = GetHash(fileName)
                if hashResult:
                    refFile.write(fileName + " " + hashResult + '\n')
    except:
        print("Could not write to record file!")
    print("The record has been created!")

# Function to create a table from the record file
def CreateTable():
    try:
        with open(RECORD_FILE, 'r') as refFile:
            data = refFile.read().splitlines()
    except:
        print("Could not read the record!")
        return [], []
    
    recordTable = []
    firstLine = True
    for line in data:
        if firstLine:
            firstLine = False
        else:
            splitLine = line.split()
            recordTable.append(splitLine)
    
    oldFileList = [row[0] for row in recordTable]
    return oldFileList, recordTable

# Function to sort files into buckets: missing, added, and possibly modified
def SortBuckets():
    missingFiles = []
    possiblyModified = []
    currentFileList = GetFileList()
    oldFileList, recordTable = CreateTable()
    
    for fileName in oldFileList:
        if fileName in currentFileList:
            possiblyModified.append(fileName)
            currentFileList.remove(fileName)
        else:
            missingFiles.append(fileName)
    
    addedFiles = currentFileList
    return missingFiles, addedFiles, possiblyModified, recordTable

# Function to check if files have been modified
def CheckIfModified():
    modifiedFiles = []
    for fileName in possiblyModified:
        for row in recordTable:
            if fileName == row[0]:
                if row[1] != GetHash(fileName):
                    modifiedFiles.append(fileName)
                break
    return modifiedFiles

# Function to get the folder path from the record file
def GetFolderPath():
    try:
        with open(RECORD_FILE, 'r') as refFile:
            data = refFile.read().splitlines()
    except:
        print("Could not read record file!")
        return None
    return data[0]

# MAIN
argList = sys.argv

if len(argList) == 3:
    # PART 1: Create record file
    FOLDER_PATH = argList[1]
    RECORD_FILE = argList[2]
    # Get the list of files in the folder
    fileList = GetFileList()
    # Write the record file with file names and their hashes
    WriteRecordFile()
else:
    # PART 2: Check file system integrity
    RECORD_FILE = argList[1]
    FOLDER_PATH = GetFolderPath()
    if FOLDER_PATH:
        # Sorts the files into missing, added, and possibly modified categories
        missingFiles, addedFiles, possiblyModified, recordTable = SortBuckets()
        modifiedFiles = CheckIfModified()
        # Prints the lists of missing, added, and modified files
        print("Missing files list:", missingFiles)
        print("Added files list:", addedFiles)
        print("Modified file list:", modifiedFiles)
