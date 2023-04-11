import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="estante"
    )
cursor = conexao.cursor()
#######################################
titulo = input("Qual o título do livro? ")
autor = input("Quem é o autor do livro? ")

cursor.execute(
f'''INSERT INTO livros VALUES(null, '{titulo}', '{autor}')''')


'''
Podemos fazer também: "INSERT INTO livros VALUES(null, %s,%s)",
(titulo, autor) )

'''
conexao.commit()
print("Inserido com sucesso")

cursor.close()
conexao.close()
print("Conexão encerrada")
