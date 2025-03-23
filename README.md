# Django-backend
A repo with the basic template to quickly build a backend application

## Basic steps:
* Clone the repo
* Refer `.sample.env.app` file for environment variables to be set and create a `.env` file accordingly
* Checkout the `Makefile` for shortcuts
* Please make sure that docker is updated. Update Rancher if not already
* Start docker/rancher

## How to run code on local machine using dockerfile:
* Run the command to build your image: `docker build . -t backend_svc`
* Check whether the image is built: `docker images | grep backend_svc`
* Deploy the server: `docker run --rm -it -p 8000:8000 backend_svc`

## How to run code on local machine using makefile:
* There is a Makefile present which runs docker compose commands
* Start server: `make start`
* Stop server: `make stop`
* Make sure your app migration folder is added in the volume mount for the app in compose file. This is a must have.
* If you want to run any command like make `python manage.py migrate` then open shell using `make shell`.
* Incase you want to remove all postgres data and volumes: `make clean`
* After you run `make clean`, you can run `make init` to perform basic setups. It will also set some tables with relevent default values.
* Change the `SITE_ID` env variable in `.env` file as specified in the output of `make init` command.
* Then you can run `make start` to start the server.
* Refer: https://github.com/docker/awesome-compose/blob/master/official-documentation-samples/django/README.md