import re

class Endereco:

    def __init__(self,estado,cidade,bairro,cep,rua,numero,complemento):
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
    
    def __str__(self):
        return f"\nEstado: {self.estado}, Cidade: {self.cidade}, Bairro: {self.bairro}, CEP: {self.cep}, Rua: {self.rua}, Número: {self.numero}, Complemento: {self.complemento}"

    @staticmethod
    def cadastrar_Endereco():
        print("Cadastre o endereço:")
        estado = input("Digite o nome do estado: ")
        cidade = input("Digite o nome da cidade: ")
        bairro = input("Digite o nome do bairro: ")
        cep = input("Digite o CEP: (No formato XXXXX-XXX) ")
        rua = input("Digite o nome da rua: ")
        numero = input("Digite o número da casa: ")
        complemento = input("Digite o complemento: ")

        return Endereco(estado,cidade,bairro,cep,rua,numero,complemento)

    @staticmethod
    def validar_cep(cep):
        # Define o padrão para o CEP
        padrao_cep = r'^\d{5}-\d{3}$'
        # Verifica se o CEP corresponde ao padrão
        if re.match(padrao_cep, cep):
            return True
        else:
            return False