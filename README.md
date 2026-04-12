[![Python Tests](https://github.com/Kyon-S2/BootCampII/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Kyon-S2/BootCampII/actions/workflows/python-tests.yml)

# Nome do Projeto


*Control of exaggerations*


## O que é esse projeto?


*- Esse projeto é um sistema em que pessoas conseguem controlar seus gastos, ajudando-as a adminstrarem melhor suas finanças.*

**Qual a dor que o meu software pretende minimizar ou resolver?**

*- Pessoas devendo em seus cartões por não saberem como estão seus gastos e com isso tendo que pedir dinheiro a alguém pra conseguir pagar, mas criando uma outra dívida fazendo uma bola de neve com a situação. -*


**Público-Alvo?**

*- Qualquer pessoa que queira ter um controle sobre seus gastos, mas sendo mais específico, aquela pessoa que usa o cartão além do limite e no fim não tem dinheiro para pagar e se individa e começa a ter dificuldades com os juros. . -*


**De qual forma meu software ajuda essas pessoas?**

*- Meu software pretende ajudar essas pessoas a controlarem seus gastos através de um CLI (interface na tela preta), onde as pessoas conseguem armazenar suas dívidas ou excluirem, colocando valor, data, tipo de dívida e etc, mantendo assim um armazenamento dos seus gastos e obtendo um certo controle com eles. -*


**Fluxo de Uso claro e funcional ?**

*- 1. Pessoa entra no sistema, coloca a sua dívida e salva ela. 2. O sistema vai armazenar isso e guardar mostrando para ela o valor total da dívida e uma tabela dos gastos. 3. Caso a pessoa queira ou ja tenha pago a dívida ela será possibilitada de excluir a dívida. 4. A pessoa pode consultar sua dívida a qualquer momento. -*


**Principais Funcionalidades**

*Cadastro de Gastos, Exclusão de gastos, Atualização de Gastos(Em breve!), Criação do relatório e saída do sistema.*


**Tecnologias utilizadas**

*Vscode com python(Escrever, organizar e estruturar o código) | Python(v3.14.3) | JSON(banco de dados) | Pytest(testes) | Ruff(lint) | Formatação Manual(para criar o menu principal e etc) | tabulate (criar as tabelas) | Git | Github | Github Actions(CI - Integração contínua) | venv(ambiente virtual para isolar as bibliotecas do projeto e não conflitarem com outras coisas do computador) | pip (gerenciador do python para instalações e lista de dependência.).*


### Instruções de Instalação e Execução:**


**1. Baixe o Python 3.14.3**

*"Baixe a extensão do python no vscode"*

*As que tenho baixado!*

![alt text](<img/Captura de tela 2026-04-12 173429.png>)


**2. Clone o repositório com os seguintes comandos:**

*-Git clone https://github.com/Kyon-S2/BootCampII.git-*
*-cd BootCampII-*


**3. Configure o ambiente virtual(.venv)**

*No bash. No meu caso, usei o terminal bash no vscode. Use esses comandos nele!*

*Windows*

*-python -m venv .venv-*
*-.venv\Scripts\Activate-*

*Linux/Mac*

*-python3 -m venv .venv-*
*-source .venv/bin/activate-*


**4. Instalar as dependências**

*No bash use:*

*-pip install -r requirements.txt-*


**5. Por fim, para executar o sistema use no bash(terminal), com o .venv ativo!!!:**

*python -m app.main*


**Avisos**

*Ao salvar o seu primeiro gasto, será criado um arquivo chamado: gastos.json, que nesse caso é onde serão armazenados os seus gastos!*

*Usei o vscode para fazer o projeto, então de preferência execute nele!*


### Como rodar os testes???


*Para rodar os testes primeiro verifique se no seu bash o ambiente virtual está ativo (.venv)!*

*Após isso basta rodar o seguinte comando no bash:*

*-Pytest-*


### Como rodar o Lint?


*Para rodar o lint verifique se no bash o ambiente virtual também está ativo (.venv)*

*Após isso use o seguintes comandos no bash:*

*-Ruff check .-* para fazer o teste de lint!

*Ruff check . --fix* para corrigir automaticamente!

**Ambos os testes funcionam automaticamente pelo Github Actions (CI/CD)**


### Versão Atual: 1.0.


### Autor: Felipe


### Link do Repositório: https://github.com/Kyon-S2/BootCampII

### Testes imagens!

**Teste de exclusão com persistência**

![alt text](<img/Captura de tela 2026-04-12 154403.png>)

![alt text](<img/Captura de tela 2026-04-12 154435.png>)

### Sistema funcionando!!!

![alt text](<img/Captura de tela 2026-04-12 180108.png>)

![alt text](<img/Captura de tela 2026-04-12 180155.png>)

![alt text](<img/Captura de tela 2026-04-12 180211.png>)

![alt text](<img/Captura de tela 2026-04-12 180242.png>)

### Referências e IA!

**Estou usando a Inteligência Artificial (GEMINI) para me auxiliar na criação do projeto,  tanto em questões como código (guiar e criando para uso), como para estudo e entendimento do conteúdo,e para o que for necessário!**

**Também usei os conheimentos fornecidos pelo meu professor para criar o sistema, uma vez que ao ver seu vídeo na aula mostrando o sistema feito por ele achei interessante de ser feito e bem útil.**

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Extra!

### Comandos para uso!

**Criar versionamento com tags:** 

*- Use após o commit -*

git tag -a v0.0.0 -m "Escreva"
git push origin v0.0.0

No lugar do v0.0.0 coloque a versão que você está dando!