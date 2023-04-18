entrada = input('Digite a hora número inteiros: ')

try:
    hora = entrada = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom Dia')

    elif hora >= 12 and hora <= 17:
        print('Boa Tarde')

    elif hora >= 18 and hora <= 23:
        print('Boa Noite')

    else:
        print('Não conheco essa hora')
        
except:
    print('Por favor, digite apenas numeros inteiros')