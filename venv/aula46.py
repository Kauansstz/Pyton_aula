'''
Retorno de valores das funções(return)
'''

def soma(x,y):
    if x < 20:
        return 'parou aqui'
    return 'teste'
    
def multiplica(x,y):
    if x * y >= 30:
        return soma(x,y)
    return 'ops'

print(multiplica(30, 1))
