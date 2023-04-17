"""
Introdução  ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str= input('Vou dobra o npumero que vc digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 3}')

except:
    print('Isso não é um número')