contador = 'Cada 100 números, será pulado'
cont = contador.split(', ')
cont_2 = []

for i, contador in enumerate(range(1, 201)):
    print(i, end='  ')
    cont_2.append(contador[i].strip())

    

        

    frase = 'olha só que, coisa interessante'
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

frase = ', '.join(lista_frases)
print(frase)

