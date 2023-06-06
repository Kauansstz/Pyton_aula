# Yield from
def gn1():
    print('Começou gn1')
    yield 1
    yield 2
    yield 3
    print('Acabou o gn1')

def gn3():
    print('Começou gn3')
    yield 10
    yield 20
    yield 30
    print('Acabou o gn3')

def gen2(gen=None):
    print('Começou gn2')
    if gen is not None:
        yield from gen()
    yield 4
    yield 5
    yield 6
    print('Acabou o gn2')
    
g1 = gen2(gn1)
g2 = gen2(gn3)
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()
