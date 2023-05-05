'''
split e join com list e str
split - divide uma string
join - une uma string
'''

frase = 'olha só que, coisa interessante'
lista_frases = frase.split(',')


for i, frase in enumerate(lista_frases):
    print(lista_frases[i])
    