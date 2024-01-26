

class Pessoa:

    def __init__(self, cpf, nome, email, endereco):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.endereco = endereco

    def __str__(self):
        return f"\nCPF: {self.cpf}, Nome: {self.nome}, Email: {self.email}, Endereço: {self.endereco}"
    
    def validar_cpf(cpf):
        # Remover caracteres não numéricos do CPF
        cpf = ''.join(filter(str.isdigit, cpf))

        # Verificar se o CPF tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Calcular o primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = 11 - (soma % 11)
        if resto == 10 or resto == 11:
            resto = 0
        if resto != int(cpf[9]):
            return False

        # Calcular o segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = 11 - (soma % 11)
        if resto == 10 or resto == 11:
            resto = 0
        if resto != int(cpf[10]):
            return False

        return True