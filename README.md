# Template finder service

### 1. Docker installation

- clone repo

```sh
git clone https://github.com/jlomuk/templates_finder
```

- move in directory "templates_finder"

```sh
cd templates_finder
```

- copy .env file from .env.example in CI directory

```sh
cp ci/.env.example ci/.env
```

- start docker-compose

```sh
docker-compose -f ci/docker-compose.yaml up
```

- after start docker containers, the site will be available on http://127.0.0.1:9000/ 


### 2. POSTMAN COLLECTION:

Import and use postman collections for testing api

```sh
templates_finder/Template_finder_collection.postman_collection.json
```
