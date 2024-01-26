import os

# ======================================================================================================
# 4) Altere o exercicio numero 3 para adicionar o preço dos itens comprados, mantendo uma conta do valor
# total gasto nas compras, e no fim, imprima o valor total e os itens na cesta de compras.


exercicio = 4
print(f"Exercício {exercicio}")

cesta = []
tabela_preco = {'Banana':'4','Melancia':'6','Morango':'10'}
total=0

while True:
    print("""
        # Menu principal:
        # Quitanda:
        # 1: Ver cesta
        # 2: Adicionar frutas
        # 3: Sair
      """)
    opc_menu_principal=input("# Digite à opção desejada: ")
    #print(mensagem)
    if opc_menu_principal == "1":
        if len(cesta) == 0:
            print("Cesta está vazia!")
            print(f"Valor total: {total}")
        else:
            for n in range(0, len(cesta)):
                print(cesta[n])
            print(f"Valor total: {total}")
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
                    total += int(tabela_preco[fruta])
                    print(f"{fruta} adicionada com sucesso!")
                else:
                    print(f"{fruta} já adicionada a cesta. ")
            elif opc_menu_frutas == "2":
                fruta = "Melancia"
                if cesta.count(fruta) == 0:
                    cesta.append(fruta)
                    total += int(tabela_preco[fruta])
                    print(f"{fruta} adicionada com sucesso!")
                else:
                    print(f"{fruta} já adicionada a cesta. ")
            elif opc_menu_frutas == "3":
                fruta = "Morango"
                if cesta.count(fruta) == 0:
                    cesta.append(fruta)
                    total += int(tabela_preco[fruta])
                    print(f"{fruta} adicionada com sucesso!")
                else:
                    print(f"{fruta} já adicionada a cesta. ")
            else:
                print("Opção incorreta. Voltando ao menu inicial.")
                break
            break
    elif opc_menu_principal == "3":
        if total > 0:
            print(f"Valor total da compra: {total}")
        print("Tchau!")
        break
    else:
        print("Opção inválida. Selecione outra opção ou 3 para sair.")


