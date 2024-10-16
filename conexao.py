# conexão com banco de dados
# pip install mysql-connector-python para estabelecer a conexão

import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        dbconfig = {
            'host': '127.0.0.1',
            'user': 'senai',
            'password': '1234',
            'database': 'senai'
        }
        
        con = mysql.connector.connect(**dbconfig)
        return con
    except (Exception, Error) as error:
        print('Não conectou! ' +str(error))

def read(con):
    # Estabelecer a conexão
    cursor = con.cursor()
    
    query = '''SELECT * FROM estudante;'''

    try:
        cursor.execute(query)

        print('\n\t\t\t ** SENAI - LISTA DE CHAMADA ** ')
        print('\t -- matricula -- \t\t ------------- Nome -------------')
        for campo in cursor.fetchall():
            print(f'\t{campo[0]} \t \t\t {campo[1]}')
            # print(f'\t matricula: {campo[0]} - Nome: {campo[1]}')
    
    except (Exception, Error) as error:
        print('Conectou mas não funcionou! ' + str(error))
    finally:
        if con is not None:
            cursor.close()
            con.close()
            print('\n\n Conexão fechada!\n')

def create(con, estudante):
    # Estabelecer a conexão
    cursor = con.cursor()
    
    # Código SQL
    query = '''INSERT INTO estudante(matricula, nome) VALUES (%s, %s);'''
    
    try:
        cursor.executemany(query, estudante)
        con.commit()
    except (Exception, Error) as error:
        print('Conectou mas não funcionou! ' + str(error))
    finally:
        if con is not None:
            cursor.close()
            con.close()
            print('\n\n Conexão fechada!\n')

            
def update(con, estudante):
   # Estabelecer a conexão
    cursor = con.cursor()

    # Codigo SQL
    query = '''UPDATE estudante SET nome = %s WHERE matricula = %s;'''

    try:
        cursor.executemany(query, estudante)
        con.commit()  # Confirma as alterações
    except (Exception, Error) as error:
        print('Conectou mas não funcionou!' + str(error))
    finally:
        if con is not None:
            cursor.close()
            con.close()
            print('\n\nConexão fechada!\n')            


def delete(con, estudante):
    # Estabelecer a conexão
    cursor = con.cursor()

    # Código SQL
    query = '''DELETE FROM estudante WHERE matricula = %s;'''

    try:
        cursor.execute(query, estudante)
        con.commit()
    except (Exception, Error) as error:
        print('Conectou mas não funcionou! ' + str(error))
    finally:
        if con is not None:
            cursor.close()
        con.close()
        print('\n\n Conexão fechada!\n')

        # Teste
create(conectar(), [('7298', 'Ryan gay')])

# create(conectar(), [('23456', 'Maria')])
# create(conectar(), [('34567', 'João')])

# update(conectar(), [('Catarina', '1234')])

# delete(conectar(), [('12345')])

read(conectar())