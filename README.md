# nginx-dash-gunicorn-boilerplate
This repository is a boilerplate for the deployment of a dash app using nginx and gunicorn all as docker containers

Fire it up
docker-compose up --build

down
docker-compose rm -fs
docker stop  $(docker ps -a -q)
docker rm  $(docker ps -a -q)