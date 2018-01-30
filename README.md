1. Create Project Root Dir
2. Create requirements.txt
3. Create Dockerfile
4. Create docker-compose.yml
5. Setup Django Project
```
$ docker-compose run web django-admin.py startproject src/my_project ./src 
```
6. ADD . /code/  




## Create Docker-Machine

```
docker-machine create -d virtualbox default
```

## View env of Docker-Machine

```
docker-machine env default
```


## Manage Docker-Machine

```
docker-machine start <MachineName>

docker-machine stop <MachineName>

docker-machine rm <MachineName>

```


## Check status of Docker-Machine

```
docker-machine status default
```