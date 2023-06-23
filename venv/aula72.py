# Módulos padrão do Python(import, from, as e *)
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# partes - from nome_modulo import object1, object2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, plataforma

# plataforma = 'TU'
# print(plataforma)

# alias 1 - import nome_modulo as apelido
# import sys as s
# sys = 'bla'
# print(s.plataforma)
# print(sys)

# alias 2 - from nome_modulo import objeto as apelido
# from sys import platform as pf, exit as ex
# print(pf)

# Vantagens: Você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padroa da linguagem

# Má pratica - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

from sys import *

print(platform)
exit()