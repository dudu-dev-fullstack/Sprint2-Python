regioes = []
temperaturas = []

def mostrar_menu():
    print("\n========== MENU ==========")
    print("1 - Sobre o projeto")
    print("2 - Cadastrar região")
    print("3 - Listar regiões")
    print("4 - Analisar temperaturas")
    print("5 - Relatório")
    print("0 - Sair")
    print("==========================")

def sobre_projeto():
    print("\n===== SOBRE O PROJETO =====")
    print("Sistema inspirado em tecnologias espaciais.")
    print("O objetivo é monitorar regiões com")
    print("temperaturas elevadas e riscos climáticos.")
    print("A solução ajuda no acompanhamento")
    print("de possíveis desastres naturais.")

def cadastrar_regiao():

    nome = input("\nDigite o nome da região: ")

    temperatura = float(input("Digite a temperatura da região: "))

    regioes.append(nome)
    temperaturas.append(temperatura)

    print("Região cadastrada com sucesso!")

def listar_regioes():

    print("\n===== REGIÕES CADASTRADAS =====")

    for i in range(len(regioes)):

        print("\nRegião:", regioes[i])
        print("Temperatura:", temperaturas[i], "°C")

def analisar_temperaturas():

    print("\n===== ANÁLISE DE RISCO =====")

    for i in range(len(regioes)):

        print("\nRegião:", regioes[i])

        if temperaturas[i] >= 40:
            print("Risco ALTO de desastre climático!")

        elif temperaturas[i] >= 30:
            print("Risco MÉDIO de desastre climático!")

        else:
            print("Risco BAIXO de desastre climático!")


def relatorio():

    print("\n===== RELATÓRIO =====")

    print("Quantidade de regiões cadastradas:", len(regioes))

    soma = 0

    for temp in temperaturas:
        soma = soma + temp

    if len(temperaturas) > 0:

        media = soma / len(temperaturas)

        print("Média das temperaturas:", media)

    else:
        print("Nenhuma temperatura cadastrada.")


opcao = -1

while opcao != 0:

    mostrar_menu()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        sobre_projeto()

    elif opcao == 2:
        cadastrar_regiao()

    elif opcao == 3:
        listar_regioes()

    elif opcao == 4:
        analisar_temperaturas()

    elif opcao == 5:
        relatorio()

    elif opcao == 0:
        print("\nSistema encerrado.")

    else:
        print("\nOpção inválida!")