# ====================================================
# Exercicio 2:
# Escreva uma calculadora utilizando funções
# Ela pergunta dois numeros, e da as opções de calculo.
# (soma, diferença, multiplicação, divisão)

def somar(a,b):
    resultado = a + b
    return resultado

def subtrair(a,b):
    resultado = a-b
    return resultado

def divisao(a,b):
    if b == 0:
        return "Divisão por 0 da ruim champs!"
    else:
        resultado = a/b
        return resultado

def multiplicacao(a,b):
    resultado = a*b
    return resultado

def main():
    n1=float(input("Digite o primeiro número: "))
    n2=float(input("Digite o segundo número: "))

    opcao = input('Digite a opção desejada:\n 1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir')

    if opcao == '1':
        print(somar(n1,n2))
    elif opcao == '2':
        print(subtrair(n1,n2))
    elif opcao == '3':
        print(multiplicacao(n1,n2))
    elif opcao == '4':
        print(divisao(n1,n2))
    else:
        print('Opcao Inválida')

if __name__ == '__main__':
    main()