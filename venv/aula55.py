# Função lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única 
# expressão.
# lista = [ 
#       {'nome': 'Luiz', 'sobrenome': 'miranda'}
#       {'nome': 'Maria', 'sobrenome': 'Oliveira'}
#       {'nome': 'Daniel', 'sobrenome': 'Silva'}
#       {'nome': 'Eduardo', 'sobrenome': 'Moreira'}
#       {'nome': 'Aline', 'sobrenome': 'Souza'}
# ]
# lista = [4, 55, 7, 0, 8, 3, 10, 61, 152, 13]
# lista.sort(reverse=True)
# sorted(lista)
# print(lista)

lista = [ 
      {'nome': 'Luiz', 'sobrenome': 'Miranda'},
      {'nome': 'Maria', 'sobrenome': 'Oliveira'},
      {'nome': 'Daniel', 'sobrenome': 'Silva'},
      {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
      {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

s1 = sorted(lista, key=lambda item: item['nome'])
s2 = sorted(lista, key=lambda item: item['sobrenome'])


exibir(s1)
exibir(s2)
exibir(s2)
