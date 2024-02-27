# REST API system users.

#### REST API developed with FastAPI, MySQL, SQLAchemy and ASGI Web Server: uvicorn

## Pre-requisities 📋

#### Make sure you have the _pip_ package management system installed.

```
pip --version
```

#### Create the database in MySQL in case you do not use docker

```
create database restapidb;
```

#### Clone project folder and then create virtual environment with [Anaconda](https://www.anaconda.com/download)

```
# Being located in the cloned project folder:

conda create --name NAME-VIRTUAL-ENVIROMENT python=3
```

## Installation 🔧

#### Install all project dependencies

```
pip install -r requirements.txt
```

## Docker 🐳

#### Create the containers (services) that are described in the docker-compose file.

```
docker compose up
```

## Start app 🚀

#### Start the application with the next command and then you can use to the integrated [FastAPI swagger](https://fastapi.tiangolo.com/features/), Postman, or another to use the REST API

```
python app.py
```

## Documentation

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Anaconda](https://docs.anaconda.com/free/anaconda/configurations/switch-environment/)
- [Uvicorn](https://www.uvicorn.org/)
