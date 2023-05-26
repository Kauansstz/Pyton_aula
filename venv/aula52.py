# Métidis úteis dos dicionarios em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave nã
# cpý - retorna uma cópia rasa (shallow cop
# get - obtém uma chave
# pop - Apaga um item com a chave especific
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionario com outro
p1 = {
    'nome': 'Kauan',
    'Sobrenome':'Paluo',
}

print(p1['nome'])
print(p1.get('nome', 'não existe'))
# 
# nome= p1.pop('nome')
# print(nome)
# print(p1)

# nome= p1.popitem()
# print(nome)
# print(p1)

# p1.update({
#     'nome': 'noo',
#     'idade': 90,
# })
p1.update(nome = 'teste', idade = 30)
print(p1)