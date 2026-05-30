palavras = ["fusão", "átomo", "quark", "força"]
chute = []
tentativas = 6

def randomizar_palavra():
    import random
    palavra = random.choice(palavras)
    return palavra

print("Bem vindo ao TERMO-FÍSICO!")
with open("ignore/regras_do_termo.txt", "r") as r:
    print(r.read())

palavra = randomizar_palavra()

while True:
    chute = input("Digite uma palavra de 5 letras: ")
    if chute == palavra and tentativas <= 6:
        print("Parabéns! Você acertou a palavra!")
        break
    elif chute != palavra and tentativas <= 6 and tentativas > 0:
        print("Tente novamente!")
        tentativas -= 1
    else:
        print("Suas tentativas acabaram! A palavra era:", palavra)
        break