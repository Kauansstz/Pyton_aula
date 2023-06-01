# Empacotamento e desempacotamento de dicionário
a, b = 1, 2
a, b = b, a
# print(a, b)

# a, b = pessoa.values()
# print('1', a, b)
# (a1, a2), (b1, b2) = pessoa.items()
# print('2',a1, a2)
# print('2', b1, b2)

# for chave, valor in pessoa.items():
#     print('3',chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade':16,
    'altura':1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

def  mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(nome= 'Joana', qlq=123)
mostro_argumentos_nomeados(**pessoa_completa)