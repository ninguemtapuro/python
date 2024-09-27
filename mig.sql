-- Verificar os registros da tabela
SELECT *
FROM estudante;

-- Gravar um registro de teste
INSERT INTO estudante(matricula, nome)
VALUE('1234', 'Miguel Romero');

-- Testando o update
UPDATE estudante
SET nome = 'Catarina Luiza'
WHERE matricula = '1234';

-- Verificar os registros da tabela
SELECT *
FROM estudante;

-- Excluindo os registros da tabela
DELETE FROM estudante
WHERE matricula = '1234';

-- Verificar os registros da tabela
SELECT *
FROM estudante;