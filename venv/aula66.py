import sys

# Generator expression, iterables e iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

generator = (n for n in range(10))
lista = [n for n in range(10)]

print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))