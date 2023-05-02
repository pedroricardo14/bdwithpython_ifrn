import mysql.connector
conexao = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="lojacarros")
cursor = conexao.cursor()
#############  LISTAR OS REGISTROS DA TABELA  #############
cursor.execute("SELECT * FROM carros")
for linha in cursor:
    print(linha)

############# SOLICITAR A DIGITAÇÃO/CONFIRMAÇÃO ##########
cod = input("Qual código deseja excluir? ")
cursor.execute("SELECT * FROM carros WHERE codigo = " + cod)
##### CONVERTE A CONSULTA EM UMA LISTA ###########
dados = cursor.fetchall()
if len(dados) == 0 :
    print("Código não encontrado.")
else:
   #print(dados)
   print("Código:", dados[0][0])
   print("Fabricante:", dados[0][1])
   print("Modelo:", dados[0][2])
   print("Preço", dados[0][3])
   resp = input("Confirma a exclusão(s/n)? ")
   if resp == "s":
        cursor.execute(
            "DELETE FROM carros WHERE codigo =" + cod)
        conexao.commit()
        print("Excluído com sucesso.")