# Description
This repository is a boilerplate for the deployment of a multipage dash app using nginx and gunicorn all as docker containers

# Files

## nginx
File / Folder | Description
--- | --- 
Dockerfile | nginx Dockerfile
nginx.conf | nginx configurations
project.conf | nginx configurations

## dash
File / Folder | Description
--- | --- 
assessts | contains pictures and css stylesheet
pages | contains individual dash pages
app.py | dash navigation app to navigate between the different pages
Dockerfile | dash Dockerfile

# Installation
- Install Docker

# Run
## Fire it up
- Make sure docker is running
- docker-compose up --build
- visit your local host address or ip address of your computer on port 80 the multipage dash app should now be hosted

## Down
- docker-compose rm -fs
- docker stop  $(docker ps -a -q)
- docker rm  $(docker ps -a -q)