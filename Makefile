.PHONY: deploy, down

deploy:
	@echo "Realizando o deploy..."
	docker compose -f docker/compose/docker-compose.yml up --build -d
down:
	docker-compose -f docker/compose/docker-compose.yml down -v

