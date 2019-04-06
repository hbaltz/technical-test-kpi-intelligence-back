# Technical test kpi intelligence back

## Description

Paris Region wants to have a web application to track the investments it makes for its high schools buildings. 
This is the REST API to retrieve the investments data.

## Requirement

* Docker : you can acces the installation documentation [here](https://docs.docker.com/install/)

## Launch the application

* Build the docker image `docker build --rm . -t hbaltz/technical-test-kpi-intelligence-back:TAG`
* Delete old container `docker rm api-inv`
* Launch the image `docker run -d -p 5000:5000 --name=api-inv hbaltz/technical-test-kpi-intelligence-back:TAG`

## Use the application 

* Get all the investments: `curl -i -H "Content-Type: application/json" "http://localhost:5000/api/investment"`
* Apply a filter on the city and/or the progress status: `curl -i -H "Content-Type: application/json" "http://localhost:5000/api/investment?city=<THE_CITY>&progress_status=<THE_PROGRESS_STATUS>"`
Example: `curl -i -H "Content-Type: application/json" "http://localhost:5000/api/investment?city=Versailles&progress_status=Opération livrée"`
* Get a single investment: `curl -i -H "Content-Type: application/json" "http://localhost:5000/api/investment/<CODEUAI>"`
Example: `curl -i -H "Content-Type: application/json" "http://localhost:5000/api/investment/0782562L"`

## Stop the application

* Launch this command `docker stop api-inv`