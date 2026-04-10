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

def validar_classeGasto(classe_texto):

    if len(classe_texto) > 0 and not classe_texto.isdigit():
        return True
    return False

#Teste para valor dado ao GASTOS!

def teste_valor_positivo_deve_funcionar():
    assert validar_valorGasto("100.50")

def teste_valor_negativo_deve_falhar():
    assert not validar_valorGasto("-50.30")

def teste_valor_texto_deve_falhar():
    assert not validar_valorGasto("Ciquenta reais e dez centavos") # Assert not pra FALSE!

#Testes para nomes dados ao GASTOS!

def teste_nome_valido_deve_funcionar():
    assert validar_nomeGasto("Aluguel do meu Filho")

def teste_nome_invalido_deve_falhar():
    assert not validar_nomeGasto("1023994")

def teste_nome_vazio_deve_falhar():
    assert not validar_nomeGasto("")

#TESTANDO CLASSE!

def teste_classe_somente_letras_funcionando():
    assert validar_classeGasto("Lazer")

def teste_classe_somente_numeros_falhando():
    assert not validar_classeGasto("129343")

def teste_classe_hibrida_funcionando():
    assert validar_classeGasto("Lazer 1")