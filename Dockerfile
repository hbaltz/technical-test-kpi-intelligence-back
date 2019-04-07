# Pull a pre-built alpine docker image with nginx and python3 installed
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

# Set the port on which the app runs; make both values the same.
ENV LISTEN_PORT=5000
EXPOSE 5000

LABEL maintainer="Hugo Baltz"


RUN apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add --no-cache --update postgresql-dev

# Indicate where uwsgi.ini lives
ENV UWSGI_INI uwsgi.ini

# Set the folder where uwsgi looks for the app
WORKDIR /api

# Copy the app contents to the image
COPY . /api

RUN pip install -r requirements.txt