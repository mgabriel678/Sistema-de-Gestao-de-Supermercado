from Pessoa import Pessoa

class Funcionario(Pessoa):

    def __init__(self, cpf, nome, email, endereco, cargo, salario):
        super().__init__(cpf, nome, email, endereco)
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return super().__str__() + f", Cargo: {self.cargo}, Salário: {self.salario}"
    
    #Cadastro de Funcionários
    def cadastrar_funcionario(endereco):
        cpf = input("Digite o cpf do funcionário: ")
        nome = input("Digite o nome do funcionário: ")
        email = input("Digite o e-mail do funcionário: ")
        cpf = input("Digite o CPF do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))


        return Funcionario(cpf, nome, email,endereco, cargo, salario)