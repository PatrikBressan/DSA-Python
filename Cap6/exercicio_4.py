# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo.
# Aplique as duas funções aos elementos da lista abaixo.
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

#Solution
square = lambda x: x**2
cube = lambda x: x**3

funcs = [square,cube]

for i in lista:
    result = map(lambda x: x(i), funcs)
    print(list(result))


#Others solutions
add = lambda x: x+1
sub = lambda x: x-1

funcs2 = [add,sub]

for i in lista:
    resultado = map(lambda x: x(i), funcs2)
    print(list(resultado))