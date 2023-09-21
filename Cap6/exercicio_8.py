# Exercício 8 - Considere os dois dicionários abaixo.
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

#Solution
def trocar(d1,d2):
    dictTemp = {}

    for d1key, d2val in zip(d1,d2.values()):
        dictTemp[d1key] = d2val
    
    return dictTemp

dict3 = trocar(dict1,dict2)
print(dict3)