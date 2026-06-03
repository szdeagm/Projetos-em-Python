import colorama
from colorama import Fore, Style

palavras = [("fusão"), ("átomo"), ("quark"), ("força")]
chute = ""
tentativas = 6

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

while True:
    chute = input("\n aureoDigite uma palavra de 5 letras: ")
    if chute == palavra and tentativas <= 6:
        print("Parabéns! Você acertou a palavra!")
        break
    elif chute != palavra and tentativas <= 6 and tentativas > 0:
        verificar_chute(chute, palavra)
        tentativas -= 1
    else:
        print("Suas tentativas acabaram! A palavra era:", palavra)
        break