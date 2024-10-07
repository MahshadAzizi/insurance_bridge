## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/MahshadAzizi/url_shortener.git
$ cd url_shortener
```

## Database connection
Some environment variables must be defined to connect to the postgresql database:

```
- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_HOST
- POSTGRES_PORT
```

## Backend variables
Some environment variables must be defined to connect to the backend service:

```
- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
```

## How to run the app:
Via docker-compose

```sh
$ docker-compose build
$ docker-compose up -d
```
