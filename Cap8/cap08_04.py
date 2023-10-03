'''
Uma função dentro de uma classe é chamado de "Método"

Em Python, os métodos de classes são funções definidas dentro de uma classe. Os métodos de classes
são usados para implementar o comportamento dos objetos que pertencem a essa classe.

O método init é um método especial que é chamado quando um objeto é criado a partir da classe.
Esse método é usado para inicializar os atributos do objeto. Outros métodos podem ser definidos
para executar tarefas específicas em um objeto, como calcular valores, realizar operações de 
entrada e saída, ou alterar o estado do objeto.
'''

# Criando uma classe chamada Circulo
class Circulo():
    # o valor de pi é constante
    pi = 3.14

    # Quando um objeto desta classe for criado, este método será executado e o valor default do raio será 5
    def __init__(self, raio = 5):
        self.raio = raio

    # Esse método calcula a área.
    def area(self):
        return(self.raio * self.raio) * Circulo.pi
    
    # Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio
    
    # Método para obter o raio do círculo
    def getRaio(self):
        return self.raio

# Criando um objeto circ, uma instância da classe Circulo()    
circ = Circulo()

# Executando um método da classe Circulo
print(circ.getRaio())

# Criando outro objeto chamado circ1. Uma instância da classe Circulo()
# Agora sobrescrevendo o valor do atributo
circ1 = Circulo(7)

# Executando um método da classe Circulo
print(circ1.getRaio())

# Imprimindo o raio
print(f'O raio de circ é: {circ.getRaio()}')
print(f'O raio de circ1 é: {circ1.getRaio()}')

# Imprimindo a área
print(f'Área de circ é: {circ.area()}')
print(f'Área de circ1 é: {circ1.area()}')

# Gerando um novo valor para o raio do círculo
circ.setRaio(3)
print(f'Novo raio de circ é: {circ.getRaio()}')