nome = input('Digite o seu nome completo: ')
idade = input('Digite a sua Idade: ')


if nome and idade:
    print(f"Seu nome é {nome}"),
    print(f"Seu nome invertido é {nome [::-1]}")
    print(f"Sua Idade é {idade}"),
    print(f'Seu nome tem {len(nome)} de letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
    if ' ' in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome nao possui espaço')

else:
    print("Desculpe, você não digitou nada")