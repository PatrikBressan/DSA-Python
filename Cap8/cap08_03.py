# Criando uma classe
class Funcionarios:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def listFunc(self):
        print(f'Funcionário(a) {self.nome} tem salário de R$ {self.salario} e o cargo é {self.cargo}')
    

# Criando um objeto (uma instância da classe) chamado Func1 a partir da classe Funcionarios
Func1 = Funcionarios('Mary', 20000, 'Cientista de Dados')

# Usando o método da classe
Func1.listFunc()

# Usando atributos: hasattr (tem atributo)
print(hasattr(Func1, 'nome'))
print(hasattr(Func1, 'salario'))
setattr(Func1, 'salario', 4500)
print(getattr(Func1, 'salario'))
delattr(Func1, 'salario')
print(hasattr(Func1, 'salario'))


