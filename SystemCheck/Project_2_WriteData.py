'''
Script that retrieves;
Machine name,
List of all users and the group they are in (alphabetical),
Processor Info (/proc/cpuinfo),
Current status of all services on machine,
of a Linux machine and writes as "Project_2.json".

Reference: Lecture with Mr. Marcel Tozser, https://www.geeksforgeeks.org/python-string-startswith/, 
https://www.scaler.com/topics/startswith-in-python/, https://linuxhandbook.com/systemctl-check-service-status/

Stanlee, Warren, Tim, Roed, Nelvic
CRPG-217-D JUNE 2024
'''

import grp
import pwd
import json
import os
import subprocess

# Function to get the machine's hostname
def get_hostname():
    if os.path.exists('/etc/hostname'):
        with open('/etc/hostname', 'r') as f:
            hostname = f.read().strip()
        return hostname
    else:
        return "Error: Hostname not found."

# Function to get users and their groups
def get_users_and_groups():
    allrecordsarray = pwd.getpwall()
    allrecordstable = []

    for record in allrecordsarray:
        name = record.pw_name
        defaultgroupid = record.pw_gid
        defaultgrouprecord = grp.getgrgid(defaultgroupid)
        defaultgroupname = defaultgrouprecord.gr_name
        grouplistarray = [defaultgroupname]

        for grouprecord in grp.getgrall():
            if name in grouprecord.gr_mem:
                groupname = grouprecord.gr_name
                grouplistarray.append(groupname)

        allrecordstable.append([name, sorted(grouplistarray)])

#Alphabetical sorting
    sortedarray = sorted(allrecordstable, key=lambda record: record[0].lower())
    return sortedarray

# Function to get CPU information
def get_cpu_info():
    cpu_info = {}
    if os.path.exists('/proc/cpuinfo'):
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                if line.startswith('vendor_id'):
                    cpu_info['vendor_id'] = line.split(':')[1].strip()
                elif line.startswith('model'):
                    cpu_info['model'] = line.split(':')[1].strip()
                elif line.startswith('model name'):
                    cpu_info['model_name'] = line.split(':')[1].strip()
                elif line.startswith('cache size'):
                    cpu_info['cache_size'] = line.split(':')[1].strip()
    else:
        cpu_info = {"Error": "Unable to retrieve CPU info, /proc/cpuinfo not found."}
    return cpu_info

# Function to get services status 
def get_services_status():
    services_status = []
    try:
        output = subprocess.check_output(['systemctl', 'list-units', '--type=service', '--all', '--no-pager', '--no-legend'], text=True)
        for line in output.splitlines():
            parts = line.split()
            if len(parts) >= 4:
                service_name = parts[0]
                service_status = parts[3]
                services_status.append({"name": service_name, "status": service_status})
    except subprocess.CalledProcessError as e:
        services_status = [{"Error": f"Failed to retrieve service status: {e}."}]
    return services_status

# Main function to collect all data and write to a .json file
def main():
    data = {}
    data['machine_name'] = get_hostname()
    data['users_and_groups'] = get_users_and_groups()
    data['cpu_info'] = get_cpu_info()
    data['services_status'] = get_services_status()

    with open('Project_2.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    main()