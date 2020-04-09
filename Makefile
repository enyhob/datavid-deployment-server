run:
	TOKEN=$$TOKEN PROJECT=$$PROJECT gunicorn3 --bind 0.0.0.0:8081 app:app

deploy:
	export TOKEN=$$TOKEN; \
	export PROJECT=$$PROJECT; \
	nohup gunicorn3 --bind 0.0.0.0:8081 app:app &

lock:
	pipenv lock -r > requirements.txt