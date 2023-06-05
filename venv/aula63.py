# Valores Truthy e Falsy, tipos Mutáveis e Imutáveis
#  Mutáveis [] {} set ()
# Imutáveis () "" 0 0.0 None False rande(0,10)
lista = []
dicionarios = {}
conjuntos = set()
tupla = ()
string = ''
inteito = 0 
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'Teste', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionarios=}', falsy(dicionarios))
print(f'{conjuntos=}', falsy(conjuntos))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteito=}', falsy(inteito))
print(f'{flutuante=}', falsy(flutuante))
print(f'{falso=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))
