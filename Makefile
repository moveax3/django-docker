start:
	docker-compose -f docker-compose.yml up -d
clear_pagespeed:
	docker-compose exec nginx rm -rf /var/cache/pagespeed/*

debug:
	docker-compose stop
	docker-compose -f docker-compose.debug.yml up -d
	docker-compose exec -d django_en python3 manage.py runserver 0.0.0.0:8000 

backup:
	docker-compose exec db_en pg_dump -U postgres -a -Fc -f /fixtures/django_en.backup database_en

restore:
	make -k restore_from_backup

restore_from_backup: recreate_db db_migrate restore_db_en

restore_db_en:
	docker-compose exec db_en pg_restore -U postgres -a -d database_en /fixtures/django_en.backup

recreate_db:
	docker-compose stop django_en
	docker-compose exec db_en dropdb -U postgres database_en
	docker-compose exec db_en createdb -U postgres database_en
	docker-compose start django_en

db_migrate:
	docker-compose exec django_en python3 manage.py makemigrations
	docker-compose exec django_en python3 manage.py migrate auth
	docker-compose exec django_en python3 manage.py migrate contenttypes
	docker-compose exec django_en python3 manage.py migrate

db_show_tables:
	docker-compose exec db_en psql -U postgres -d database_en -c "SELECT * FROM pg_catalog.pg_tables"

createsuperuser_en:
	docker-compose exec django_en python3 manage.py createsuperuser

djangoshell:
	docker-compose exec django python3 manage.py shell_plus

cleardefender:
	docker-compose exec django python3 manage.py cleanup_django_defender

loaddata:
	docker-compose exec django python3 manage.py loaddata dump.json

dumpdata:
	docker-compose exec django python3 manage.py dumpdata --exclude=sessions --exclude=contenttypes --exclude=admin --exclude=auth --exclude=defender --exclude=auditlog --exclude=hitcount > dump.json

run:
	docker-compose up

build:
	docker-compose build

stop:
	docker-compose stop

full_rebuild:
	docker-compose build --no-cache
