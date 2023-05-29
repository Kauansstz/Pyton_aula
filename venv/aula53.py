# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados em matemática 
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno

# Criando um set 
# set(iterável) ou {1, 2, 3}
s1 = set() # vazio
s1 = {'Pedro'} # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - eles não tem índexes;
# - ele não garantem orfem;
# - eles são iteráveis (for, in, not in)

# l1= [1, 2, 3, 3, 3,3 , 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

# Métodos úteis:
# add, update, clear, discard
s1= set()
s1.add('Luiz')
s1.add(1)
s1.update(('Ola mundo', 1,2,3,4,5))
s1.discard('Ola mundo')
# print(s1)

# Operadores úteis:
# união | uniao (union) | un
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda 
# diferença simétrica ^ - Itens não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)