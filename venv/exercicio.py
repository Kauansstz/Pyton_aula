# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# numero_1 = input('Digite um numero: ')
# opcao = input('Digite 2x, 3x ou 4x que ira magicamente mudar de numero: ')
# try:
#     numero_1_float = float(numero_1)

# except ValueError:
#     print('Numero invalido')

# if opcao == '2x' or opcao == '2':
#     print(f'O numero escolhido foi {numero_1} e duplicou para {numero_1_float * 2}')

# elif opcao == '3x' or opcao == '3':
#     print(f'O numero escolhido foi {numero_1} e triplicou para {numero_1_float * 3}')

# else:
#     print(f'O numero escolhido foi {numero_1} e quadruplicou para {numero_1_float * 4}')
    
def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quadriplicar(numero):
    return numero * 4

numero = input('Digite um numero: ')
numero_float = float(numero)

print(duplicar(numero_float))
print(triplicar(numero_float))
print(quadriplicar(numero_float))