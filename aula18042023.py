# Importar o conector
import mysql.connector

#estabelecer a conexao
conexao = mysql.connector.connect(
    host="localhost", user="root", password="", database="deposito"
)

# criar o cursor

cursor = conexao.cursor()

# laço para repetir a consulta






# laço para repetir cadastro
while True:
    resp = input("Deseja cadastrar? (s/n) ")
    if resp =="n":
        break
    descricao = input("Descriçao: ")
    posicao = input("Posição? ")
    cursor.execute(f'''INSERT INTO itens
    VALUES(null, "{descricao}", "{posicao}");
    ''')








    item = input("Qual item deseja localizar? ")
    pos = input("Qual posição?  ")


    #solicita digitação do item a localizar

    #item = input("Qual item deseja localizar?")

    #executar a consulta
    cursor.execute(f'''SELECT * FROM itens
    WHERE descricao LIKE "%{item}%"
    AND posicao LIKE "%{pos}%"; ''')

    # processa todos os registros do cursor

    #cursor.fetchall()

    #converte od dados para uma lista

    dados = cursor.fetchall()

    #exibir os dados do cursor
    #for linha in cursor:
    #    print(linha)


    #Exibir os dados do cursor
    for linha in dados:
        print("código: ", linha[0])
        print("descrição: ", linha[1])
        print("posição: ", linha[2])
        print("----------------------")

    # processa todos os registros do cursor
    cursor.fetchall()
    #retorna qts itens afetados no último comando
    #informa o tamanho da lista
    print(len(dados), "itens encontrados.")

    resp = input("Repetir a consulta? (s/n)")
    if resp == "n":
        break

    #print(cursor.rowcount, "itens encontrados.")

    #fechar o cursor

