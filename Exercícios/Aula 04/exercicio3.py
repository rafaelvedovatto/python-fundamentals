# =============================================================
# 3) Crie um programa que pergunte para o usuario um numero de pessoas a participarem de um sorteio (2-20),
#  e o numero de pessoas a serem sorteadas, e depois sorteie esse numero de pessoas da lista.

# O programa deverá pegar o numero de pessoas a participar aleatoriamente desta lista:

# lista = ["Joao", "Maria", "Tiago", "Amanda", "Emanuele", "Caio", "Suzana", "Miguel", 
# "Rosangela", "Rian", "Lucimar", "Ulisses", "Leonardo", "Kaique", "Bruno", "Raquel", 
# "Benedito", "Tereza", "Valmir", "Joaquim"]

# Nota: A mesma pessoa não pode ganhar duas vezes.

import random
from exercicio2_func import LimpaTela

def RealizaSorteio(lista,num_pessoas,num_sorteios):
    LimpaTela()
    participantes = random.sample(lista, num_pessoas)
    print("Lista de participantes:")
    for nome in participantes:
        print(f" - {nome}")
    if num_sorteios > num_pessoas:
        print(f"Foi informado {num_sorteios} soreios mas apenas {num_pessoas} partcipantes. Sobrará {num_sorteios - num_pessoas} brinde(s).")
    ganhadores = random.sample(participantes,num_sorteios)
    print("O(s) granhado(res) é(são):")
    for ganhador in ganhadores:
        print(f" - {ganhador}")


def main():
    lista = ["Joao", "Maria", "Tiago", "Amanda", "Emanuele", "Caio", "Suzana", "Miguel", 
             "Rosangela", "Rian", "Lucimar", "Ulisses", "Leonardo", "Kaique", "Bruno", "Raquel", 
             "Benedito", "Tereza", "Valmir", "Joaquim"]
    while True:
        LimpaTela()
        num_pessoas = int(input("Quantas pessoas vão participar do sorteio? (2-20) "))
        num_sorteios = int(input("Quantas sorteio serão realizados? "))
        if (num_pessoas >= 2 and num_pessoas <= 20) and num_pessoas > num_sorteios:
            RealizaSorteio(lista,num_pessoas,num_sorteios)
            break
        else:
            LimpaTela()
            print("Opção inválida. Responda novamente. ")
            input("")

if __name__ == '__main__':
    main()


