'''
Herança:
- Classe original: classe mãe ou superclasse
- Nova classe: classe filha ou subclasse
'''

# Criando a classe Animal - Superclasse
class Animal:
    def __init__(self):
        print('Animal Criado.')
    
    def imprimir(self):
        print("Este é um animal.")
    
    def comer(self):
        print("Hora de comer.")
    
    def emitir_som(self):
        pass

# Criando a classe Cachorro - Sublasse
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado.")
    
    def emitir_som(self):
        print("Au au!")

# Criando a classe Cachorro - Sublasse
class Gato(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato Criado.")
    
    def emitir_som(self):
        print("Miau!")

# Criando um objeto (Instanciando a classe)
rex = Cachorro()
rex.emitir_som()
rex.imprimir()
rex.comer()

# Criando um objeto (Instanciando a classe)
zeze = Gato()
zeze.emitir_som()
zeze.imprimir()
zeze.comer()

