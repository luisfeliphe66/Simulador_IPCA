#!/bin/bash

# Função para verificar e criar conector se não existir
create_connector_if_not_exists() {
  local connector_name=$1
  local config_file=$2

  # Verificar se o conector já existe
  connector_exists=$(openmetadata check-connector --name "$connector_name")

  if [ "$connector_exists" != "true" ] then
    echo "Creating connector: $connector_name"
    openmetadata create-connector -c "$config_file"
  else
    echo "Connector $connector_name already exists, skipping creation."
  fi
}

# Percorrer todos os arquivos de configuração no diretório de conectores e criar conectores
for config_file in /etc/openmetadata/connectors/*.yaml; do
  connector_name=$(basename "$config_file" .yaml)
  create_connector_if_not_exists "$connector_name" "$config_file"
done
