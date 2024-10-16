-- Criação do usuário e concessão de privilégios
-- CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED BY 'password';
-- GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
-- FLUSH PRIVILEGES;

-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS bacen_db;

-- Uso do banco de dados
USE bacen_db;

-- Criação da tabela com verificações adicionais
CREATE TABLE IF NOT EXISTS indicador_economico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    indicador VARCHAR(50) NOT NULL,
    data DATE NOT NULL,
    suavizada VARCHAR(1) NOT NULL,
    media DECIMAL(5,4) NOT NULL,
    mediana DECIMAL(5,4) NOT NULL,
    desvio_padrao DECIMAL(5,4) NOT NULL,
    minimo DECIMAL(5,4) NOT NULL,
    maximo DECIMAL(5,4) NOT NULL,
    numero_respondentes INT NOT NULL,
    base_calculo INT NOT NULL
);
