produto= [
    'queijo', 'presunto' , 'Mouse'
]

produto.sort()
# print(produto)

saida = ''
cont = 1

for i in produto:
    saida+=i
    if cont < len(produto):
        saida+=', '
    cont+=1

print(saida)

# print(produto[0]+', '+produto[1]+', '+produto[2])

# saida = ''

# for i, v in enumerate(produto):
#     saida+=v

# print(saida)
