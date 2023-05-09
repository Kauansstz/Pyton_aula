'''
Introdução as funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor epecífico.
Por padrão, funções Python retornam None (nada)
'''

# def Print(a, b, c):
#     print('Varias1')
#     print('Varias2')
#     print('Varias3')
#     print('Varias4')

# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)

def saudacao(nome = 'anônimo'):
    print(f'Olá, {nome}!')

saudacao('Kauan')
saudacao('Pedro')
saudacao('Maicon')
saudacao()