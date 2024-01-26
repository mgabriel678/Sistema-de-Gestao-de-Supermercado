class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto, quantidade):
        if produto in self.produtos:
            self.produtos[produto] += quantidade
        else:
            self.produtos[produto] = quantidade
        print(f"\n{quantidade} unidades do produto '{produto.nome}' adicionadas ao estoque.")

    def remover_produto(self, produto, quantidade):
        if produto in self.produtos:
            if self.produtos[produto] >= quantidade:
                self.produtos[produto] -= quantidade
                print(f"\n{quantidade} unidades do produto '{produto.nome}' removidas do estoque.")
            else:
                print(f"\nQuantidade insuficiente do produto '{produto.nome}' no estoque.")
        else:
            print(f"\nProduto '{produto.nome}' não encontrado no estoque.")

    def listar_produtos(self):
        if self.produtos:
            print("\nProdutos em estoque:")
            for produto, quantidade in self.produtos.items():
                print(f"\n{produto} - Quantidade: {quantidade}")
        else:
            print("\nO estoque está vazio.")

    def alterar_produto(self, produto, novo_preco, novo_departamento):
        if produto in self.produtos:
            produto.preco = novo_preco
            produto.departamento = novo_departamento
            print(f"\nProduto '{produto.nome}' alterado com sucesso.")
        else:
            print(f"\nProduto '{produto.nome}' não encontrado no estoque.")

    def identificar_produto(self, codigo_produto):
        for produto in self.produtos.keys():
            if produto.codigo == codigo_produto:
                return produto
        return None