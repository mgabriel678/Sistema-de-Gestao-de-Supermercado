from Funcionario import Funcionario
from Cliente import Cliente
from Transportadora import Transportadora
from Endereco import Endereco
from Produto import Produto
from Caixa import Caixa
from Estoque import Estoque



class InterfaceSupermercado:
    def __init__(self):
        pass
        
    def menu_principal(self):
        print("\nBem vindo!")
        print("\nPara começar escolha uma das opções abaixo...\n")
        print("1. Menu de cadastro")
        print("2. Menu do caixa")
        print("3. Menu do estoque")
        print("4. Listas dos cadastros")
        print("5. Encerrar Programa")


    def menu_cadastro(self):
        print("\nOpções de Cadastro: ")
        print("1. Cadastro de Funcionários")
        print("2. Cadastro de Clientes")
        print("3. Cadastro de Transportadoras")
        print("4. Cadastro de Produtos")
        print("5. Voltar")
        print("6. Encerrar Programa")

    def menu_caixa(self):
        print("\nOpções de Caixa: ")
        print("1. Abrir caixa")
        print("2. Fechar caixa")
        print("3. Voltar")
        print("4. Encerrar Programa")
    
    def menu_estoque(self):
        print("\nOpções de estoque: ")
        print("1. Adicionar certa quantidade de um produto ao estoque")
        print("2. Remover certa quantidade de um produto do estoque")
        print("3. Alterar um produto do estoque(Preço e Departamento)")
        print("4. Listar produtos do estoque")
        print("5. Voltar")
        print("6. Encerrar Programa")

    def menu_lista(self):
        print("\nOpções de listas: ")
        print("1. Listas de Funcionários")
        print("2. Listas de Clientes")
        print("3. Listas de Transportadoras")
        print("4. Listas de Produtos")
        print("5. Voltar")
        print("6.Encerrar Programa")


