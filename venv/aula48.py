#Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor
# da variavel.
# Crie uma função fala se um número é par ou impar.
# Retorne se o número é par ou impar.

# numero_1 = input("Digite um numero: ")
# numero_2 = input("Digite um numero: ")


# numero_1_float = 0
# numero_2_float = 0
# numeros_validos = None
# try:
#     numero_1_float = float(numero_1)
#     numero_2_float = float(numero_2)
#     numeros_validos = True
#     resultado =  numero_1_float * numero_2_float
# except ValueError:
#     numeros_validos = None
    
# multi = resultado % 2

# if multi == 0:
#     print(f'Seu resultado foi {resultado} e é número par.')

# else:
#     print(f'Seu resultado foi {resultado} e é número impar')
# código acima foi feito por mim

# código abaixo é do instrutor.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multi = multiplicar(1, 2, 3, 4, 5)
print(multi)

def par_impar(numero):
    multiplo = numero % 2 == 0

    if multiplo:
        return f'{numero} é par'
    return f'{numero} é ímpar'
    
print(par_impar(2))
print(par_impar(3))
print(par_impar(4))
print(par_impar(6))