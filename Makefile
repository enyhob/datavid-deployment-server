run:
	TOKEN=$$TOKEN gunicorn --bind 0.0.0.0:8081 app:app