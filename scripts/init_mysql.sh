#!/bin/sh

echo "Iniciando script de criação de tabelas."

# Esperar o MySQL estar pronto para conexões
while ! mysql -h "mysql" -u root -p"$MYSQL_ROOT_PASSWORD" -e "SHOW DATABASES;" > /dev/null 2>&1; do
  echo "Aguardando MySQL..."
  sleep 3
done

echo "MySQL está pronto para conexões. Criando tabela..."

# # Criar a tabela
# mysql -h "mysql" -u root -p"$MYSQL_ROOT_PASSWORD" <<EOF
# USE sua_database;
# CREATE TABLE sua_tabela (
#   id INT AUTO_INCREMENT PRIMARY KEY,
#   nome VARCHAR(255) NOT NULL
# );
# EOF

# Executar o script SQL
mysql -h "mysql" -u root -p"$MYSQL_ROOT_PASSWORD" < /var/scripts/mysql/init.sql

echo "Tabela criada com sucesso."


# #!/bin/bash

# # Criar o diretório e ajustar as permissões
# mkdir -p /var/lib/mysql
# chmod -R 777 /var/lib/mysql

# # Iniciar o MySQL sem networking
# mysqld --initialize-insecure --user=mysql --datadir=/var/lib/mysql &
# sleep 10

# # Executar o script de inicialização
# mysql -u root -p"$MYSQL_ROOT_PASSWORD" < /docker-entrypoint-initdb.d/init.sql

# # Finalizar o MySQL
# mysqladmin shutdown -p"$MYSQL_ROOT_PASSWORD"

# # Reiniciar o MySQL com as configurações padrão
# exec mysqld --default-authentication-plugin=mysql_native_password --sort_buffer_size=10M