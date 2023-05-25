# Métidis úteis dos dicionarios em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# cpý - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionario com outro
import copy

d1= {
    'c1':1,
    'c2':2,
    'li': [0, 1, 2]
}

d2=copy.deepcopy(d1)#Deepcopy - cópia profunda

d2['c1']= 1000
d2['li'][1]= 1000
print(d1)
print(d2)