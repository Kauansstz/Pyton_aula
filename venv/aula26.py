frase = 'O Python é uma linguagem de programação '\
        'multiparadigma. '\
        'Python foi crriado por Guido van Rossum.'
            
i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    quant_x_letra = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if apareceu_mais_vezes < quant_x_letra:
        apareceu_mais_vezes = quant_x_letra
        letra_apareceu_mais = letra_atual
        
    i += 1
    
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais}" que apareceu '
    f'{apareceu_mais_vezes}x'
)