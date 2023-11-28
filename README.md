# Tugas Virtual Machine 2 (28 Nov 2023)

# Simple Task 2
- Buatlah sebuah inventory, pada inventory tersebut mendefinisikan daftar variables dan hosts
- Buatlah satu playbook dengan task menjalankan sebuah docker container dengan kriteria yaitu terdapat image, port dan environment variables

## Answer 1

**Buatlah sebuah inventory, pada inventory tersebut mendefinisikan daftar variables dan hosts**

### SSH to VM

    ssh athiflananguntoro@btj-academy.bangunindo.io

### Make Inventory

    sudo nano inventory_athif

- Input inside Inventory

> [mentor_vm]
mentor ansible_host=10.184.0.100 ansible_user=athiflananguntoro db_port=3306
> 
> [group_name1] host1 ansible_host=10.184.0.100 ansible_user=athiflananguntoro variable1=value1 variable2=value2
> 
> [group_name2] host2 ansible_host=10.184.0.100 ansible_user=athiflananguntoro variable3=value3 variable4=value4

### Run

    ansible-inventory -i inventory_athif --list

### Output

     {
        "_meta": {
            "hostvars": {
                "host1": {
                    "ansible_host": "10.184.0.100",
                    "ansible_user": "athiflananguntoro",
                    "variable1": "value1",
                    "variable2": "value2"
                },
                "host2": {
                    "ansible_host": "10.184.0.100",
                    "ansible_user": "athiflananguntoro",
                    "variable3": "value3",
                    "variable4": "value4"
                },
                "mentor": {
                    "ansible_host": "10.184.0.100",
                    "ansible_user": "athiflananguntoro",
                    "db_port": 3306
                }
            }
        },
        "all": {
            "children": [
                "group_name1",
                "group_name2",
                "mentor_vm",
                "ungrouped"
            ]
        },
        "group_name1": {
            "hosts": [
                "host1"
            ]
        },
        "group_name2": {
            "hosts": [
                "host2"
            ]
        },
        "mentor_vm": {
            "hosts": [
                "mentor"
            ]
        }
    }
## Answer 2

**Buatlah satu playbook dengan task menjalankan sebuah docker container dengan kriteria yaitu terdapat image, port dan environment variables**

### Make Docker Container

    nano run_docker_container.yml
    
- Input inside Container
```
name: Run Docker Container
hosts: mentor_vm
become: true
tasks:
  name: Run Docker Container
  docker_container:
  name: my_postgres_container 
  image: postgres:latest
  ports: 
  "5432:5432"
    env: 
      POSTGRES_DB: "database_athif"
      POSTGRES_USER: "admin" 
      POSTGRES_PASSWORD: "secretpassword" 
    state: started
```
### Get Public Key

    scp C:\Users\TUF\.ssh\id_rsa athiflananguntoro@btj-academy.bangunindo.io:/home/athiflananguntoro/.ssh/id_rsa
    
### Change id_rsa Permission

    chmod 400 /home/athiflananguntoro/.ssh/id_rsa

### Run

    ansible-playbook -i /home/athiflananguntoro/inventory_athif /home/athiflananguntoro/run_docker_container.yml
   
### Output

    PLAY [Run Docker Container] *********************************************************************************************************
     
     TASK [Gathering Facts]
     ************************************************************************************************************** 
     ok: [mentor]
     
     TASK [Run Docker Container]
     ********************************************************************************************************* 
     changed: [mentor]
     
     PLAY RECAP
     ************************************************************************************************************************** 
     mentor                     : ok=2    changed=1    unreachable=0   failed=0    skipped=0    rescued=0    ignored=0
