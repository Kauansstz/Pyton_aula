entrada = input('Digite um numero: ')

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'
    print(f'o número {entrada_int} é {par_impar_texto}')

except:
    print('Voce não digitou um numero inteiro')