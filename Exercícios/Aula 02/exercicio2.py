# ======================================================================================================
# 2) Escreva um programa que receba o ano de nascimento, e que ele retorne à geração
# a qual a pessoa pertence. Para definir a qual geração uma pessoa pertence temos a
# seguinte tabela:

# Geração        Intervalo

# Baby Boomer -> Até 1964
# Geração X   -> 1965 - 1979
# Geração Y   -> 1980 - 1994
# Geração Z   -> 1995 - Atual

# Para testar se seu script está funcionando, considere os seguintes resultados esperados:

# • ano nascimento = 1988: Geração: Y
# • ano nascimento = 1958: Geração: Baby Boomer
# • ano nascimento = 1996: Geração: Z

exercicio = 2
print(f"Exercício {exercicio}")

ano = int(input('Qual o seu ano de nascimento? '))

if ano <= 1964:
    gen = "Baby Boomer"
elif ano <= 1979:
    gen = "X"
elif ano <= 1994:
    gen = "Y"
else:
    gen = "Z"

mensagem = "Ano de nascimento = " + str(ano) + ": Geração: " + gen

print(mensagem)

