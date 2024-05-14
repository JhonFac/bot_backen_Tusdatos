# Project Name: Python Clean Architecture Microservices Templates

### Description

The template was structured following the principles defined by [clean architecture](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/).

The base template written with Python using Flask, SQL Alchemy.

Each service has his own database, but the schema, user, password params are the same for both.

In this example, each application contains two sections: one called "greeting", which is simply an endpoint that returns a greeting indicating the visitor's number, which is obtained from a cache, and the other is "books", which consists of a CRUD of books, which are stored in a database, either in MySQL or in Firestore.

Being a Python project, the following conventions are followed:

- Four-space identation (no tabs), even in non-`.py` files.
- Class names in `UpperCamelCase`.
- Methods, functions and variables in `snake_case`.
- Module names (`.py` files) in` snake_case`.
- Package names (folders) in `lowercase`, no underscores even if they contain more than one word (eg" usecases "instead of" use_cases ").
- Use absolute imports where possible.

### Construction 🛠️
* **Language:** Python 3
* **Framework:** Flask, SQL Alchemy

## Requirements
- Docker installed

## Installation and execution

- Clone or Fork the project.
- Copy **.env.example** to **.env**. It will be used as environment variables source.
- Inside Docker/app folders of casos-service and delivery-services:
* Copy **.env.example** to **.env**. It will be used as environment variables source.

Run ```docker-compose``` command inside **docker-python** folder.

* Building the containers: ```docker-compose build```

* Starting the services: ```docker-compose up -d```

* Stoping the services: ```docker-compose stop```

By default the microservices will run under the following ports:
- casos-service: 8000
- delivery-service: 8001

Check the **.env.example** file to change these or any other params.

#### Note
The Flask application will probably throw an exception the first time, because it will try to connect to the MySQL service that is still initializing for the first time; in this case wait for MySQL to fully initialize first and then run the command `docker-compose restart $NAME_SERVICE` in another terminal to restart the crashed service.

