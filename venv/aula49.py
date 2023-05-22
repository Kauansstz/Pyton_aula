"""
Closure e funções que retornam
"""

def criar(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}! '
    return saudar

falar_bom_dia = criar('Bom dia')
falar_boa_noite = criar('Boa noite')

for nome in ['Maria', 'Pedro', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))    