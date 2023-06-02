# Mapeamento de dados em list comprehension
produtos = [
    {'Nome':'p1', 'preco': 20, },
    {'Nome': 'p2', 'preco': 10, },
    {'Nome': 'p3', 'preco': 30, },
]

novo_produto = [
    {**produto, 'preco':produto['preco']* 1.05 }
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novo_produto, sep='\n') 