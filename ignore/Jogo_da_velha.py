import io
saida = io.StringIO()
saida2 = io.StringIO()
saida3 = io.StringIO()
saida4 = io.StringIO()
saida5 = io.StringIO()
saida6 = io.StringIO()
saida7 = io.StringIO()
saida8 = io.StringIO()
saida9 = io.StringIO()

jogador1 = []
jogador2 = []

def verificar_vitoria(jogador1, jogador2):
    linhas = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    colunas = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    diagonais = [(1, 5, 9), (3, 5, 7)]
    for linhas in linhas:
         if all(posicao in jogador1 for posicao in linhas):
            return "Jogador 1 venceu!"
         elif all(posicao in jogador2 for posicao in linhas):
            return "Jogador 2 venceu!"
    for colunas in colunas:
        if all(posicao in jogador1 for posicao in colunas):
            return "Jogador 1 venceu!"
  

JV = ("  1 | 2 | 3\n ------------\n  4 | 5 | 6\n ------------\n  7 | 8 | 9")

print("Boas vindas ao MELHOR jogo da velha!\n\n  1 | 2 | 3\n ------------\n  4 | 5 | 6\n ------------\n  7 | 8 | 9\n")

while True:
  J1 = int(input("Jogador 1, você será X. Escolha uma casa para iniciar a jogada:" ))
  if J1 == 1:
    a = "  X | 2 | 3\n ------------\n  4 | 5 | 6\n ------------\n  7 | 8 | 9"
  elif J1 == 2:
    a = "  1 | X | 3\n ------------\n  4 | 5 | 6\n ------------\n  7 | 8 | 9"
  elif J1 == 3:
    a = "  1 | 2 | X\n ------------\n  4 | 5 | 6\n ------------\n  7 | 8 | 9"
  elif J1 == 4:
    a = "  1 | 2 | 3\n ------------\n  X | 5 | 6\n ------------\n  7 | 8 | 9"
  elif J1 == 5:
    a = "  1 | 2 | 3\n ------------\n  4 | X | 6\n ------------\n  7 | 8 | 9"
  elif J1 == 6:
    a = "  1 | 2 | 3\n ------------\n  4 | 5 | X\n ------------\n  7 | 8 | 9"
  elif J1 == 7:
    a = "  1 | 2 | 3\n ------------\n  4 | 5 | 6\n ------------\n  X | 8 | 9"
  elif J1 == 8:
    a = "  1 | 2 | 3\n ------------\n  4 | 5 | 6\n ------------\n  7 | X | 9"
  elif J1 == 9:
    a = "  1 | 2 | 3\n ------------\n  4 | 5 | 6\n ------------\n  7 | 8 | X"
  else:
    print("Escolha uma casa válida!")
  print(a, file=saida)
  print(saida.getvalue())
  break

print("Boa jogada!")
print("\n")

while True:
    J2 = int(input("Jogador 2, você será O. Escolha uma casa para iniciar a jogada:" ))
    if J2 != J1 and J2 == 1:
      b = saida.getvalue().replace("1", "O", 1)
    elif J2 != J1 and J2 == 2:
      b = saida.getvalue().replace("2", "O", 2)
    elif J2 != J1 and J2 == 3:
      b = saida.getvalue().replace("3", "O", 3)
    elif J2 != J1 and J2 == 4:
      b = saida.getvalue().replace("4", "O", 4)
    elif J2 != J1 and J2 == 5:
      b = saida.getvalue().replace("5", "O", 5)
    elif J2 != J1 and J2 == 6:
      b = saida.getvalue().replace("6", "O", 6)
    elif J2 != J1 and J2 == 7:
      b = saida.getvalue().replace("7", "O", 7)
    elif J2 != J1 and J2 == 8:
      b = saida.getvalue().replace("8", "O", 8)
    elif J2 != J1 and J2 == 9:
      b = saida.getvalue().replace("9", "O", 9)
    else:
      print("Escolha uma casa válida!")

    print(b, file=saida2)
    print(saida2.getvalue())
    break

print("Boa jogada!")
print("\n")

