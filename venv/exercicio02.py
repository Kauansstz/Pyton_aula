# Exercicio - sistema de perguntas e respostas 

perguntas = [
    {
        'Perguntas':'Quantos que é 2+2?',
        'opções': ['1', '2', '3', '4', '5'],
        'Respostas': '4',
    },

    {
        'Perguntas':'Quantos que é 10/2?',
        'opções': ['6', '4', '5', '1', '2'],
        'Respostas': '5',
    },


    {
        'Perguntas':'Quantos que é 5*5?',
        'opções': ['25', '10', '55', '51', '05'],
        'Respostas': '25',
    },
]

qtd_acertou = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Perguntas'])
    print()
    
    opcoes = pergunta['opções']
    for  i, opcao in enumerate(opcoes):
        print(i, opcao, sep=') ')
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
        
        if escolha_int is not None:
            if escolha_int >= 0 and escolha_int < qtd_opcoes:
                if opcoes[escolha_int] == pergunta['Respostas']:
                    acertou = True

    print()    
    if acertou:
        qtd_acertou += 1
        print('acertou 👍')

    else:
        print('Errou ❌')

    print()
    

print('Você acertou', qtd_acertou)
print('de', len(pergunta), 'perguntas.')