def main():
    endereco1 = Endereco("GO","Goiânia","Setor Oeste","93130-440","Rua Aristides Baronio","S/N","Quadra 2 Lote 5")
    endereco2 = Endereco("RO","Porto Velho","Caladinho","76808-207","Rua Bom Jesus","2","Quadra 5 Lote 10")
    endereco3 = Endereco("SP","Araçatuba","Conjunto Habitacional Nossa Senhora Aparecida","16056-630","Rua Nova Luzitânia","302","Quadra 5 Lote 1 a 6")
    funcionario1 = Funcionario("590.871.900-50", "Marcos","sla@gmail.com",endereco1,"Gerente",'2500.00')
    cliente1 = Cliente("263.497.300-46","João","joão@gmail.com",endereco2,"(96) 3372-5427")
    produto1 = Produto("Papel Higienico",'15.00',"Higiene e Limpeza")
    produto2 = Produto("Sabão em pó",'30.00',"Higiene e Limpeza")
    transportadora1 = Transportadora("19.652.354/0001-49","Lorenzo e Emanuelly Filmagens Ltda",endereco3,"(18) 3888-3854")
    estoque = Estoque()
    Estoque.adicionar_produto(estoque,produto1,100)
    Estoque.adicionar_produto(estoque,produto2,200)
    lista_funcionarios = []
    lista_clientes = []
    lista_produtos = []
    lista_transportadoras = []

    lista_funcionarios.append(funcionario1)
    lista_clientes.append(cliente1)
    lista_transportadoras.append(transportadora1)
    lista_produtos.append(produto1)
    lista_produtos.append(produto2)
    lista_compras = []


    caixa = Caixa()
    interface = InterfaceSupermercado()

    while True:

        interface.menu_principal()

        escolha_principal = input("Opção: ")

        if escolha_principal == '1':

            opcao_cadastro = '0'

            while opcao_cadastro != '5': 
                
                interface.menu_cadastro()
                opcao_cadastro = input("Escolha a opção de cadastro: ")

                if opcao_cadastro == '1':

                    endereço_cadastro= Endereco.cadastrar_Endereco()
                    funcionario_cadastro = Funcionario.cadastrar_funcionario(endereço_cadastro)
                    Funcionario(funcionario_cadastro.cpf,funcionario_cadastro.nome,funcionario_cadastro.email,funcionario_cadastro.endereco,funcionario_cadastro.cargo,funcionario_cadastro.salario)
                    lista_funcionarios.append(funcionario_cadastro)

                    print(f"\nFuncionário: {funcionario_cadastro} foi cadastrado com sucesso.")
                    
                elif opcao_cadastro == '2':
                    
                    endereço_cadastro = Endereco.cadastrar_Endereco()
                    cliente_cadastro = Cliente.cadastrar_cliente(endereço_cadastro)
                    Cliente(cliente_cadastro,cliente_cadastro.nome,cliente_cadastro.email,cliente_cadastro.endereco,cliente_cadastro.telefone)
                    lista_clientes.append(cliente_cadastro)
                    print(f"\nCliente: {cliente_cadastro} foi cadastrado com sucesso.")

                elif opcao_cadastro == '3':
                    
                    endereço_cadastro= Endereco.cadastrar_Endereco()
                    transportadora_cadastro = Transportadora.cadastrar_transportadora(endereço_cadastro)
                    Transportadora(transportadora_cadastro,transportadora_cadastro.nome,transportadora_cadastro.endereco,transportadora_cadastro.telefone)
                    lista_transportadoras.append(transportadora_cadastro)

                    print(f"\nTransportadora: {transportadora_cadastro} foi cadastrado com sucesso.")

                elif opcao_cadastro == '4':

                    produto_cadastro = Produto.cadastrar_produto()
                    Produto(produto_cadastro,produto_cadastro.preco,produto_cadastro.departamento)
                    lista_produtos.append(produto_cadastro)

                    print(f"\nProduto: {produto_cadastro} foi cadastrado com sucesso.")

                elif opcao_cadastro == '5':

                    print("\nVoltando...")

                elif opcao_cadastro == '6':

                    print("\nEncerrando Programa...")
                    break

                else:

                    print("\nOpção inválida.")


        elif escolha_principal == '2':

            opcao_caixa = '0'

            while opcao_caixa != '3':

                interface.menu_caixa()
                opcao_caixa = input("Escolha a opção de caixa: ")
            
                if opcao_caixa == '1':

                    Caixa.abrir_caixa(caixa)

                    print("Iniciando compras...")

                    opcao_compra = '0'
                    total = 0

                    while opcao_compra == '0':
                        

                        codigo_compra = int(input("Adicione o codigo do produto: "))
                        produto_compra = Estoque.identificar_produto(estoque,codigo_compra)

                        total = produto_compra.preco + total
                        
                        print(f"Valor total: {total}")

                        Caixa.adicionar_compra(caixa,produto_compra)
                        
                        escolha_caixa = input("Deseja adicionar outro produto? s/n")

                        if escolha_caixa == 'n':
                            opcao_compra = '1'
                

                    lista_produtos = Caixa.finalizar_compra
                    Caixa.gerar_recibo(caixa)
                    print("\nObrigado pela compra!")
                    

                elif opcao_caixa == '2':

                    Caixa.fechar_caixa(caixa)

                elif opcao_caixa == '3':

                    print("\nVoltando...")

                elif opcao_caixa == '4':
                    
                    print("\nEncerrando Programa...")
                    break

                else:

                    print("\nOpção inválida.")
        
        elif escolha_principal == '3':

            opcao_estoque = '0'

            while opcao_estoque != '5':

                interface.menu_estoque()
                opcao_estoque = input("Escolha a opção de estoque: ")


                if opcao_estoque == '1' :

                    codigo_produto = int(input("Digite o código do produto:"))
                    produto3 = Estoque.identificar_produto(estoque,codigo_produto)

                    if produto3 == None:
                        print("\nProduto não encontrado")
                    else:
                        quantidade_produto = int(input("Digite a quantidade que deseja adicionar: "))
                        Estoque.adicionar_produto(estoque,produto3,quantidade_produto)

                elif opcao_estoque == '2' :

                    codigo_produto = int(input("Digite o código do produto:"))
                    produto3 = Estoque.identificar_produto(estoque,codigo_produto)

                    if produto3 == None:
                        print("\nProduto não encontrado")
                    else:
                        quantidade_produto = int(input("Digite a quantidade que deseja remover: "))
                        Estoque.remover_produto(estoque,produto3,quantidade_produto)

                elif opcao_estoque == '3' :

                    codigo_produto = int(input("Digite o código do produto: "))
                    produto3 = Estoque.identificar_produto(estoque,codigo_produto)

                    if produto3 == None:
                        print("\nProduto não encontrado")
                    else:
                        novo_preco_produto = float(input("Digite o novo preço do produto: "))
                        novo_departamento_produto = input("Digite o novo departamento do produto: ")
                        Estoque.alterar_produto(estoque,novo_preco_produto,novo_departamento_produto)

                elif opcao_estoque == '4' :

                    Estoque.listar_produtos(estoque)

                elif opcao_estoque == '5' :
                    
                    print("\nVoltando...")

                elif opcao_estoque == '6' :

                    print("\nEncerrando Programa...")
                    break

                else:

                    print("\nOpção inválida.")

        elif escolha_principal == '4':

            opcao_lista = '0'

            while opcao_lista != '5':
            
                interface.menu_lista()
                opcao_lista = input("Escolha a opção de listas: ")

                if opcao_lista == '1':

                    for funcionario in lista_funcionarios:
                        print(f"\nCPF: {funcionario.cpf}, Nome: {funcionario.nome}, E-mail: {funcionario.email}, Endereço: {funcionario.endereco}, Cargo: {funcionario.cargo}, Salário: {funcionario.salario}")
                
                elif opcao_lista == '2':

                    for cliente in lista_clientes:
                        print(f"\nCPF: {cliente.cpf}, Nome: {cliente.nome}, E-mail: {cliente.email}, Endereço: {cliente.endereco}, Telefone: {cliente.telefone}")

                elif opcao_lista == '3':

                    for transportadora in lista_transportadoras:
                        print(f"CNPJ: {transportadora.cnpj}, Nome: {transportadora.nome}, Endereço: {transportadora.endereco}, Telefone: {transportadora.telefone}")

                elif opcao_lista == '4':

                    for produto in lista_produtos:
                        print(f"Código: {produto.codigo}, Nome: {produto.nome}, Preço: {produto.preco}, Departamento: {produto.departamento}")

                elif opcao_lista == '5':

                    print("\nVoltando...")

                elif opcao_lista == '6':

                    print("\nEncerrando Programa...")
                    break

                else:

                    print("\nOpção inválida.")



        elif escolha_principal == '5':

            print("\nEncerrando Programa...")
            break

        else:

            print("\nOpção inválida.")


if __name__ == "__main__":
    main()
