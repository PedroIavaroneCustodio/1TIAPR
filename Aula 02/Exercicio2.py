numero = float(input("Escreva um numero \n"))
resto = numero % 2

if resto == 1:
    print(f"O numero {numero} eh impar")
else:
    print(f"O numero {numero} eh par")