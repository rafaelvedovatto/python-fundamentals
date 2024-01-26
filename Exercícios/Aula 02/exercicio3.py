# ======================================================================================================
# 3) Escreva um script em python que represente uma quitanda. O seu programa deverá
# apresentar as opções de frutas, e a cada vez que você escolher a fruta desejada, a fruta
# deverá ser adicionada a uma cesta de compras.

# Menu principal:

# Quitanda:
# 1: Ver cesta
# 2: Adicionar frutas
# 3: Sair

# Menu de frutas:
# Digite a opção desejada:
# Escolha fruta desejada:
# 1 - Banana
# 2 - Melancia
# 3 - Morango

# Digite à opção desejada: 2
# Melancia adicionada com sucesso!

# Os menus 1 e 2 deverão retornar ao menu principal após executar as suas tarefas.
# Você deverá validar as opções digitadas pelo usuário (caso ele digitar algo errado, a mensagem:
# Digitado uma opção inválida

# O programa deverá ser encerrado apenas se o usuário digitar a opção 3.

exercicio = 3
print(f"Exercício {exercicio}")

cesta = []

while True:
    print("""
        # Menu principal:
        # Quitanda:
        # 1: Ver cesta
        # 2: Adicionar frutas
        # 3: Sair
      """)
    opc_menu_principal=input("# Digite à opção desejada: ")
    if opc_menu_principal == "1":
        if len(cesta) == 0:
            print("Cesta está vazia!")
        else:
            for n in range(0, len(cesta)):
                print(cesta[n])
    elif opc_menu_principal == "2":
        while True:
            print("""
                # Menu de frutas:
                # Escolha fruta desejada:
                # 1 - Banana
                # 2 - Melancia
                # 3 - Morango
                """)
            opc_menu_frutas = input("# Digite à opção desejada: ")
            if opc_menu_frutas == "1":
                fruta = "Banana"
                if cesta.count(fruta) == 0:
                    cesta.append(fruta)
                    print(f"{fruta} adicionada com sucesso!")
                break
            elif opc_menu_frutas == "2":
                fruta = "Melancia"
                if cesta.count(fruta) == 0:
                    cesta.append(fruta)
                    print(f"{fruta} adicionada com sucesso!")
                break
            elif opc_menu_frutas == "3":
                fruta = "Morango"
                if cesta.count(fruta) == 0:
                    cesta.append(fruta)
                    print(f"{fruta} adicionada com sucesso!")
                break
            else:
                print("Opção incorreta. Voltando ao menu inicial.")
                break
    elif opc_menu_principal == "3":
        print("Tchau!")
        break
    else:
        print("Opção inválida. Selecione outra opção ou 3 para sair.")
