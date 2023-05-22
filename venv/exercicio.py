# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def dobrar(numero, duplicar):
    total = 1
    multiplico = numero * 2
    for digito in numero, duplicar:
        total *= digito
        return multiplico
    
print(dobrar(2))