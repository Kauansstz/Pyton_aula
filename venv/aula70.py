# try, except, else e finally
# a = 18
# b = 0
#c = a / b - error
try:
    a = 18
    b = 0
    print('Aqui vai'[1000])
    c = a / b
    print('Aqui nao')
except ZeroDivisionError:
    print('Dividiu por zero')

except (TypeError, IndexError) as error:
    print('TyperErroor + IndexError')
    print('MSG', error)
    print('Nome: ', error.__class__.__name__)

except NameError:
    print('Nome b não está definido')

except Exception:
    print('Erro desconhecido')

print('DNV')