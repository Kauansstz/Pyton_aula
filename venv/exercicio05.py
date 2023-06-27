# Exercicio - Adiando execução de funções 

def soma (x,y):
    return x + y

def multiplica (x,y):
    return x * y

def executa (funcao,x):
    def interna(y):#close, ira adiar a execução do def acima
        return funcao(x,y)
    return interna

soma_com_cinco = executa(soma,5)
multiplica_por_dez = executa(multiplica,10)
print(soma_com_cinco(10))

