python:
	.venv\Scripts\activate

restart:
	docker-compose down
	docker-compose build
	docker-compose up -d