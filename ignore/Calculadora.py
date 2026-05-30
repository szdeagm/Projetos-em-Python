from ast import While
import math


n1 = float(input('Coloque aqui o primeiro número:'))
n2 = float(input('Coloque aqui o segundo número:'))

while True:
    operação = int(input( "Selecione o número da operação desejada: 1. Soma | 2. Subtração | 3.Multiplicação | 4.Divisão | 5. Potência: "))
    soma = float( n1 + n2 )
    subtração = float( n1 - n2 )
    multiplicação = float( n1*n2 )
    divisão = float( n1/n2 )
    potência = float( n1**n2 )
    if operação == 1:
        print(f"O resultado é: {soma}")
    elif operação == 2:
        print(f"O resultado é: {subtração}")
    elif operação == 3:
        print(f"O resultado é: {multiplicação}")
    elif operação == 4:
        print(f"O resultado é: {divisão}")
    else:
        print(f"O resultado é: {potência}")

    sair = input("Deseja realizar outra operação? (s/n) ou ir para o menu de projetos? (m): ")
    if sair == "s":
        continue
    elif sair == "m":
        with open("inicio.py", "r") as i:
            exec(i.read())
    else:
        print("Obrigado por usar a calculadora!")
        break
