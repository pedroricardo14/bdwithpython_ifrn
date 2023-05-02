## CONECTAR AO BANCO DE DADOS ##
import mysql.connector
conexao = mysql.connector.connect(
    host = "localhost", user = "root",
    password = "", database = "livraria")
cursor = conexao.cursor()
#print("Conexão OK")


## FUNÇÃO CADASTRO #############
def cadastrar():
    print("=== CADASTRO DE LIVRO ===")
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    preco = input("Preço do livro: ")
    cmd = "INSERT INTO livros VALUES (null, %s, %s, %s)"
    cursor.execute(cmd, (titulo,autor,preco) )
    conexao.commit()
    print("Inserido com sucesso! \n\n")


## FUNÇÃO LISTAR #####
def listar():
    print("== LISTAGEM DE LIVROS ===")
    cursor.execute("SELECT * FROM livros")
    for linha in cursor:
        print("Código:", linha[0])
        print("Titulo:", linha[1])
        print("Autor:", linha[2])
        print("Preço:", linha[3])

## FUNÇÃO PESQUISAR ###
def pesquisar():
    print("== PESQUISA DE LIVROS ==")
    titulo = input("Tútulo do Livro: ")
    autor = input("Autor do Livro: ")
    cmd = f'''SELECT * FROM livros
            WHERE titulo LIKE '%{titulo}%'
            AND autor LIKE '%{autor}%' '''
    cursor.execute(cmd)
    for linha in cursor:
        print("Código:", linha[0])
        print("Titulo:", linha[1])
        print("Autor:", linha[2])
        print("Preço:", linha[3])



## MENU PRINCIPAL ##
while True:
    print("=== MENU DO SISTEMA ===")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Pesquisar")
    print("5. Sair")
    opcao = input("Opção: ")

    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        pesquisar()
       #print("Cadastrar")
    elif opcao == '5':
        print("Até a próxima!")
        break