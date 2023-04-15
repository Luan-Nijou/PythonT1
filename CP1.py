# RM98920 / Luan Nijou
print("BEM VINDO A VINHARIA ")
nome = input("Coloque seu nome completo:")
Idade = int(input("Coloque sua idade:"))
EndereçoDoCliente = input("Coloque seu endereço:")
EndereçoDaEntrega = input("Coloque o endereço da entrega:")
cep = int(input("Coloque o número do seu CEP:"))
MeioDeCompra = input("Qual o meio de compra(Exemplos: Cartão de crédito): ")
CatalogoVinho = ("Vinhos a venda ---> (1)Vinho_A->R$50 / (2)Vinho_B->R$100 / (3)Vinho_C->R$150 / (4)Vinho_D->R$200 / (5)Vinho_E->R$250")


QtdViA = 0
ValorViA = 0
QtdViB = 0
ValorViB = 0
QtdViC = 0
ValorViC = 0
QtdViD = 0
ValorViD = 0
QtdViE = 0
ValorViE = 0
ValorTotalCompra = 0
Frete = 10

if Idade<18:  
    print("Pessoas menores de idade não podem comprar")
    
elif Idade>=18:
    print(CatalogoVinho)
    print("Escolha a quantidade de cada vinho que irá comprar, valores acima de 200 reais recebem frete grátis(frete = 10 reais)")
    QtdViA = int(input("Qtd VinhoA:"))
    QtdViB = int(input("Qtd VinhoB:"))
    QtdViC = int(input("Qtd VinhoC:"))
    QtdViD = int(input("Qtd VinhoD:"))
    QtdViE = int(input("Qtd VinhoE:"))
    ValorViA = 50 * QtdViA
    ValorViB = 100 * QtdViB
    ValorViC = 150 * QtdViC
    ValorViD = 200 * QtdViD
    ValorViE = 250 * QtdViE
    ValorTotalCompra = ValorViA + ValorViB + ValorViC + ValorViD + ValorViE

    if ValorTotalCompra<100:
        print("Valor mínimo da compra total é de R$100")
    elif ValorTotalCompra<=199:
        print("Compra com frete")
    else:
        print("Compra com frete grátis")
    print("Unidades compradas --> VinhoA-> %d unidades   VinhoB-> %d unidades / VinhoC-> %d unidades / VinhoD-> %d unidades / VinhoE-> %d unidades" %(QtdViA,QtdViB,QtdViC,QtdViD,QtdViE))
    print("Valor total da compra: %1.2f" %ValorTotalCompra)
    print("Será entregue em: %s" %EndereçoDaEntrega)
    Confirmação = input("A compra está correta? (S/N)  ")
    if Confirmação == "S":
        print("Obrigado pela compra, volte a nos visitar")
    elif Confirmação == "N":
        print("Refaça a compra")
    else:
        print("Opção inválida")

    
    
    
    








