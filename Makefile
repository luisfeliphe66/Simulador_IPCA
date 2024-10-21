.PHONY: deploy, down

deploy:
	@echo "Realizando o deploy..."
	docker compose -f docker/compose/docker-compose.yml up --build -d
	@echo "Deploy concluído com sucesso!"
	@echo "Agora você pode visualizar seu aplicativo IPCA em seu navegador."
	@echo "URL: http://0.0.0.0:8501"
	@echo "Agora você pode visualizar seu aplicativo OPENMETADATA em seu navegador."
	@echo "URL: http://0.0.0.0:8585"
	@echo "Agora você pode visualizar seu aplicativo AIRFLOW em seu navegador."
	@echo "URL: http://localhost:8080"

down:
	docker-compose -f docker/compose/docker-compose.yml down -v

#OPENMETADATA
#http://0.0.0.0:8585/
#Username: admin@open-metadata.org
#Password: admin

# AIRFLOW
#http://localhost:8080/
#Username: admin
#Password: admin

#IPCA
#http://0.0.0.0:8501/