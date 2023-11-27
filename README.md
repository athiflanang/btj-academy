# Tugas Virtual Machine (28 Nov 2023)

# Simple Task
- Buatlah image dari aplikasi sederhana yang sudah dibuat
- Jalankan image tersebut sebagai container dan berjalan pada port 8081
- Berapakah IP docker container  **whoami**?
- Apa isi dari file yang tersembunyi dari docker container  **whoami**? Clue: Volume Mounting
- Image apa yang digunakan pada docker container  **whoami**?

## Answer 1

**Buatlah image dari aplikasi sederhana yang sudah dibuat**

### SSH to VM
`ssh athiflananguntoro@btj-academy.bangunindo.io`

### Clone Github

    git clone https://github.com/athiflanang/btj-academy.git

### Create Docker File

    athiflananguntoro@btj-academy:~/btj-academy$ nano Dockerfile
- input inside Docker File

> FROM python:3
WORKDIR /app;
COPY programsimple.py /app/;
EXPOSE 8081;
CMD ["python", "programsimple.py";

### Run

    docker build -t my-python-app .

## Answer 2

**Jalankan image tersebut sebagai container dan berjalan pada port 8081**

### Run Docker File with Port 8081

    docker run -d -p 8081:8081 --name athif my-python-app

### Check If Run Properly

    docker ps -a
    
### Output

> my-python-app athif

## Answer 3

**Berapakah IP docker container  *whoami* ?**

### Check IP Using Docker Inspect

    docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' whoami

### Output

> (172.17.0.2)

## Answer 4
**Apa isi dari file yang tersembunyi dari docker container *whoami* ?**

### Use Volume Mounting with Docker Inspect

    docker inspect -f '{{json .Mounts}}' whoami
### Output

> [{"Type":"bind","Source":"/home/local/.docker","Destination":"/tmp/system","Mode":"","RW":true,"Propagation":"rprivate"}]

### Explore inside whoami To Find Hidden File

    docker exec -it whoami /bin/sh -c 'ls /tmp/system'
### Output

> whoami

### Display Content

    docker exec -it whoami cat /tmp/system/whoami
### Output

> Oofooni1eeb9aengol3feekiph6fieve

## Answer 5

**Image apa yang digunakan pada docker container *whoami* ?**

### Use Docker Inspect with Config Image

    docker inspect -f '{{.Config.Image}}' whoami
### Output

> secret:aequaix9De6dii1ay4HeeWai2obie6Ei
