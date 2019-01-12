# Carver Edison 

## Technologies
- [Docker](https://docs.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/gettingstarted/)
- [Flask](http://flask.pocoo.org/docs/1.0/patterns/)
- React
- Postgres
- [Swagger UI](https://swagger.io/tools/swagger-ui/)
- Nginx as a Reverse Proxy

## Task
The goal is to build a web app using python, postgresql and openapi specs that makes an http call to any feed provider [twitter, linkedIn, bureau of labor statistics, anything for that matter] and pulls the data to store it in a managed database. Use swagger to document the API details [like endpoints, methods, input and output etc]. Display the stored data on a single web page in a tabular format. 
It is not a must have but feel free to get creative using Docker to create a package. Please organize your code structure, so it’s easier to follow through and configurable to make needed changes along the path of deployment in real life.


## Task Completed as follows:
1.  Simple Flask app created with Application Factory Pattern. Introduced Flask CLI tool to manage commands from terminal, i.e.,
    - recreate-db
    - seed-db
    - test
2. Create GET endpoint with Flask and accompanied testing.
3. Introduce Docker and Docker-compose to Flask, Postgres, React, Swagger
4. Introduce React for front-end focus and tabular format of GET request
5. Apply Swagger-UI for API specs

## How to Run
1. Clone Repo
2. `cd carver-edison`
2. Depending on your environment, I have a mac, `chmod +x services/tweets/entrypoint.sh`
    - Because of dependent services, tweets on tweets_db (Postgres) we add an entrypoint to wait for Postgres to be up and running. 
3. From the command line
    1. `docker-compose -f docker-compose-dev.yml build`
    2. `export REACT_APP_TWEETS_SERVICE_URL=http://localhost` - Important! 
    3. `docker-compose -f docker-compose-dev.yml up -d --build`
    4. `docker-compose -f docker-compose-dev.yml run tweets python manage.py recreate-db`
    5. `docker-compose -f docker-compose-dev.yml run tweets python manage.py seed-db`
    6. `docker-compose -f docker-compose-dev.yml run tweets python manage.py test`
9. Navigate to http://localhost
    - this will show off two names: Prakash Sinha, Gamal Ali on a React front-end
    - API endpoint is on http://localhost/tweets
10. SwaggerUI can be seen on http://localhost/swagger
11. Tell me what you are satisfied with and dissatisfied with. 

## Commands
- View healthy docker services running and their ports `docker ps -a`

## What can be added?
1. React testing
2. Travis CI
3. Other HTTP Methods
4. More testing

* Worth about another 2 days of work to add the other features. 

