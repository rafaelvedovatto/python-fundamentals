# from random import randint

# print(radint(0,10))

# print(randint(4,15))

# função soma 2 números
def func(a, b):
    pass #sinaliza pro interpretador que não tem nada pra executar - tipo BR14 :)

# função soma 2 números
def adicao(num1, num2):
    adicao = num1 + num2
    return adicao

print(adicao(1,2))

# Funções Anônimas
# O Python nos permite criar funções e armazená-las em variáveis. A essa modalidade de uso
# da funções é denominada funções anônimas. É anônima por duas razões:
#   1. Pela ausência de uma definição formal de função, com clausula def
#   2. Pela capacidade de não ser associado à qualquer nome ou símbolo, e ser armazenado
#      em qualquer variável, desde que respeitado as palavras reservadas da linguagem
# Para criar uma função dessa forma, utiliza-se a palavra chave lambda. Veja a seguir um exemplo
# de função anônima para a função soma:

soma = lambda x,y: x + y
print(soma(1,1))

# O uso de funções anônimas está ligado ao paradigma funcional o qual o Python incorpora
# algumas de suas características. Iremos abordar algumas de suas características no último
# capítulo desta apostila.


# Modularização de código:

# 1. Capturar dois números
# 2. Apresentar as opções de cálculo (+ ; - ; / e *)
# 3. Escolher uma opção
# 4. realizar o cálculo de acordo com a opção
# 5. apresentar o resultado
# Como a ideia é modularizar o nosso código, iremos criar:
# • Uma função para cada operação
# • Uma função principal para controlar o fluxo da aplicação

def somar(a,b):
    resultado = a + b
    return resultado

def subtrair(a,b):
    resultado = a-b
    return resultado

def divisao(a,b):
    if b == int(b):
        print("Divisão por 0 da ruim champs!")
        return
    resultado = a/b
    return resultado

def multiplicacao(a,b):
    resultado = a*b
    return resultado

# a = 1
# b = 0

# print(somar(a,b))
# print(subtrair(a,b))
# print(divisao(a,b))
# print(multiplicacao(a,b))

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


