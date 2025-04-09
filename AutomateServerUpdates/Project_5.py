'''
A script that runs ansible configuration through servers. Automating server updates 

References:
In-class Lab with Mr. Marcel, https://www.linkedin.com/learning/red-hat-certified-engineer-ex294-cert-prep-1-foundations-of-ansible/ansible-concepts?autoAdvance=true&autoSkip=false&autoplay=true&resume=true&u=2245281),
https://docs.python.org/3/library/subprocess.html, https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html

CPRG-217-D August 2024
Stanlee Fabian
Tim Matsevich 
Martin Sy
Warren Peng
Roed Lanada
John Patron
'''

import subprocess

def run_playbook():
    command = ["ansible-playbook", "-i", "inventory", "Paybook_1.yml"]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("An error occurred:", result.stderr)

if __name__ == "__main__":
    run_playbook()
