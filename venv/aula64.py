# dir, hasattr e getattr em python
string = 'kauan'
metodo = 'upper1'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
    
else: 
    print('Não existe upper')