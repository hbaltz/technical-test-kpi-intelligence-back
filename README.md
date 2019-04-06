# Technical test kpi intelligence back

## Description

Paris Region wants to have a web application to track the investments it makes for its high schools buildings. 
This is the REST API to retrieve the investments data.

## Requirement

* Docker : you can acces the installation documentation [here](https://docs.docker.com/install/)

## Launch the application :

* Build the docker image `docker build --rm . -t hbaltz/technical-test-kpi-intelligence-back:TAG`
* Launch the image `docker run -d -p 5000:5000 hbaltz/technical-test-kpi-intelligence-back:TAG`