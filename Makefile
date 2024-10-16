.PHONY: deploy, down

deploy:
	@echo "Realizando o deploy..."
	docker-compose -f docker-compose.yml up --build -d
	@echo "Deploy concluído com sucesso!"
	@echo "You can now view your Streamlit app in your browser."
	@echo "URL: http://0.0.0.0:8501"

down:
	docker-compose -f docker-compose.yml down -v

#Username: admin@open-metadata.org
#Password: admin
