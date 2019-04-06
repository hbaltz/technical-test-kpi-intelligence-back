# Pull a pre-built alpine docker image with nginx and python3 installed
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

# Set the port on which the app runs; make both values the same.
ENV LISTEN_PORT=5000
EXPOSE 5000

LABEL maintainer="Hugo Baltz"

# Indicate where uwsgi.ini lives
ENV UWSGI_INI uwsgi.ini

# Tell nginx where static files live.
ENV STATIC_URL /api/static

# Set the folder where uwsgi looks for the app
WORKDIR /api

# Copy the app contents to the image
COPY . /api