'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''

#Lembre-te de desempacotamento
# x, y, *resto= 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

# def soma(*args):
#     total = 0
#     for numero in args:
#         print('Total: ', total, '+', numero)
#         total = total + numero
#         print('Total =', total)
#     print('Último resultado foi: ', total )
# soma(1, 2, 3, 4, 5, 6)

# def soma(*args):
#     total = 0
#     for numero in args:
#         total += numero
#         return total

# soma_1 = soma(1, 2, 3)
# print(soma_1)
# soma_2 = soma(4, 5 ,6)
# print(soma_2)

def soma(*args):
    x = args[0]
    y = args[1]
    z = args[2]
    return x+y+z

print(soma(1,2,3))
print(soma(2,3,8))