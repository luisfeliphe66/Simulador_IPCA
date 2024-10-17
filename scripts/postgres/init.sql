-- -- Criação do usuário e concessão de privilégios
-- DO
-- $$
-- BEGIN
--    IF NOT EXISTS (
--       SELECT
--       FROM pg_catalog.pg_roles
--       WHERE rolname = 'root') THEN
--       CREATE ROLE root LOGIN PASSWORD 'password';
--    END IF;
-- END
-- $$;


-- -- ALTER DATABASE my_db OWNER TO postgres;

-- -- \connect my_db

-- GRANT ALL PRIVILEGES ON DATABASE mydatabase TO root;

-- -- Criação do banco de dados
-- CREATE DATABASE IF NOT EXISTS bacen_db;

-- -- Conectar-se ao banco de dados bacen_db
-- \c bacen_db;

-- -- Criação da tabela com verificações adicionais no banco de dados bacen_db
-- CREATE TABLE IF NOT EXISTS public.indicador_economico (
--     id SERIAL PRIMARY KEY,
--     indicador VARCHAR(50) NOT NULL,
--     data DATE NOT NULL,
--     suavizada VARCHAR(1) NOT NULL,
--     media DECIMAL(5,4) NOT NULL,
--     mediana DECIMAL(5,4) NOT NULL,
--     desvio_padrao DECIMAL(5,4) NOT NULL,
--     minimo DECIMAL(5,4) NOT NULL,
--     maximo DECIMAL(5,4) NOT NULL,
--     numero_respondentes INT NOT NULL,
--     base_calculo INT NOT NULL
-- );
