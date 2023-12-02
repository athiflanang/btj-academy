# Tugas Virtual Machine 3 (2 Dec 2023)

# Simple Task 3
- Pada example python app, tambahkan beberapa routing kemudian custom port yang di listen
- Buatlah satu playbook dengan beberapa task yaitu :
  1) Menyalin file dari local ke server server btj-academy
  2) Build docker image untuk example python app
  3) Jalankan container yang sudah di build

## Answer 1

**Pada example python app, tambahkan beberapa routing kemudian custom port yang di listen**

### SSH to VM

    ssh athiflananguntoro@btj-academy.bangunindo.io

### Download python app and requirement text

    https://github.com/rrw-bangunindo/btj-academy/tree/main

### Add routing and custom port to python app
- Input inside Inventory
```
from flask import Flask
    
app = Flask(__name__)
    
@app.route('/')
def hello_world():
        return 'Hello, Virtual Machine!'
    
@app.route('/about')
def about():
        return 'About page.'
    
@app.route('/contact')
def contact():
	return 'Contact us at burner@email.com'

if __name__ == '__main__':
    	app.run(debug=True, host='0.0.0.0', port=9081)
```
### Clone github repository
    git clone https://github.com/athiflanang/btj-academy.git

## Answer 2

**Buatlah satu playbook dengan beberapa task yaitu ( 
	1. Menyalin file dari local ke server server btj-academy,
  	2. Build docker image untuk example python app,
  	3. Jalankan container yang sudah di build)**

### Create Docker file

    nano Deploy_Dockerfile
    
- Input inside Dockerfile
	```
	FROM python:3.8
	WORKDIR /app
	COPY . /app
	RUN pip install --no-cache-dir -r requirements.txt
	EXPOSE 8081
	CMD ["python", "examplepyapp.py"]
	```

### Run

    docker build -t deploy_image -f Deploy_Dockerfile /home/athiflananguntoro/btj-academy
    
### Create playbook (yaml)

    nano testplaybook.yaml

- Input inside Dockerfile

      name: Perform deployment tasks
      hosts: 10.184.0.100
      become: yes
    
      tasks:
          name: Copy file to server-deploy
          ansible.builtin.copy:
            src: /home/athiflananguntoro/btj-academy/examplepyapp.py #Pathing for examplepyapp
            dest: /home/athiflananguntoro #Pathing for copied server
    
          name: Build Docker image
          ansible.builtin.docker_image:
            name: deploy_image # Docker image name
            path: /home/athiflananguntoro/btj-academy/Deploy_Dockerfile #Pathing for docker image
            state: present
    
          name: Run the container
          ansible.builtin.docker_container:
            name: container_athif #Container name
            image: deploy_image #Docker image used
            state: started
            ports: "9084:9081" #Port

### Run

    ansible-playbook -i "10.184.0.100," testplaybook.yaml

### Output

    PLAY [Perform deployment tasks] *****************************************************************************************************
    
    TASK [Gathering Facts] **************************************************************************************************************
    ok: [10.184.0.100]
    
    TASK [Copy file to server-deploy] ***************************************************************************************************
    ok: [10.184.0.100]
    
    TASK [Build Docker image] ***********************************************************************************************************
    ok: [10.184.0.100]
    
    TASK [Run the container] ************************************************************************************************************
    changed: [10.184.0.100]
    
    PLAY RECAP **************************************************************************************************************************
    10.184.0.100               : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

