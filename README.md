<div align="center">

<h3>
 User System - API
</h3>

![Python Badge](https://img.shields.io/badge/Python-090a15?logo=python)
![FastAPI Badge](https://img.shields.io/badge/FastAPI-000?logo=fastapi)
![GitHub issues](https://img.shields.io/github/issues/josueluque/rest-api)
![GitHub forks](https://img.shields.io/github/forks/josueluque/rest-api)
![GitHub PRs](https://img.shields.io/github/issues-pr/josueluque/rest-api)

</div>

## About the system

#### User system API developed with FastAPI, MySQL, SQLAchemy and ASGI Web Server: uvicorn

## Pre-requisities 📋

#### Make sure you have the _pip_ package management system installed.

```
pip --version
```

#### Create the database in MySQL in case you do not use docker

```
create database restapidb;
```

## Installation 🔧

```
# (RECOMMENDED) Create virtual environment with Anaconda 
conda create --name NAME-VIRTUAL-ENVIROMENT python=3

# Fork or clone this respository
git clone https://github.com/josueluque/rest-api.git

# Install all project dependencies
cd rest-api
pip install -r requirements.txt
```

## Docker 🐳
> [!IMPORTANT]
> Before executing the `docker compose` command run the `invoke generate-env` command to generate the env file
```
cd rest-api
invoke generate-env

docker compose up -d
```

## Start app 🚀

#### Start the application with the next command and then you can use to the integrated [FastAPI swagger](https://fastapi.tiangolo.com/features/), Postman, or another to use the REST API

```
python app.py
```

## Documentation

- [![FastAPI][fastapi-badge]][fastapi-url]
- [![SQLAlchemy][sqlalchemy-badge]][sqlalchemy-url]
- [![Anaconda][anaconda-badge]][anaconda-url]
- [![Docker][docker-badge]][docker-url]
- [![Uvicorn][uvicorn-badge]][uvicorn-url]

<!-- Variables -->

[fastapi-badge]: https://img.shields.io/badge/fastapi-000?style=for-the-badge&logo=fastapi
[fastapi-url]: https://fastapi.tiangolo.com/
[sqlalchemy-badge]: https://img.shields.io/badge/sqlalchemy-000?style=for-the-badge&logo=sqlalchemy
[sqlalchemy-url]: https://www.sqlalchemy.org/
[anaconda-badge]: https://img.shields.io/badge/anaconda-000?style=for-the-badge&logo=anaconda
[anaconda-url]: https://docs.anaconda.com/free/anaconda/configurations/switch-environment/
[docker-badge]: https://img.shields.io/badge/docker-000?style=for-the-badge&logo=docker
[docker-url]: https://docs.docker.com/
[uvicorn-badge]: https://img.shields.io/badge/uvicorn-000?style=for-the-badge&logo=uvicorn
[uvicorn-url]: https://www.uvicorn.org/
