from Produto import Produto 

class Caixa:
    def __init__(self):
        self.produtos_comprados = []
        self.aberto = False

    def abrir_caixa(self):
        if not self.aberto:
            self.aberto = True
            print("Caixa aberto.")
        else:
            print("O caixa já está aberto.")

    def fechar_caixa(self):
        if self.aberto:
            self.aberto = False
            print("Caixa fechado.")
            self.produtos_comprados = []  
        else:
            print("O caixa já está fechado.")

    def adicionar_compra(self, produtos):
        self.produtos_comprados.append(produtos)

        print("Compra adicionada com sucesso.")


    def finalizar_compra(self):
        print("Finalizando compra...")
        print("Métodos de pagamento disponíveis:")
        print("1. Dinheiro")
        print("2. Cartão de crédito")
        print("3. Cartão de débito")
        
        metodo_pagamento = input("Escolha o método de pagamento: ")
        if metodo_pagamento == "1":
            print("Pagamento em dinheiro selecionado.")
        elif metodo_pagamento == "2":
            print("Pagamento com cartão de crédito selecionado.")
        elif metodo_pagamento == "3":
            print("Pagamento com cartão de débito selecionado.")
        else:
            print("Método de pagamento inválido.")

        return Caixa.produtos_comprados 

    def gerar_recibo(self):
        print("RECIBO DE COMPRA")
        for i, compra in enumerate(self.produtos_comprados, 1):
            print(f"Compra {i}: {compra}")