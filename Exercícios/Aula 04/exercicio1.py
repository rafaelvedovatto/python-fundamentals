# 1) Escreva um programa em Python que simule uma dança das cadeiras. Você deverá
# importar o pacote random e iniciar uma lista com nomes de pessoas que participariam da
# brincadeira. O jogo deverá iniciar com 9 cadeiras e 10 participantes. A cada rodada,
# uma cadeira deverá ser retirada e um dos jogadores, de forma aleatória, ser eliminado. O
# jogo deverá terminar quando apenas restar uma cadeira e ao final de todas as rodadas,
# deverá ser apresentado vencedor.

# Dica: [OPCIONAL] Você poderá utilizar o modulo "time" para simular um tempo de a cada rodada para criar
# um efeito mais interessante.

# Dica: [OPCIONAL] Tentem fazer a remoção de uma pessoa aleatória por rodada sem utilizar a função "choice".

import os
import random
import time

lista_participantes = ["Rafael", "Lívia", "Goku", "Gohan", "Joel Santana", "Sulian", "Tafarel", "Timão", "Pumba", "Jonas"]

def NumAleatorio(min,max):
    num = random.randint(min,max)
    print(num)
    return num

def RemovePessoa(proxima_vitima):
    print(f"{lista_participantes[proxima_vitima]} foi eliminado da brincadeira.")
    lista_participantes.pop(proxima_vitima)

def ImprimeParticipantes():
    print(f"Participantes: {lista_participantes}")

def main():
    num_cadeiras = 9
    participantes = 9
    rodada = 1
    
    while True:
        print(f"Rodada número: {rodada}")
        ImprimeParticipantes()
        time.sleep(random.randint(2,10))
        proxima_vitima = NumAleatorio(0,participantes)
        RemovePessoa(proxima_vitima)
        #print(lista_participantes,proxima_vitima)
        participantes -= 1
        rodada += 1
        if len(lista_participantes) == 1:
            print(lista_participantes[0])
            break
        print("Indo para próxima rodada")
        time.sleep(1)
        os.system('cls')
    
if __name__ == '__main__':
    main()