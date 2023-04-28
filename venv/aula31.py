"""
Listas em Python
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índice e fatiamento 
Métodos úteis
    append, insert, pop, del, clear, extend, +
Create Read update  Delete
Criar, ler, alterar, apagar = Lista[i] (Crud)

"""

lista = [ 10,20,30,40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(50)
ultimo_valor1 = lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor2 = lista.pop()
print(lista, f'Removido: {ultimo_valor1} e {ultimo_valor2}')