while True:
    J3 = int(input("Jogador 1 é a sua vez! escolha uma casa:"))
    if J3 != J1 and J3 != J2 and J3 == 1:
      c = saida2.getvalue().replace("1", "X", 1)
    elif J3 != J1 and J3 != J2 and J3 == 2:
      c = saida2.getvalue().replace("2", "X", 2)
    elif J3 != J1 and J3 != J2 and J3 == 3:
      c = saida2.getvalue().replace("3", "X", 3)
    elif J3 != J1 and J3 != J2 and J3 == 4:
      c = saida2.getvalue().replace("4", "X", 4)
    elif J3 != J1 and J3 != J2 and J3 == 5:
      c = saida2.getvalue().replace("5", "X", 5)
    elif J3 != J1 and J3 != J2 and J3 == 6:
      c = saida2.getvalue().replace("6", "X", 6)
    elif J3 != J1 and J3 != J2 and J3 == 7:
      c = saida2.getvalue().replace("7", "X", 7)
    elif J3 != J1 and J3 != J2 and J3 == 8:
      c = saida2.getvalue().replace("8", "X", 8)
    elif J3 != J1 and J3 != J2 and J3 == 9:
      c = saida2.getvalue().replace("9", "X", 9)
    else:
      print("Escolha uma casa válida!")

    print(c, file=saida3)
    print(saida3.getvalue())
    break

print("Boa jogada!")
print("\n")

while True:
    J4 = int(input("Jogador 2 é a sua vez! escolha uma casa:"))
    if J4 != J1 and J4 != J2 and J4 != J3 and J4 == 1:
      d = saida3.getvalue().replace("1", "O", 1)
    elif J4 != J1 and J4 != J2 and J4 != J3 and J4 == 2:
      d = saida3.getvalue().replace("2", "O", 2)
    elif J4 != J1 and J4 != J2 and J4 != J3 and J4 == 3:
      d = saida3.getvalue().replace("3", "O", 3)
    elif J4 != J1 and J4 != J2 and J4 != J3 and J4 == 4:
      d = saida3.getvalue().replace("4", "O", 4)
    elif J4 != J1 and J4 != J2 and J4 != J3 and J4 == 5:
      d = saida3.getvalue().replace("5", "O", 5)
    elif J4 != J1 and J4 != J2 and J4 != J3 and J4 == 6:
      d = saida3.getvalue().replace("6", "O", 6)
    elif J4 != J1 and J4 != J2 and J4 != J3 and J4 == 1:
      d = saida3.getvalue().replace("7", "O", 7)
    elif J4 != J1 and J4 != J2 and J4 != J3 and J4 == 1:
      d = saida3.getvalue().replace("8", "O", 8)
    elif J4 != J1 and J4 != J2 and J4 != J3 and J4 == 1:
      d = saida3.getvalue().replace("9", "O", 9)
    else:
      print("Escolha uma casa válida!")

    print(d, file=saida4)
    print(saida4.getvalue())
    break

print("Boa jogada!")
print("\n")

while True:
    J5 = int(input("Jogador 1 é a sua vez! escolha uma casa:"))
    if J5 != J1 and J5 != J2 and J5 != J3 and J5 != J4 and J5 == 1:
      e = saida4.getvalue().replace("1", "X", 1)
    elif J5 != J1 and J5 != J2 and J5 != J3 and J5 != J4 and J5 == 2:
      e = saida4.getvalue().replace("2", "X", 2)
    elif J5 != J1 and J5 != J2 and J5 != J3 and J5 != J4 and J5 == 3:
      e = saida4.getvalue().replace("3", "X", 3)
    elif J5 != J1 and J5 != J2 and J5 != J3 and J5 != J4 and J5 == 4:
      e = saida4.getvalue().replace("4", "X", 4)
    elif J5 != J1 and J5 != J2 and J5 != J3 and J5 != J4 and J5 == 5:
      e = saida4.getvalue().replace("5", "X", 5)
    elif J5 != J1 and J5 != J2 and J5 != J3 and J5 != J4 and J5 == 6:
      e = saida4.getvalue().replace("6", "X", 6)
    elif J5 != J1 and J5 != J2 and J5 != J3 and J5 != J4 and J5 == 7:
      e = saida4.getvalue().replace("7", "X", 7)
    elif J5 != J1 and J5 != J2 and J5 != J3 and J5 != J4 and J5 == 8:
      e = saida4.getvalue().replace("8", "X", 8)
    elif J5 != J1 and J5 != J2 and J5 != J3 and J5 != J4 and J5 == 9:
      e = saida4.getvalue().replace("9", "X", 9)
    else:
      print("Escolha uma casa válida!")

    print(e, file=saida5)
    print(saida5.getvalue())
    break

print("Boa jogada!")
print("\n")

