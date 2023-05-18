# Import
import mysql.connector

# MYSQL Connection
# localhost Server
# database crudbd
# tables: vendas

conexao = mysql.connector.connect(
    host="localhost", 
    port="3306",
    user="root",
    password="",
    database="crudbd"
)

cursor = conexao.cursor()

# Create
nome_produto = "chocolate"
valor = 15.69
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()

# Read
comando = f"SELECT * FROM vendas"
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

# Update
nome_produto = "toddynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

# Delete
nome_produto = "toddynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

# Finish Connection
cursor.close()
conexao.close()
