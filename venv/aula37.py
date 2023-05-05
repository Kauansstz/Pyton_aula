'''
split e join com list e str
split - divide uma string
join - une uma string
'''

frase = 'olha só que, coisa interessante'
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

frase = ', '.join(lista_frases)
print(frase)


