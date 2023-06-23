import importlib
import aula74_m

print(aula74_m.variavel)

for i in range(10):
    importlib.reload(aula74_m)
    print(i)

print('Acabou')