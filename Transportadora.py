class Transportadora:
    def __init__(self, cnpj, nome, endereco, telefone):
        self.cnpj = cnpj
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f"\nCNPJ: {self.cnpj}\nTransportadora: {self.nome}\nEndereço: {self.endereco}\nTelefone: {self.telefone}\n"

    def cadastrar_transportadora():
        nome = input("Digite o nome da transportadora: ")
        cnpj = input("Digite o CNPJ da transportadora: ")
        endereco = input("Digite o endereço da transportadora: ")
        telefone = input("Digite o telefone da transportadora: ")


        return Transportadora(cnpj, nome, endereco, telefone)