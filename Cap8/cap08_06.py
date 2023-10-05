'''
Polimorfismo:
- se refere à habilidade de um objeto responder de diferentes formas a uma mesma mensagem.
- Isso é possível porque as subclasses podem implementar métodos com o mesmo nome que os métodos
da superclasse, mas com comportamentos diferentes.
'''

# Superclasse
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def acelerar(self):
        pass

    def frear(self):
        pass

# Subclasse
class Carro(Veiculo):
    def acelerar(self):
        print("O carro está acelerando.")
    
    def frear(self):
        print("O carro está freando.")

# Subclasse
class Moto(Veiculo):
    def acelerar(self):
        print("A moto está acelerando.")
    
    def frear(self):
        print("A moto está freando.")

# Subclasse
class Aviao(Veiculo):
    def acelerar(self):
        print("O avião está acelerando.")

    def frear(self):
        print("O avisão está freando.")
    
    def decolar(self):
        print("O avião está decolando.")

# Cria os objetos
lista_veiculos = [Carro("Porche", "911 Turbo"), Moto("Honda", "CB 1000R Black Edition"), Aviao("Boeing", "757")]

#Loop
for item in lista_veiculos:
    # O método acelerar tem comportamento diferente dependendo do tipo de objeto
    item.acelerar()

    # O método frear tem comportamento diferente dependendo do tipo de objeto
    item.frear()

    # Executamos o método decolar somente se o objeto for instância da classe Aviao
    if isinstance(item, Aviao):
        item.decolar()
    
    print('---')