# Exercicio 1:
# Escreva uma função que receba um nome e que tenha como saída uma saudação.

# O argumento da função deverá ser o nome, e saída deverá ser como a seguir:

# chamada da função: saudacao('Lalo')
# saída: 'Olá Lalo! Tudo bem com você?'

def ola(nome):
    print(f"Olá {nome}! Tudo bem com você?")
#    return

def main():
    nome = input("Oi! Qual é o seu nome? ")
    ola(nome)


if __name__ == '__main__':
    main()


