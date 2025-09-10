preco = float(input("Digite o preco do produto: \n R$"))
qtd = int(input("Digite a quantidade a ser comprada \n"))

if qtd > 10:
    valortot = (preco * qtd) * 0.9
else:
    valortot = preco * qtd

print(f"A compra deu no total: R${valortot}")