while True:
    J6 = int(input("Jogador 2 é a sua vez! escolha uma casa:"))
    if J6 != J1 and J6 != J2 and J6 != J3 and J6 != J4 and J6 != J5 and J6 == 1:
      f = saida5.getvalue().replace("1", "O", 1)
    elif J6 != J1 and J6 != J2 and J6 != J3 and J6 != J4 and J6 != J5 and J6 == 2:
      f = saida5.getvalue().replace("2", "O", 2)
    elif J6 != J1 and J6 != J2 and J6 != J3 and J6 != J4 and J6 != J5 and J6 == 3:
      f = saida5.getvalue().replace("3", "O", 3)
    elif J6 != J1 and J6 != J2 and J6 != J3 and J6 != J4 and J6 != J5 and J6 == 4:
      f = saida5.getvalue().replace("4", "O", 4)
    elif J6 != J1 and J6 != J2 and J6 != J3 and J6 != J4 and J6 != J5 and J6 == 5:
      f = saida5.getvalue().replace("5", "O", 5)
    elif J6 != J1 and J6 != J2 and J6 != J3 and J6 != J4 and J6 != J5 and J6 == 6:
      f = saida5.getvalue().replace("6", "O", 6)
    elif J6 != J1 and J6 != J2 and J6 != J3 and J6 != J4 and J6 != J5 and J6 == 7:
      f = saida5.getvalue().replace("7", "O", 7)
    elif J6 != J1 and J6 != J2 and J6 != J3 and J6 != J4 and J6 != J5 and J6 == 8:
      f = saida5.getvalue().replace("8", "O", 8)
    elif J6 != J1 and J6 != J2 and J6 != J3 and J6 != J4 and J6 != J5 and J6 == 9:
      f = saida5.getvalue().replace("9", "O", 9)
    else:
      print("Escolha uma casa válida!")

    print(f, file=saida6)
    print(saida6.getvalue())
    break

print("Boa jogada!")
print("\n")

while True:
    J7 = int(input("Jogador 1 é a sua vez! escolha uma casa:"))
    if J7 != J1 and J7 != J2 and J7 != J3 and J7 != J4 and J7 != J5 and J7 != J6 and J7 == 1:
      g = saida6.getvalue().replace("1", "X", 1)
    elif J7 != J1 and J7 != J2 and J7 != J3 and J7 != J4 and J7 != J5 and J7 != J6 and J7 == 2:
      g = saida6.getvalue().replace("2", "X", 2)
    elif J7 != J1 and J7 != J2 and J7 != J3 and J7 != J4 and J7 != J5 and J7 != J6 and J7 == 3:
      g = saida6.getvalue().replace("3", "X", 3)
    elif J7 != J1 and J7 != J2 and J7 != J3 and J7 != J4 and J7 != J5 and J7 != J6 and J7 == 4:
      g = saida6.getvalue().replace("4", "X", 4)
    elif J7 != J1 and J7 != J2 and J7 != J3 and J7 != J4 and J7 != J5 and J7 != J6 and J7 == 5:
      g = saida6.getvalue().replace("5", "X", 5)
    elif J7 != J1 and J7 != J2 and J7 != J3 and J7 != J4 and J7 != J5 and J7 != J6 and J7 == 6:
      g = saida6.getvalue().replace("6", "X", 6)
    elif J7 != J1 and J7 != J2 and J7 != J3 and J7 != J4 and J7 != J5 and J7 != J6 and J7 == 7:
      g = saida6.getvalue().replace("7", "X", 7)
    elif J7 != J1 and J7 != J2 and J7 != J3 and J7 != J4 and J7 != J5 and J7 != J6 and J7 == 8:
      g = saida6.getvalue().replace("8", "X", 8)
    elif J7 != J1 and J7 != J2 and J7 != J3 and J7 != J4 and J7 != J5 and J7 != J6 and J7 == 9:
      g = saida6.getvalue().replace("9", "X", 9)
    else:
      print("Escolha uma casa válida!")

    print(g, file=saida7)
    print(saida7.getvalue())
    break

print("Boa jogada!")
print("\n")

