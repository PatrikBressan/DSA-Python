# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, 
# passando 2 parâmetros e depois faça uma chamada aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print('\nObjeto do tipo Rocket criado com sucesso!')
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
        
def main():
    roc1 = Rocket(7,23)
    roc1.x
    roc1.y

    roc1.print_rocket()
    roc1.move_rocket()
    roc1.print_rocket()

# Executa o programa
if __name__ == "__main__":
    main()