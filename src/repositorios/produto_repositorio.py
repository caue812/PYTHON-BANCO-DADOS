from src.database.conexao import abrir_conexao


def cadastrar(nome_produto: str):
    try:
        conexao = abrir_conexao()
       
        # Criar um cursor que nos permitirá executar comandos no banco de dados
        cursor = conexao.cursor()

        # SQL Injection é uma técnica de ataque em que comandos SQL maliciosos são inseridos em entradas 
        # de dados para manipular o banco de dados. Em Python, proteger-se contra SQL Injection é 
        # essencial para evitar vazamento de dados e garantir a segurança de aplicativos web.
        # Como prevenir:
        # update colaboradores set nome = 'Francisco', idade = 31 where id = 10;
        # "update colaboradores set nome = %s, idade = %s where id = %s", (colaborador_nome, idade, id)

        # Definir qual será o comando que iremos executar, neste caso será um insert
        # O que não fazer cursor.execute("insert into produtos (nome) values ('X-calabresa')") 
        cursor.execute("insert into produtos (nome) values (%s)", (nome_produto,)) 

        # Commit é necessário pois sem ele o insert n será concretizado no bd
        conexao.commit()
        # Fechar a conexão com o bd
        conexao.close()
        
    except Exception as e:
        print(e)

def listar_todos():
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("select id, nome from produtos")
        registros = cursor.fetchall()

        produtos = []
        for registro in registros:
            produto = {
                "id": registro[0],
                "nome": registro[1]
            }
            produtos.append(produto)
        return produtos
    except Exception as err:
        print("Não foi possível carregar os produtos")
        print(err)
