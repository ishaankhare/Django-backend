.PHONY: clean init start stop config shell pg-shell py-shell consumer-shell migrations

clean:
	docker compose down --remove-orphans -v

init:
	docker compose kill --remove-orphans && \
	docker compose up --build --remove-orphans -d postgres app && \
	docker compose exec app /bin/bash -c '\
	python manage.py makemigrations && \
	python manage.py migrate && \
	echo "Creating super user with username $$DJANGO_SUPERUSER_USERNAME" && \
	python manage.py ensure_adminuser && \
	python manage.py ensure_self_host_site && \
	python init_script.py' && \
	docker compose kill --remove-orphans

start:
	docker compose up --build --watch --remove-orphans

stop:
	docker compose down --remove-orphans

config:
	docker compose config

shell:
	docker compose exec app /bin/bash

pg-shell:
	docker compose exec postgres /bin/sh -c \
	'psql -v ON_ERROR_STOP=1 --username "$$POSTGRES_USER" --dbname "$$POSTGRES_DB"'

py-shell:
	docker compose exec app /bin/bash -c 'python manage.py shell'

consumer-shell:
	docker compose exec consumer /bin/bash

migrations:
	docker compose run --build --rm --remove-orphans app /bin/bash -c \
	'python manage.py makemigrations' && make stop