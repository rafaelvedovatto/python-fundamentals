# ====================================================
# Exercicio 3:
# Reescreva o exercício da quitanda do capítulo 2 separando as operações 
# em funções.


def Menu_principal():
    print("""
            # Menu principal:
            # Quitanda:
            # 1: Ver cesta
            # 2: Adicionar frutas
            # 3: Sair
        """)
    opc_menu_principal=input("# Digite à opção desejada: ")
    return opc_menu_principal
    
def Menu_frutas():
    print("""
            # Menu de frutas:
            # Escolha fruta desejada:
            # 1 - Banana
            # 2 - Melancia
            # 3 - Morango
        """)
    opc_menu_frutas = input("# Digite à opção desejada: ")
    return opc_menu_frutas

def Lista_cesta(cesta,total):
    if len(cesta) == 0:
        print("Cesta está vazia!")
        print(f"Valor total: {total}")
    else:
        for n in range(0, len(cesta)):
            print(cesta[n])
        print(f"Valor total: {total}")
    return 

def Adiciona_fruta(cesta,fruta,tabela_preco):
    if cesta.count(fruta) == 0:
        cesta.append(fruta)
        preco = int(tabela_preco[fruta])
        print(f"{fruta} adicionada com sucesso!")
    else:
        print(f"{fruta} já adicionada a cesta. ")
        return
    return preco


def main():
    cesta = []
    tabela_preco = {'Banana':'4','Melancia':'6','Morango':'10'}
    total=0
    while True:
        opc_menu_principal = Menu_principal()
        if opc_menu_principal == "1":
            Lista_cesta(cesta,total)

        elif opc_menu_principal == "2":
            while True:
                opc_menu_frutas = Menu_frutas()
                if opc_menu_frutas == "1":
                    fruta = "Banana"
                    total += Adiciona_fruta(cesta,fruta,tabela_preco)
                    print(total)
                    
                elif opc_menu_frutas == "2":
                    fruta = "Melancia"
                    total += Adiciona_fruta(cesta,fruta,tabela_preco)
                    
                elif opc_menu_frutas == "3":
                    fruta = "Morango"
                    total += Adiciona_fruta(cesta,fruta,tabela_preco)
                    
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


if __name__ == '__main__':
    main()


