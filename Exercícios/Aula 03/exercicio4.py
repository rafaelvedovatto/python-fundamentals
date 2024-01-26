from random import randint

# ====================================================
# Exercicio 4:
# Escreva um programa que possua uma função que conte o
# numero de números pares passados à ela, pelo usuário.

def Numeros_pares(lista):
    total = 0
    for i in range(0,len(lista)):
        if int(lista[i]) % 2 == 0:
            total += 1
    return total

# def Numero_aleatorio():
#     num = str(randint(0,999))
#     return num
    
def CriaListaAleatoria():
    i=0
    aux_lista = []
    while i < 20:
        aux_lista.append(str(randint(1,999)))
        i += 1
    return aux_lista

def main():
    
    # lista_num = []

    # j=0

    # while j <= 20:
    #     print(j)
    #     lista_num.append(Numero_aleatorio())
    #     j += 1

    # lista_num.sort()

    # print(lista_num)

    # a=[]
    # a.copy(CriaListaAleatoria())
    a = CriaListaAleatoria()

    print(a)

    print(f"Total de números pares é: {Numeros_pares(a)}")

    # numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    # print(f"Total de números pares é: {Numeros_pares(numeros)}")
    
if __name__ == '__main__':
    main()


