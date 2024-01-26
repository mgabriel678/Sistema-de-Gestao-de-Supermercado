from Pessoa import Pessoa

class Cliente(Pessoa):

    def __init__(self, cpf, nome, email, endereco, telefone):
        super().__init__(cpf, nome, email, endereco)
        self.telefone = telefone

    def __str__(self):
        return super().__str__() + f", Telefone: {self.telefone}"
    
    #Cadastro de Clientes
    def cadastrar_cliente(endereco):
        cpf = input("Digite o CPF do cliente: ")
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o email do cliente: ")
        telefone = input("Digite o telefone do cliente: ")


        return Cliente(cpf,nome,email,endereco,telefone)
