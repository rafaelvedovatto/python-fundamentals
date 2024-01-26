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

import os

def LimpaTela():
    os.system('cls')

def AdicionaPessoa(dic):
    nome = input("Infome o nome a ser adicionado: ")
    idade = input("Informe a idade: ")
    dic[nome]=str(idade)
    LimpaTela()
    print(f"{nome} foi adicionado. ")

def ProcessaDados(dic,opc=1):
    idade0017 = 0
    idade1859 = 0
    idade60 = 0
    nomes0017=[]
    nomes1859=[]
    nomes60=[]
    for x, y in dic.items():
        if int(y) <= 17:
            idade0017 += 1
            nomes0017.append(x)
        elif int(y) >=18 and int(y) <= 59:
            idade1859 += 1
            nomes1859.append(x)
        else:
            idade60 += 1
            nomes60.append(x)
    if opc == 1:
        LimpaTela()
        print(f"""
    0-17 anos: Menor de idade {idade0017} \n
    18-59 anos: Adulto        {idade1859} \n
    60+ anos: Idoso           {idade60} \n
            """)
    if opc == 2:
        msg = PrintaNomes(nomes0017)
        print(f"Nomes na faixa etária de 0 à 17 anos: {msg}")
        msg = PrintaNomes(nomes1859)
        print(f"Nomes na faixa etária de 0 à 17 anos: {msg}")
        msg = PrintaNomes(nomes60)
        print(f"Nomes na faixa etária de 0 à 17 anos: {msg}")
        
def PrintaNomes(lista):
    nomes = ""
    if len(lista) == 0:
        return "não foi informado nenhuma pessoa nessa faixa etária"
    else:
        for chave in lista:
            print(chave)
            nomes = nomes + " " + chave
            print(nomes)
        return nomes.rstrip()
