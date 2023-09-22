# Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#Solution
def index(lista):
    elements = []
    number = len(lista)
    for i in range(6, number):
        elements.append(lista[i])
    return(elements)

result = index(lista)
print(result)

#Other solution
for indice, valor in enumerate(lista):
    if indice <= 5:
        continue
    else:
        print(valor)