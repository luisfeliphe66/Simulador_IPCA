# Dockerfile.init_db

FROM mysql:8.0.32 as mysql

# Copiar script de automação
COPY ./scripts/init_mysql.sh /usr/local/bin/init_mysql.sh

COPY ./scripts/mysql/init.sql /var/scripts/mysql/init.sql

# Ajustar permissões do script
RUN chmod +x /usr/local/bin/init_mysql.sh

# Usar o script de automação como comando
CMD [ "/usr/local/bin/init_mysql.sh" ]