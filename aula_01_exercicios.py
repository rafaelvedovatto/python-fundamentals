# 1) Em muitos programas, nos é solicitado o preenchimento de algumas informações como
# nome, CPF, idade e unidade federativa. Escreva um script em Python que solicite as
# informações cadastrais mencionadas e que em seguida as apresente da seguinte forma:

# -----------------------------
# Confirmação de cadastro:
# Nome: Guido Van Rossum
# CPF: 999.888.777/66
# Idade: 65
# -----------------------------

cabecalho = "# -----------------------------"

nome = input("Informe o seu nome: ")
cpf = input("Informe o seu CPF ")
idade = input("Informe a sua idade: ")

mascara = '%s%s%s.%s%s%s.%s%s%s-%s%s'
cpfmask = mascara % tuple(cpf)

print(cabecalho)
print(f"Nome: {nome}")
print(f"CPF: {cpfmask}")
print(f"Idade: {idade}.")
print(cabecalho)


# 2) Escreva um script em Python que receba dois números e que seja realizado as seguintes
# operações:
# • soma dos dois números
# • diferença dos dois números
# O resultado deverá ser apresentado conforme a seguir - no exemplo foram digitados os números
# 4 e 2:

# ------------------------------
# Soma: 4 + 2 = 6
# Diferença: 4 - 2 = 2

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

print(cabecalho)
print(f"Soma: {a} + {b} = {a+b}")
print(f"Diferença: {a} - {b} = {a-b}")
print(cabecalho)
