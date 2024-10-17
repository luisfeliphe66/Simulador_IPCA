
#!/bin/bash

# # Esperar o PostgreSQL iniciar
sleep 10

# Adicionar a linha para permitir conexões de todos os hosts
# echo "host all all 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf
echo "host all all 172.26.12.7/24 md5" >> /var/lib/postgresql/data/pg_hba.conf

# Trocar para o usuário postgres
su - postgres -c "
  # Reiniciar o PostgreSQL para aplicar as mudanças
  pg_ctl -D '$PGDATA' -m fast -w stop
  pg_ctl -D '$PGDATA' -o '-c listen_addresses='*'' -w start
"


# # Parar o PostgreSQL para aplicar as mudanças
# pg_ctlcluster 13 main stop

# # Reiniciar o PostgreSQL para aplicar as mudanças
# pg_ctlcluster 13 main start














#!/bin/bash
# set -e

# psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
# 	CREATE USER docker;
# 	CREATE DATABASE docker;
# 	GRANT ALL PRIVILEGES ON DATABASE docker TO docker;
# EOSQL


# # Trocar para o usuário postgres
# su - postgres -c "

# # Iniciar o PostgreSQL em segundo plano
# pg_ctl -D \$PGDATA -o \"-c listen_addresses='*'\" -w start

# # Verificar se o diretório de inicialização contém scripts SQL
# if [ -d \"/docker-entrypoint-initdb.d\" ]; then
#   for f in /docker-entrypoint-initdb.d/*; do
#     case \"\$f\" in
#       *.sh)     echo \"\$0: executando \$f\"; . \"\$f\" ;;
#       *.sql)    echo \"\$0: executando \$f\"; psql -U \"\$POSTGRES_USER\" -d \"\$POSTGRES_DB\" -f \"\$f\"; echo ;;
#       *)        echo \"\$0: ignorando \$f\" ;;
#     esac
#     echo
#   done
# fi

# # Parar o PostgreSQL para continuar a inicialização do Docker
# pg_ctl -D \$PGDATA -m fast -w stop

# # Iniciar o PostgreSQL novamente
# exec postgres
# "


# #!/bin/bash

# # Iniciar o PostgreSQL em segundo plano
# pg_ctl -D "$PGDATA" -o "-c listen_addresses='*'" -w start

# # Verificar se o diretório de inicialização contém scripts SQL
# if [ -d "/docker-entrypoint-initdb.d" ]; then
#   for f in /docker-entrypoint-initdb.d/*; do
#     case "$f" in
#       *.sh)     echo "$0: executando $f"; . "$f" ;;
#       *.sql)    echo "$0: executando $f"; psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f "$f"; echo ;;
#       *)        echo "$0: ignorando $f" ;;
#     esac
#     echo
#   done
# fi

# # Parar o PostgreSQL para continuar a inicialização do Docker
# pg_ctl -D "$PGDATA" -m fast -w stop

# # Iniciar o PostgreSQL novamente
# exec postgres
