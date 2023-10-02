# Criando uma classe chamada livro
class Livro():

    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__ "Método Construtor"
    # self é uma referência a cada atributo da própria classe (e não de uma classe mãe, por exemplo)
    def __init__(self):
        # Atributos são propriedades
        self.titulo = 'Sapiens - Uma Breve História da Humanidade'
        self.isbn = 9988888
        print('Construtor chamado para criar um objeto desta classe.')
    
    # Métodos são funções que executam ações nos objetos da classe
    def imprime(self):
        print('Foi criado o livro %s com ISBN %d' %(self.titulo, self.isbn))
        print(f'Foi criado o livro {self.titulo} com ISBN {self.isbn}')

# Criando uma instância da classe Livro
Livro1 = Livro()

# O objeto Livro1 é do tipo Livro
print(type(Livro1))

print(Livro1.titulo)
print(Livro1.isbn)
Livro1.imprime()

# Criando uma classe Livro com parâmetros no método construtor
class LivroMelhorado():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print('\nConstrutor chamado para criar um objeto desta classe.')

    def imprime(self, titulo, isbn):
        print(f'Este é o livro: {self.titulo}, com ISBN {self.isbn}')

Livro2 = LivroMelhorado('O Poder do Hábito', 77886611)
print(Livro2.titulo)
Livro2.imprime('O Poder do Hábito', 77886611)

# Criando uma classe Algoritmo
# Em Python, recomenda-se escrever a primeira letra de cada palavra da classe com letra maiúscula
class Algoritmo():
    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print('Construtor chamado para criar um objeto desta classe.')

algo1 = Algoritmo(tipo_algo = 'Random Forest')
algo2 = Algoritmo(tipo_algo = 'Deep Learning')

print(algo1.tipo)
print(algo2.tipo)