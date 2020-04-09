run:
	TOKEN=$$TOKEN gunicorn3 --bind 0.0.0.0:8081 app:app

lock:
	pipenv lock -r > requirements.txt