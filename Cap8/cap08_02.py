# Em Python, tudo é Objeto!
lst_num = ['Data', 'Science', 'Academy', 'Nota', 10, 10]

print(type(lst_num))
print(lst_num.count(10))

print(type(10))
print(type([]))
print(type(()))
print(type({}))
print(type('a'))

class Carro(object):
    pass

ferrari = Carro()
print(type(ferrari))

class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

Estudante1 = Estudantes('Patrik', 35, 7)
print(Estudante1.nome, Estudante1.idade, Estudante1.nota)