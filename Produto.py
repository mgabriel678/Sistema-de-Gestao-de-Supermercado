class Produto:
    ultimo_codigo = 0

    def __init__(self, nome, preco, departamento):
        Produto.ultimo_codigo += 1
        self.codigo = Produto.ultimo_codigo
        self.nome = nome
        self.preco = float(preco)
        self.departamento = departamento

    def __str__(self):
        return f"\nCódigo: {self.codigo}, Produto: {self.nome}, Preço: R${self.preco:.2f}, Departamento: {self.departamento}"

    @staticmethod
    def cadastrar_produto():
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        departamento = input("Digite o departamento do produto: ")

        return Produto(nome, preco, departamento)
    