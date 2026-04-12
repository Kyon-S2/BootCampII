import json
import os
from tabulate import tabulate

#Funcionalidades para armazenar(salvar) os gastos da pessoa! SAVE!

arquivo_dados = "gastos.json"

def salvar_dados(lista_gastos):
    
    with open(arquivo_dados, "w", encoding="utf-8") as arquivo:
        json.dump(lista_gastos, arquivo, indent=4, ensure_ascii=False)

def carregar_dados():
    
    if not os.path.exists(arquivo_dados):
        return []
    
    with open(arquivo_dados, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
    

historico_gastos = carregar_dados() # Onde está sendo armazenado as informações (historico_gastos) e var que carrega os dados!

#DEMAIS FUNCIONALIDADES!

def obter_valor_valido():
    while True:

        valorGastoUsuario = input("Informe o valor do seu gasto nesse formato (50.30):")

        try:

            valorGastoUsuario = float(valorGastoUsuario)

            if valorGastoUsuario > 0:
                return valorGastoUsuario
            else:
                print("O valor precisa ser maior que 0") # Caso seja menor ou igual a 0

        except ValueError: #Caso informe letras OU outros caracteres!

            print(" Isso provavelmente não é um número. Por favor, informe um número (30.20)")

#Obter data válida!

def obter_data_valida():
    while True:

        dataUsuario = input("Informe a data nesse formato, incluindo as barras, ex: (DD/MM/AAAA):")

        if len(dataUsuario) == 10 and dataUsuario[2] == "/" and dataUsuario[5] == "/" : #LEN usado para verificar se o texto digitado tem 10 caracteres e se as barras estão no lugar certo!
            return dataUsuario
        
        else: 
            print("Data inválida! Informe nesse formato: (DD/MM/AAAA)")

#Obter nome do gasto!

def obter_nome_gasto():
    while True:

        nomeGasto = input("Informe o nome do seu gasto, ex: (Arroz, boneca, etc): ")

        if len(nomeGasto) > 0 and not nomeGasto.isdigit(): #Uso do isdigit para não aceitar apenas números!
            return nomeGasto
        
        else:
            print("Informe um nome válido!")

#Obter Classe do gasto

def obter_classeGasto():
    while True:

        nomeClasseGasto = input("Informe o tipo de gasto, ex:(Mercado,Lazer,etc):")

        if len(nomeClasseGasto) > 0 and not nomeClasseGasto.isdigit():
            return nomeClasseGasto
        else:
            print("Escreva um nome de classe válida para ser aceito, ex: (mercado,lazer,etc)")


#CADASTRO DE GASTO! (Função que vai juntar todas as funções acima para o cadastro dos gastos!)

def cadastro_gasto():
    print("\n --- Cadastro de Gasto ---")

    nome = obter_nome_gasto()
    valor = obter_valor_valido()
    classe = obter_classeGasto()
    data = obter_data_valida()

#Criação do dicionário (para juntar as informaçoes em 1 só!)

    gastoFormado =  {
        "nome": nome,
        "valor": valor,
        "classe": classe,
        "data": data
    }

    print("\n Gasto formado!")
    return gastoFormado

# Função que possibilita com que o usuário continue cadastrando gastos até que decida parar!

def menu_cadastro():

    global historico_gastos
    while True:

        novo_gasto = cadastro_gasto()
        historico_gastos.append(novo_gasto)
        salvar_dados(historico_gastos) #Salvando!

        opcao = input("\n Quer cadastrar outro gasto? (S/N):").upper().strip()

        if opcao != "S":
            print("Retornando ao Menu")
            break

def menu_principal():
        global historico_gastos
        while True:
            print("\n =-=-=-=-=-=-=-=-= Finance Control System =-=-=-=-=-=-=-=-=")
            print("1. Cadastrar Novos Gastos!")
            print("2. Remover Gastos!")
            print("3. Atualizar Gastos! (Sem funcionamento ainda!)")
            print("4. Ver relatório de Gastos")
            print("5. Sair do sistema")
            print("\n =-=-=-=-=-=-=-=-= Finance Control System =-=-=-=-=-=-=-=-=")

            escolha = input("Escolha uma das opções:")

            if escolha == "1":
                menu_cadastro()

            elif escolha == "2":
                print("\n" + "=-"*8 + "Remover Gasto" + "-="*8)
                if not historico_gastos:
                    print("Não existe gastos para serem removidos!")
                else:
                    for  i, g in enumerate(historico_gastos, 1):
                        print(f"{i}. {g['nome']} | R$ {g['valor']} | {g['data']}")

                    try:
                        num = int(input("\n Digite o número do gasto que deseja excluir!"))
                        remover_gasto(num)
                    
                    except ValueError:
                        print("Digite apenas números, por favor!")
                    

            elif escolha == "4":
                print("\n" + "=-"*10 + "Relatório/Total" + "-="*10)
                
                tabela = relatorio_tabela(historico_gastos)
                print(tabela)

                #Calculando total agora!

                total = sum(g['valor'] for g in historico_gastos)
                print(f"\n Valor Total Acumulado: R$ {total:.2f}")
                print("=-="*15)

            elif escolha == "5":
                print("Encerrando o programa, até mais!")
                break

            else:
                print("Opção inválida ou sem funcionamento ainda!")

#Função para fazer o relatório no formato de tabela! (Organização)!

def relatorio_tabela(lista_gastos):
    if not lista_gastos:
        return "Não há gastos cadastrados!"
    
#Lista propriamente dita!

    dados_tabela = []
    for g in lista_gastos:
        dados_tabela.append ([
            g['nome'],
            f"R$ {g['valor']:.2f}",
            g['classe'],
            g['data']
        ])

    cabecalhos = ["Nome do Produto", "Valor", "Categoria","Data"]
    return tabulate(dados_tabela, headers=cabecalhos, tablefmt="fancy_grid")

def remover_gasto(indice):
    global historico_gastos
    try:
        if indice <= 0:
            print("Informe um número maior que zero! \n")
            return
        gasto_removido = historico_gastos.pop(indice-1)
        salvar_dados(historico_gastos)
        print(f"Tudo certo!, o gasto: '{gasto_removido['nome']}' foi removido!")
    except IndexError:
        print("\n Erro!: O número inserido não existe na lista!")