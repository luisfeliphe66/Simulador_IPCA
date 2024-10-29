-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS bc_data;

-- Uso do banco de dados
USE bc_data;

-- Criação da tabela com verificações adicionais
CREATE TABLE IF NOT EXISTS taxa_juros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    valor VARCHAR(50) NOT NULL
);