# texto = iter('Kauan') #___iter___()
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())


#for letra in texto:
texto = 'Kauan' # iterável
iteratador = iter(texto) # iterador

while True:
    try:
        letra = next(iteratador)
        print(letra)

    except StopIteration:
        break