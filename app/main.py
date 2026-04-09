#INTERFACE!

#Sistema que salva os gastos!
#Sistema que salva os dados!
#Sistema que carrega os dados salvos!
#Sistema que exclui os gastos!
#Sistema que cria os gastos!
#Sistema que atualiza os gastos já criados!
#Sistema que mostra os gastos salvos em formato (total, valor, data, classe, gasto em si)
#Sistema que calcula o total gasto!

#Obter um valor permitido!

def obter_valor_valido():
    while True:
        valorGastoUsuario = float(input("Informe o valor do seu gasto nesse formato (50.30)"))

        try:

            if valorGastoUsuario > 0:
                return valorGastoUsuario
            else:
                print("O valor precisa ser maior que 0") # Caso seja menor ou igual a 0

        except ValueError: #Caso informe letras OU outros caracteres!

            print(" Isso provavelmente não é um número. Por favor, informe um número (30.20)")

#Obter data válida!

def obter_data_valida():
    while True:
        dataUsuario = input("Informe a data nesse formato, incluindo as barras: ex: (DD/MM/AAAA):")

        if len(dataUsuario) == 10 : #LEN usado para verificar se o texto digitado tem 10 caracteres.
            return dataUsuario
        
        else: print("Data inválida! Informe nesse formato: (DD/MM/AAAA)")