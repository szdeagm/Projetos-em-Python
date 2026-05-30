

print("Seja bem-vindo aos meus primeiros projetos em python! Aqui você pode escolher entre uma calculadora ou um jogo da velha.")
with open("ignore/gatinho.txt", "r") as f:
    print(f.read())

while True:
    escolha_de_projetos = int(input("Digite 1 para acessar a calculadora ou 2 para acessar o jogo da velha: "))
    if escolha_de_projetos == 1:
        with open("ignore/Calculadora.py", "r") as c:
            exec(c.read())
    elif escolha_de_projetos == 2:
        with open("ignore/Jogo_da_velha.py", "r") as j:
            exec(j.read())
    else:    
        print("Opção inválida, por favor escolha entre 1 ou 2.")
    break 