# Solicite ao usuario usando entrada de dados ate que um numero par seja fornecido

while True:
    numero = int(input("Digite um número par: "))
    if numero % 2 == 0:
        print(f"Obrigado por fornecer o número par: {numero}")
        break
    else:
        print(f"O número {numero} não é par. Tente novamente.")