ano = int(input("Escreva um ano \n"))


if (ano % 4) != 0:
    print(f"{ano} nao eh bissexto")
elif (ano % 4 == 0) and (ano % 100 != 0):
    print(f"{ano} eh bissexto")
elif (ano % 100) == 0 and (ano / 400 != 0):
     print(f"{ano} nao eh bissexto")
elif (ano % 400) == 0:
     print(f"{ano} eh bissexto")