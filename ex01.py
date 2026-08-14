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

# Função responsável por somar dois valores
def somar(valor1, valor2):
    return valor1 + valor2


# Função responsável por subtrair dois valores
def subtrair(valor1, valor2):
    return valor1 - valor2


# Função responsável por multiplicar dois valores
def multiplicar(valor1, valor2):
    return valor1 * valor2


# Função responsável por dividir dois valores
def dividir(valor1, valor2):

    # Verifica se o segundo valor é zero
    if valor2 == 0:
        return None

    return valor1 / valor2


# Função responsável por receber os valores digitados pelo usuário
def ler_valor(mensagem):

    # Continua pedindo o valor até o usuário digitar um número válido
    while True:

        try:
            # Converte o valor digitado para float
            return float(input(mensagem))

        except ValueError:
            # Mensagem exibida caso o usuário digite um valor inválido
            print("Valor inválido! Digite um número.")


# Função principal do programa
def main():

    # Mantém o programa funcionando até o usuário escolher sair
    while True:

        # Exibe o menu da calculadora
        print("\n===== CALCULADORA =====")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair")
        print("=======================")

        # Recebe a opção escolhida pelo usuário
        opcao = input("Escolha uma opção: ")

        # Encerra o programa caso o usuário escolha 5
        if opcao == "5":
            print("Calculadora encerrada!")
            break

        # Verifica se a opção escolhida é válida
        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida! Escolha uma opção de 1 a 5.")
            continue

        # Solicita o primeiro valor
        valor1 = ler_valor("Digite o primeiro valor: ")

        # Solicita o segundo valor
        valor2 = ler_valor("Digite o segundo valor: ")

        # Realiza a soma
        if opcao == "1":
            resultado = somar(valor1, valor2)
            print(f"Resultado: {resultado}")

        # Realiza a subtração
        elif opcao == "2":
            resultado = subtrair(valor1, valor2)
            print(f"Resultado: {resultado}")

        # Realiza a multiplicação
        elif opcao == "3":
            resultado = multiplicar(valor1, valor2)
            print(f"Resultado: {resultado}")

        # Realiza a divisão
        elif opcao == "4":
            resultado = dividir(valor1, valor2)

            # Verifica se houve tentativa de divisão por zero
            if resultado is None:
                print("Erro: não é possível dividir por zero!")
            else:
                print(f"Resultado: {resultado}")


# Inicia o programa chamando a função principal
main()