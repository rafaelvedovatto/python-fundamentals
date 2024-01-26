a = 5
b = 6

if a > b:
    print(f"{a} é maior que {b}")
else:
    print(f"{a} é menor do que {b}")

a = 6
b = 5

if a < b:
    print(f"{a} é menor do que {b}")
else:
    print(f"{a} é maior que {b}")

nome = "Rafael"
if nome == "Jonas":
    print(f"Meu nome é {nome} ")
else:
    print(f"Meu nome não é Jonas")


nota1 = 5
nota2 = 7.6
nota3 = 8.2
media = (nota1+nota2+nota3)/3
if media > 6:
    print("Aprovado")
elif media >= 4:
    print("Em recuperação")
else:
    print("Reprovado paquitão!")