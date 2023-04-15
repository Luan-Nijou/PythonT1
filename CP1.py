# RM98920 / Luan Nijou
print("BEM VINDO A VINHARIA ")
nome = input("Coloque seu nome completo:")
Idade = int(input("Coloque sua idade:"))
EndereçoDoCliente = input("Coloque seu endereço:")
EndereçoDaEntrega = input("Coloque o endereço da entrega:")
cep = int(input("Coloque o número do seu CEP:"))
MeioDeCompra = input("Qual o meio de compra(Exemplos: Cartão de crédito): ")
CatalogoVinho = ("Vinhos a venda ---> (1)Vinho_A->R$50 / (2)Vinho_B->R$100 / (3)Vinho_C->R$150 / (4)Vinho_D->R$200 / (5)Vinho_E->R$250")


QuantidadeVinhoA = 0
ValorViA = 0
QuantidadeVinhoB = 0
ValorViB = 0
QuantidadeVinhoC = 0
ValorViC = 0
QuantidadeVinhoD = 0
ValorViD = 0
QuantidadeVinhoE = 0
ValorViE = 0
ValorTotalCompra = 0
Frete = 10

if Idade<18:  
    print("Pessoas menores de idade não podem comprar")
    
elif Idade>=18:
    print(CatalogoVinho)
    print("Escolha a quantidade de cada vinho que irá comprar, valores acima de 200 reais recebem frete grátis(frete = 10 reais)")
    QuantidadeVinhoA = int(input("Quantidade do VinhoA:"))
    QuantidadeVinhoB = int(input("Quantidade do VinhoB:"))
    QuantidadeVinhoC = int(input("Quantidade do VinhoC:"))
    QuantidadeVinhoD = int(input("Quantidade do VinhoD:"))
    QuantidadeVinhoE = int(input("Quantidade do VinhoE:"))
    ValorViA = 50 * QuantidadeVinhoA
    ValorViB = 100 * QuantidadeVinhoB
    ValorViC = 150 * QuantidadeVinhoC
    ValorViD = 200 * QuantidadeVinhoD
    ValorViE = 250 * QuantidadeVinhoE
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

    
    
    
    








