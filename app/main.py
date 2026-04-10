#INTERFACE!

#Sistema que salva os gastos!
#Sistema que salva os dados!
#Sistema que carrega os dados salvos!
#Sistema que exclui os gastos!
#Sistema que cria os gastos!
#Sistema que atualiza os gastos já criados!
#Sistema que mostra os gastos salvos em formato (total, valor, data, classe, gasto em si)
#Sistema que calcula o total gasto!

from app.core import obter_classeGasto, obter_data_valida, obter_nome_gasto, cadastro_gasto, menu_cadastro, historico_gastos

if __name__ == "__main__":

    def menu_principal():
        while True:
            print(f"\n =-=-=-=-=-=-=-=-= Finance Control System =-=-=-=-=-=-=-=-=")
            print(f"1. Cadastrar Novos Gastos!")
            print(f"2. Remover Gastos!")
            print(f"3. Atualizar Gastos!")
            print(f"4. Ver relatório de Gastos")
            print(f"5. Sair do sistema")
            print(f"\n =-=-=-=-=-=-=-=-= Finance Control System =-=-=-=-=-=-=-=-=")

            escolha = input(f"Escolha uma das opções:")

            if escolha == "1":
                menu_cadastro()

            elif escolha == "4":
                print(f"\n Exibindo relátorio dos gastos e o valor total!:")
                for g in historico_gastos:
                    print(f"=-= {g['nome']}: R$ {g['valor']} ({g['classe']}) {g['data']} =-=")
            
            elif escolha == "5":
                print(f"Encerrando o programa, até mais!")
                break

            else:
                print(f"Opção inválida ou sem funcionamento ainda!")

