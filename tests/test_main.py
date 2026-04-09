#FUNÇÕES PARA TESTES!

def validar_valorGasto(valor_texto):
    try:
        valorGasto = float(valor_texto)
        return valorGasto > 0
    except ValueError:
        return False
    
def validar_nomeGasto(nome_texto):
    
    if len(nome_texto) > 0  and not nome_texto.isdigit():
        return True
    return False

#Teste para valor dado ao GASTOS!

def teste_valor_positivo_deve_funcionar():
    assert validar_valorGasto("100.50") == True

def teste_valor_negativo_deve_falhar():
    assert validar_valorGasto("-50.30") == False

def teste_valor_texto_deve_falhar():
    assert validar_valorGasto("Ciquenta reais e dez centavos") == False

#Testes para nomes dados ao GASTOS!

def teste_nome_valido_deve_funcionar():
    assert validar_nomeGasto("Aluguel do meu Filho") == True

def teste_nome_invalido_deve_falhar():
    assert validar_nomeGasto("1023994") == False

def teste_nome_vazio_deve_falhar():
    assert validar_nomeGasto("") == False