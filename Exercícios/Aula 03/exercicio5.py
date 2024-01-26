# ====================================================
# Exercicio 5:
# Assumindo que uma lata de tinta pinta 3m², escreva um programa
# que possua uma função que receba as dimenções de uma parede,
# passadas pelo usuario, calcule sua área, e mostre uma mensagem
# dizendo quantas latas de tinta seriam necessárias para pintar
# essa parede.

import math

def main():
    
    m_por_lata = 3
    
    altura = float(input("Informe a altura da parede: "))
    
    largura = float(input("Informe a largura da parede: "))

    calc_area = lambda altura,largura:altura*largura

    area = calc_area(altura,largura)

    #qtd_tinta = lambda altura,largura,m_por_lata:(altura*largura)/m_por_lata

    qtd_tinta = lambda area,m_por_lata:area/m_por_lata

    print(f"Serão necessárias {math.ceil(qtd_tinta(area,m_por_lata))} latas de tinta para printar {area}m² de parede.")


if __name__ == '__main__':
    main()

