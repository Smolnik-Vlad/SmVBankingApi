
migrate:
	python manage.py makemigrations
	python manage.py migrate

runserver:
	python manage.py runserver 8001

shell:
	python manage.py shell

createSU:
	python manage.py createsuperuser
