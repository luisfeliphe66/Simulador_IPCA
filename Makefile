.PHONY: deploy, down

deploy:
	@echo "Realizando o deploy..."
	docker-compose -f docker/docker-compose.yml up --build -d
	@echo "Deploy concluído com sucesso!"

down:
	docker-compose -f docker/docker-compose.yml down -v

#Username: admin@open-metadata.org
#Password: admin