while True:
    J8 = int(input("Jogador 2 é a sua vez! escolha uma casa:"))
    if J8 != J1 and J8 != J2 and J8 != J3 and J8 != J4 and J8 != J5 and J8 != J6 and J8 != J7 and J8 == 1:
      h = saida7.getvalue().replace("1", "O", 1)
    elif J8 != J1 and J8 != J2 and J8 != J3 and J8 != J4 and J8 != J5 and J8 != J6 and J8 != J7 and J8 == 2:
      h = saida7.getvalue().replace("2", "O", 2)
    elif J8 != J1 and J8 != J2 and J8 != J3 and J8 != J4 and J8 != J5 and J8 != J6 and J8 != J7 and J8 == 3:
      h = saida7.getvalue().replace("3", "O", 3)
    elif J8 != J1 and J8 != J2 and J8 != J3 and J8 != J4 and J8 != J5 and J8 != J6 and J8 != J7 and J8 == 4:
      h = saida7.getvalue().replace("4", "O", 4)
    elif J8 != J1 and J8 != J2 and J8 != J3 and J8 != J4 and J8 != J5 and J8 != J6 and J8 != J7 and J8 == 5:
      h = saida7.getvalue().replace("5", "O", 5)
    elif J8 != J1 and J8 != J2 and J8 != J3 and J8 != J4 and J8 != J5 and J8 != J6 and J8 != J7 and J8 == 6:
      h = saida7.getvalue().replace("6", "O", 6)
    elif J8 != J1 and J8 != J2 and J8 != J3 and J8 != J4 and J8 != J5 and J8 != J6 and J8 != J7 and J8 == 7:
      h = saida7.getvalue().replace("7", "O", 7)
    elif J8 != J1 and J8 != J2 and J8 != J3 and J8 != J4 and J8 != J5 and J8 != J6 and J8 != J7 and J8 == 8:
      h = saida7.getvalue().replace("8", "O", 8)
    elif J8 != J1 and J8 != J2 and J8 != J3 and J8 != J4 and J8 != J5 and J8 != J6 and J8 != J7 and J8 == 9:
      h = saida7.getvalue().replace("9", "O", 9)
    else:
      print("Escolha uma casa válida!")

    print(h, file=saida8)
    print(saida8.getvalue())

    print("Boa jogada!")
    print("\n")

    while True:
        J9 = int(input("Jogador 1 é a sua vez! escolha uma casa:"))
        if J9 != J1 and J9 != J2 and J9 != J3 and J9 != J4 and J9 != J5 and J9 != J6 and J9 != J7 and J9 == 1:
          h = saida8.getvalue().replace("1", "X", 1)
        elif J9 != J1 and J9 != J2 and J9 != J3 and J9 != J4 and J9 != J5 and J9 != J6 and J9 != J7 and J9 == 2:
          h = saida8.getvalue().replace("2", "X", 2)
        elif J9 != J1 and J9 != J2 and J9 != J3 and J9 != J4 and J9 != J5 and J9 != J6 and J9 != J7 and J9 == 3:
          h = saida8.getvalue().replace("3", "X", 3)
        elif J9 != J1 and J9 != J2 and J9 != J3 and J9 != J4 and J9 != J5 and J9 != J6 and J9 != J7 and J9 == 4:
          h = saida8.getvalue().replace("4", "X", 4)
        elif J9 != J1 and J9 != J2 and J9 != J3 and J9 != J4 and J9 != J5 and J9 != J6 and J9 != J7 and J9 == 5:
          h = saida8.getvalue().replace("5", "X", 5)
        elif J9 != J1 and J9 != J2 and J9 != J3 and J9 != J4 and J9 != J5 and J9 != J6 and J9 != J7 and J9 == 6:
          h = saida8.getvalue().replace("6", "X", 6)
        elif J9 != J1 and J9 != J2 and J9 != J3 and J9 != J4 and J9 != J5 and J9 != J6 and J9 != J7 and J9 == 7:
          h = saida8.getvalue().replace("7", "X", 7)
        elif J9 != J1 and J9 != J2 and J9 != J3 and J9 != J4 and J9 != J5 and J9 != J6 and J9 != J7 and J9 == 8:
          h = saida8.getvalue().replace("8", "X", 8)
        elif J9 != J1 and J9 != J2 and J9 != J3 and J9 != J4 and J9 != J5 and J9 !=J6 and J9 != J7 and J9 == 9:
          h = saida8.getvalue().replace("9", "X", 9)
        else:
          print("Escolha uma casa válida!")
        break
    print(h, file=saida9)
    print(saida9.getvalue())
    
    print("Bom_Jogo! FIM! ")
    1
    break
while True:
    sair = input("Deseja jogar novamente? (s/n) ou ir para o menu de projetos? (m): ")
    if sair == "s":
        with open("ignore/Jogo_da_velha.py", "r") as j:
            exec(j.read())
    elif sair == "m":
        with open("inicio.py", "r") as i:
            exec(i.read())
    elif sair == "n":
        break
    else:
        print("Escolha uma opção válida!")
