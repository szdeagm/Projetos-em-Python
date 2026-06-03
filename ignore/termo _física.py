import colorama
from colorama import Fore, Style

palavras = [("fusão"), ("átomo"), ("quark"), ("força")]
chute = ""
tentativas = 6
linha1 = []
linha2 = []
linha3 = []
linha4 = []
linha5 = []
linha6 = []


def tabuleiro():
    topo = [" ___________"]
    linha1 = ["| _ _ _ _ _ |"]
    linha2 = ["| _ _ _ _ _ |"]
    linha3 = ["| _ _ _ _ _ |"]
    linha4 = ["| _ _ _ _ _ |"]
    linha5 = ["| _ _ _ _ _ |"]
    linha6 = ["| _ _ _ _ _ |"]
    linha7 = ["|___________|"]
    if tentativas == 6:
        linha1 = [range(len(chute))]   
    elif tentativas == 5:
        linha2 = [range(len(chute))]
    elif tentativas == 4:
        linha3 = [range(len(chute))]
    elif tentativas == 3:
        linha4 = [range(len(chute))]
    elif tentativas == 2:
        linha5 = [range(len(chute))]
    elif tentativas == 1:
        linha6 = [range(len(chute))]    
    else: 
        linha7 = [range(len(chute))]
    return topo + linha1 + linha2 + linha3 + linha4 + linha5 + linha6 + linha7

def verificar_chute(chute, palavra):
    resultado = []
    for i in range(len(chute)):
        if chute[i] == palavra[i]:
            resultado.append(Fore.GREEN + chute[i] + Style.RESET_ALL)
            print(Fore.GREEN + chute[i] + Style.RESET_ALL, end="")
        elif chute[i] in palavra:
            resultado.append(Fore.YELLOW + chute[i] + Style.RESET_ALL)
            print(Fore.YELLOW + chute[i] + Style.RESET_ALL, end="")
        else:
            resultado.append(chute[i])
            print(Fore.RED + chute[i] + Style.RESET_ALL, end="")

    return resultado

def randomizar_palavra():
    import random
    palavra = random.choice(palavras)
    return palavra

print("Bem vindo ao TERMO-FÍSICO!")
with open("ignore/regras_do_termo.txt", "r") as r:
    print(r.read())

palavra = randomizar_palavra()

print("\nDigite uma palavra de 5:")
while True:
    chute = input("")
    exec(tabuleiro())
    if chute == palavra and tentativas <= 6:
        print("Parabéns! Você acertou a palavra!")
        break
    elif chute != palavra and tentativas <= 6 and tentativas > 0:
        verificar_chute(chute, palavra)
        tentativas -= 1
    else:
        print("Suas tentativas acabaram! A palavra era:", palavra)
        break