# Operadores in e not int
# Strings sao iteraveis 
# 0 1 2 3 4 5
# O t á v i o
# -6-5-4-3-2-1
#nome = 'Otávio'
#print(nome[2])
#print(nome[-1])
#print(10 * '-' )
#print('vio' not in nome)
#print('zero' not innome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que você deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esá em {nome}')

else:
    print(f'{encontrar} não está em {nome}')