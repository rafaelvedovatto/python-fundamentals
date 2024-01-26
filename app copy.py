# comentário

print('Hey fucker!')

# variáveis
nome = "Rafael Bindillati"
nome2 = 'Rafael Bindillati'
print(nome, nome2)

# Input é usado para coletar informações do usuário
x = input("Qual é o seu nome? ")
print(x)

# tb pode ser feito assim mas aí não armazena o que foi inputado pelo usuário. só imprime o que foi recebido.
# print(input("Qual é o seu nome? "))

print("Bem vindo", x)

print("Bem vindo", x,"ratata", x)

# f string (formatted string) - usado para imprimir strings com variáveis no meio
# Isso é muito útil para que você não tenha que ficar concatenando o seu texto com as variáveis e tenha que fatiar seu texto várias vezes por conta disso.
# print(f"Bem vindo {x} {nome} {nome2}")
# print("Bem vindo {} {} {}".format(x,nome,nome2))

# tipo primitivos
# String = str = string :)
# Float = float = números reais
# Integer = int = números inteiros
# Boolean = bool = True ou False

variavel_str = "Avião azul"
variavel_str2 = "está caindo"
variavel_str3 = "40"
variavel_float = 25.7
variavel_int = 9
variavel_boolean = False

print(variavel_str,variavel_float,variavel_int,variavel_boolean)

print(variavel_str + variavel_str2) # concatena a string (remove o espaço entre elas)
print(variavel_str, variavel_str2)  # imprime com espaço entre elas
print(variavel_float+variavel_int)  # soma os valores


