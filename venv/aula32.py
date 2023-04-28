"""
Listas em Python
Tipo de lista - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índice e fatiamento 
Métodos úteis
    append - Add um item ao final 
    insert - Add um item no índice escolhido
    pop - Remove do final ou do índice escolhido 
    del - Apaga a lista
    extend - Estende a lista
    + - Concatena listas
Create Read update  Delete
Criar, ler, alterar, apagar = Lista[i] (Crud)
"""

lista_a = [ 1, 2, 3]
lista_b = [ 4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)