# Mapeamento de dados em list comprehension
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)
produtos = [
    {'Nome':'p1', 'preco': 20, },
    {'Nome': 'p2', 'preco': 10, },
    {'Nome': 'p3', 'preco': 30, },
]

novo_produto = [
    {**produto, 'preco':produto['preco']* 1.05 }
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

p(novo_produto)
# print(*novo_produto, sep='\n') 
# p(novo_produto)

# lista = [n for n in range(10) if n < 5]
# print(lista)