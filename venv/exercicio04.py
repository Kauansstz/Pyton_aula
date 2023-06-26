# Exercicios

# Ordene os produtos por nome decrescente (do maior para o menor)
#Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
#     ]

# novo_produto = [
#     {**produto, 'preco':produto['preco'] + 0.1 }
#     if produto['preco'] > 1  else {**produto}
#     for produto in produtos
#     if produto['preco'] > 1
# ]
# for i in novo_produto:
#     print(i)
'''Feito'''


# Ordene os produtos por preço crescente (do menor para o maior )
# Gere produto_ordenados_por_preco por deep copy (cópia profunda)
# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
#     ]

# def ordem(produtos):
#     for item in produtos:
#         print(item)

# preco = sorted(produtos, key= lambda produtos: produtos['preco'])

# ordem(preco)
'''Feito'''

import copy

from dados import produtos

# Ordene os produtos por preço crescente (do menor para o maior )
# Gere produto_ordenados_por_preco por deep copy (cópia profunda)

produto_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)
print(*produtos, sep='\n')
print()
print(*produto_ordenados_por_preco, sep='\n')
# Ordene os produtos por nome decrescente (do maior para o menor)
#Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome']
)
# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)


novos_produtos =  [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')