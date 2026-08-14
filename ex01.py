
###################################################
# Exercício - Criação de Aplicativo               #
#                                                 #
# Aplicativo: Calculadora                         #
#                                                 #
# Operações disponíveis:                          #
# - Soma                                          #
# - Subtração                                     #
# - Multiplicação                                 #
# - Divisão                                       #
#                                                 #
# Turma: 2026.3                                   #
# Aluno: Vitor Assis                              #
###################################################

import os

# Função para limpar a tela
def limpar_tela():
    os.system("cls")


# Função para somar
def somar(valor1, valor2):
    return valor1 + valor2


# Função para subtrair
def subtrair(valor1, valor2):
    return valor1 - valor2


# Função para multiplicar
def multiplicar(valor1, valor2):
    return valor1 * valor2


# Função para dividir
def dividir(valor1, valor2):

    # Não permite divisão por zero
    if valor2 == 0:
        return None

    return valor1 / valor2


# Função para receber valores
def ler_valor(mensagem):

    while True:

        try:
            return float(input(mensagem))

        except ValueError:
            print("Valor inválido! Digite um número.")


# Função principal
def main():

    while True:

        limpar_tela()

        print("===== CALCULADORA =====")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair")
        print("=======================")

        opcao = input("Escolha uma opção: ")

        # Opção para sair
        if opcao == "5":
            print("Calculadora encerrada!")
            break

        # Verifica se a opção é válida
        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida!")
            input("\nPressione ENTER para continuar...")
            continue

        # Entrada dos valores
        valor1 = ler_valor("Digite o primeiro valor: ")
        valor2 = ler_valor("Digite o segundo valor: ")

        # Soma
        if opcao == "1":
            resultado = somar(valor1, valor2)
            print(f"\nResultado: {resultado}")

        # Subtração
        elif opcao == "2":
            resultado = subtrair(valor1, valor2)
            print(f"\nResultado: {resultado}")

        # Multiplicação
        elif opcao == "3":
            resultado = multiplicar(valor1, valor2)
            print(f"\nResultado: {resultado}")

        # Divisão
        elif opcao == "4":
            resultado = dividir(valor1, valor2)

            if resultado is None:
                print("\nErro: não é possível dividir por zero!")
            else:
                print(f"\nResultado: {resultado}")

        # Aguarda o usuário apertar ENTER antes de voltar ao menu
        input("\nPressione ENTER para voltar ao menu...")


# Inicia o programa
main()