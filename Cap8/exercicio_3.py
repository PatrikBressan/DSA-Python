# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface
        print('Objeto do tipo Smartphone criado com sucesso!')


class MP3Player(Smartphone):
    def __init__(self, capacidade, tamanho, interface):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)

    def printer(self):
        print(f'A interface do objeto do tipo Smartphone é {self.interface}, o seu tamanho é {self.tamanho}, e a sua capacidade é {self.capacidade}.')

def main():
    device1 = MP3Player(capacidade='128 GB', tamanho='Grande', interface='LED')
    device1.printer()
    device2 = MP3Player(capacidade='64 GB', tamanho='Pequeno', interface='Touch')
    device2.printer()


if __name__ == '__main__':
    main()
