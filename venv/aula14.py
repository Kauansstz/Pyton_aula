while True:
    entrada = input('Você quer "Entrar" ou "Sair"? [E] para entrar e [S] para sair: ' )
    senha_digitada = input('Senha: ')
    senha_permitida = 123456
    senha_digitada = int(senha_digitada)

 
    if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: 
        print('Você entrou no sistema')
        print('Bem - Vindo!"')
        break

    elif entrada == 'S':
        print('Você saiu do sistema') 
        break

    else:
        print('Você não digitou nem entrar e nem sair')