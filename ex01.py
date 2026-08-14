###################################################
# Aplicativo Modelo                               #
# `agenda_furreca.py` → Link                      #
# Fazer os desafios BÁSICO e INTERMEDIÁRIO → Link #
# Exercício - Criação de aplicativo               #
###################################################

def somar(valor1, valor2):
    return valor1 + valor2


def subtrair(valor1, valor2):
    return valor1 - valor2


def multiplicar(valor1, valor2):
    return valor1 * valor2


def dividir(valor1, valor2):
    if valor2 == 0:
        return None
    return valor1 / valor2


def ler_valor(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido! Digite um número.")


def main():

    while True:

        print("\n===== CALCULADORA =====")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair")
        print("=======================")

        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Calculadora encerrada!")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida! Escolha uma opção de 1 a 5.")
            continue

        valor1 = ler_valor("Digite o primeiro valor: ")
        valor2 = ler_valor("Digite o segundo valor: ")

        if opcao == "1":

            resultado = somar(valor1, valor2)
            print(f"Resultado: {resultado}")

        elif opcao == "2":

            resultado = subtrair(valor1, valor2)
            print(f"Resultado: {resultado}")

        elif opcao == "3":

            resultado = multiplicar(valor1, valor2)
            print(f"Resultado: {resultado}")

        elif opcao == "4":

            resultado = dividir(valor1, valor2)

            if resultado is None:
                print("Erro: não é possível dividir por zero!")
            else:
                print(f"Resultado: {resultado}")


main()