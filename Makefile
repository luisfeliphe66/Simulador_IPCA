.PHONY: deploy planning down

deploy:
	docker-compose -f docker/docker-compose.yml up --build -d

down:
	docker-compose -f docker/docker-compose.yml down -v