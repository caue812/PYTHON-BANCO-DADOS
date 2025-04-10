import questionary
from src.repositorios import produto_repositorio


def executar_produto():
   opcoes = ["Listar todos", "Cadastrar", "Editar", "Apagar", "Voltar"]
   opcao_desejada = ""
   while opcao_desejada != "Voltar":
    opcao_desejada = questionary.select("Escolha o menu desejado dos produtos", opcoes).ask()
    if opcao_desejada == "Cadastrar":
       __cadastrar() # C
    elif opcao_desejada == "Listar todos":
       __listar_todos()


def __listar_todos():
   produtos = produto_repositorio.listar_todos()
   print("LIsta de produtos:")
   for produto in produtos:
      print("id:", produto["id"], "Nome:", produto["nome"])


# Funções com um/dois underline(s) antes do nome são consideradas
# função privadas, ou seja, n devem/podem ser utilizadas em outros
# arquivos
def __cadastrar():
    # Função reponsável por cadastrar um produto, solicitando os dados
    # necessários para o cadastro
    nome_produto = input("Digite o nome do produto: ")

    # Chamar a função de cadastrar(insert) o produto no bd
    # passando como parâmetro o nome do produto
    produto_repositorio.cadastrar(nome_produto)
    print("Produto cadastrado com sucesso")