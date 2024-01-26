def Calculadora(valor1=1, valor2=1, operacao="1"):
    if operacao == "1":
        return(f"Soma {valor1} e {valor2} é {valor1 + valor2}")
    if operacao == "2":
        return(f"Subtração {valor1} e {valor2} é {valor1 - valor2}")
    if operacao == "3":
        return(f"Multiplicação {valor1} e {valor2} é {valor1 * valor2}")
    if operacao == "4":
        return(f"Divisão {valor1} e {valor2} é {valor1 / valor2}")
    else:
        return(f"Valor indicado para operação é inválido")
    
def Calculadora2(*, valor1=1, valor2=1, operacao="1"):
    if operacao == "1":
        return(f"Soma {valor1} e {valor2} é {valor1 + valor2}")
    if operacao == "2":
        return(f"Subtração {valor1} e {valor2} é {valor1 - valor2}")
    if operacao == "3":
        return(f"Multiplicação {valor1} e {valor2} é {valor1 * valor2}")
    if operacao == "4":
        return(f"Divisão {valor1} e {valor2} é {valor1 / valor2}")
    else:
        return(f"Valor indicado para operação é inválido")

print(Calculadora())
print(Calculadora(valor1=2,valor2=2,operacao="2"))

print(Calculadora2(valor2=1))

