letras = set()
while True:
    letra = input('Digite: ')
    letras.update(letra.lower())

    if 'l' in letras:
        quant= (len(letras))
        print(f'Parabens você acertou!\nVocê teve {quant} tentativas')
        break

    print(letras)