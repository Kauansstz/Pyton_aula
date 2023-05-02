"""
enumerate - enumera iteráveis(índices)
"""

lista = [ 'Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista))


for indice, nome in lista_enumerada: 
     print(indice,  '-' , nome)

# print(next(lista_enumerada))

# for item in lista_enumerada: 
#     print(item)


# for tupla in lista_enumerada: 
#      print('For da tupla: ')
#      for valor in tupla:
#           print(f'\t{valor}')