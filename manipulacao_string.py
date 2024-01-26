texto = "python"
caixaalta = texto.upper()
print(texto,caixaalta)

texto = "Olá,meu,nome,é,Rafael"
semvirgula=texto.split(',')
print(semvirgula)

texto = '    Oi!'
espacoesquerda = texto.lstrip()
print(espacoesquerda)

texto = 'Oi!   '
espacodireita = texto.rsplit()
print(espacodireita)

texto = "Olá tudo  bem ?   "
espacos = texto.split()
print(espacos)

replace = texto.replace('?','paquitão?')
print(replace)

idade=4384384
nome="Tchulu"
print("Olá, meu nome é {}, tenho {} anos.".format(nome,idade))

# %s é usado para substituir as variáveis do tipo string
# %d é usado para substituir as variáveis do tipo decimal
print("Olá, meu nome é %s, tenho %d anos." %(nome,idade))

clusters = 3
maquinas = 10
print(f"Temos um total de {clusters * maquinas}" \
      f" máquinas em nosso data center")

mensagem_1='A vingança nunca é plena.'
mensagem_2='Mata a alma e envenena.'
#1: Utilizando o print com valores padrão
print(mensagem_1, mensagem_2)
#2: Alterando o parâmetro de separador
print(mensagem_1, mensagem_2, sep='\n')
#3: Alterando o parâmetro de final do comando
print(mensagem_1, end = ' ')
print(mensagem_2, end = ' fim da mensagem.\n')


# Tupla
# A tupla, diferentemente da lista, não é uma coleção flexível. Uma vez definido os seus valores,
# não é mais possível [1] a sua alteração - isto é, a tupla é um objeto imutável.
# O que significa um objeto ser imutável? Significa que uma vez definido, o objeto não sofrerá
# alterações - caso exista alguma alteração, ele passa a ser um novo objeto [2]. As vantagens
# relacionadas a esse comportamento estão muito direcionadas para o funcionamento interno
# da linguagem [3] - há ganhos de performance quando se define um objeto de tamanho fixo,
# assim sua manipulação é mais previsível e facilita a execução de determinadas tarefas do
# interpretador.

idade = 37

tupla = ("Beterraba", "Mandioca", "Batata", 90, True, idade) # tb pode armazenar variáveis
# index        0          1          2      3    4      5
print(tupla)
print(tupla[0])





#-------------------------------------------------------------------------------------------------------------


# Lista

lista = ["Rafael Bindillati", 46, 55.89]
print(lista[0])

lista.append("Ratata")
lista.insert(9,"Eita")
print(lista)

lista2 = lista # não copia a lista mas cria uma referencia para ela

lista3 = lista.copy()
print(lista3)

lista3.remove("Ratata")
print(lista3)

lista3.pop(1) # remove um item da lista usando o índice e retorna o item que foi movido para aquela posição do índice
print(lista3.pop(1))
print(lista3)
print(len(lista3))



#-------------------------------------------------------------------------------------------------------------


# Dicionário

# Os dicionários, diferentemente dos seus pares tuplas e listas não trabalham com índices.

# Os dicionários podem ser compreendidos como mapeamentos. Para ilustrar, pense em um
# dicionário linguístico: temos os verbetes, e para cada verbete temos um conteúdo descritivo
# relacionado. Não faz sentido algum falar qual o significado do verbete 34567, mas sim, qual
# o significado do verbete “inconstitucionalissimamente”, por exemplo.

# Em Python, e também em outras linguagens de programação, os verbetes são chamados
# de chaves e o conteúdo relacionado aos verbetes, de valor. Nesse sentido, dicionários são
# mapeamentos de chave e valor.

# Se quiséssemos criar um dicionário para armazenar telefones, poderíamos associar nomes com
# números de telefone:

#       Nome   Telefone
#       Joana  55-11-35532443
#       Felipe 55-11-44335533
#       Maria  55-19-99003223

# Pensando em uma estrutura de verbete e conteúdo, se quiséssemos saber o telefone de uma
# pessoa, basta procurar o seu nome para que seja encontrado o seu telefone. Caso fôssemos
# criar um dicionário em Python, teríamos o nome como chave, e telefone como valor.

# A notação utilizada para dicionários em Python são os pares de chaves {}, e associação entre
# chave e valor é mediado pelo caractere ‘:’. Veja abaixo a criação de dicionário para representar
# a lista telefônica acima:

lista_tel = {'Joana':'55-19-0987-6543','Felipe':'55-19-9980-8765','Maria':'55-19-2345-0202'}
print(lista_tel)

# Conforme antecipado, como os dicionários não utilizam índices, o acesso aos seus elementos
# é dado pela indicação de uma chave existente no seu dicionário. Nesse sentido, ao invés de
# informar o índice entre colchetes, será informado a chave em questão:

print(lista_tel['Joana'])

# Adicionar itens ao dicionário

lista_tel['Luciana'] = '55-19-6565-8383'

print(lista_tel)
lista_tel2={}
print(len(lista_tel2))

dicionario = {"Altura":1.80}
dicionario["Nome"] = "Rafael"
dicionario["Cor"] = "Azul"
# percorre todo o dicionário e imprime cada chave e dado
for x, y in dicionario.items():
    print(f"Chave: {x}, Valor {y}.")


# SETS
# armazena valores únicos (chaves). se mandar adicionar algo repetido, será ignorado

sets = {10, 15, 30, "teste"}    
sets.add(20)

print(sets)



