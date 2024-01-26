# =============================================================
# 2) Crie um programa utilizando dois arquivos, onde um deles possui todas as funcçoes utilizadas na aplicação.
# Onde o programa deverá perguntar ao usuario nome/idade de uma pessoa, e armazenar esses valores em um dicionario,
# e repetir essa ação até que a pessoa não queira mais adicionar nomes, em seguida, o programa deverá mostrar o numero
# de pessoas em categorias de acordo com a idade:
# 0-17 anos: Menor de idade
# 18-59 anos: Adulto
# 60+ anos: Idoso
# E deverá perguntar para o usuario se ele gostaria de exibir na tela uma lista com os nomes das pessoas de cada grupo,
# ou se o usuario deseja finalizar o programa.

import exercicio2_func
import os

dic = {}

def main():
    
    while True:
        #exercicio2_func.AdicionaPessoa(nome,idade,dic)
        exercicio2_func.AdicionaPessoa(dic)
        print(dic)
        opc = str.lower(input("Deseja inserir mais nomes a lista? (s/n) "))
        exercicio2_func.LimpaTela()
        if opc == "s":
            pass #executa nada, volta pro loop
        elif opc == "n":
            exercicio2_func.ProcessaDados(dic)
            opc2=str.lower(input("Você gostaria de ver os nomes pertencentes a cada faixa etária? (s/n)"))
            if opc2 == "s":
                exercicio2_func.ProcessaDados(dic,opc=2)
            elif opc2 == "n":
                print("Tchau!")
            else:
                print("Opção inválida. Saindo do programa.")
            break
        else:
            print("Opção inválida. Saindo do programa.")
            break

if __name__ == '__main__':
    main()


