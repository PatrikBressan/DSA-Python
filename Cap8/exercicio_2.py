# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():
    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def printer(self):
        print(f'\nNome: {self.nome}, Cidade: {self.cidade}, Telefone: {self.telefone}, E-mail: {self.email}.')

    def countWords(self):
        contador = len(self.nome)
        print(f'\nA quantidade de letras no nome é {contador}.')

def main():
    humano = Pessoa('Patrik', 'Jardim', 67992510154, 'patrik.bressan@ifms.edu.br')
    humano.printer()
    humano.countWords()

if __name__ == '__main__':
    main()

