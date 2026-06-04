import colorama
from colorama import Fore, Style
import getpass

palavras = [("massa"),("força"),("tempo"),("calor"),("carga"),("campo"),("vetor"),("fluxo"),("pesos"),("ondas"),("raios"),("luzes"),("cores"),("lente"),("vidro"),("metal"),("gases"),("vapor"),("ciclo"),("vácuo"),("átomo"),("fóton"),("bóson"),("glúon"),("quark"),("diodo"),("pilha"),("motor"),("cunha"),("polia"),("bloco"),("placa"),("barra"),("corda"),("molas"),("eixos"),("plano"),("ponto"),("linha"),("curva"),("retas"),("graus"),("erros"),("média"),("denso"),("leves"),("baixo"),("largo"),("curto"),("finos"),("gelos"),("fogos"),("chama"),("focos"),("metro"),("litro"),("grama"),("joule"),("hertz"),("tesla"),("weber"),("gauss"),("watts"),("volts"),("méson"),("pulso"),("ruído"),("fusão"),("corpo"),("sigma"),("delta"),("omega"),("gamas"),("túnel"),("spins"),("sabor"),("píons"),("káons"),("múons"),("bohrs"),("cosmo"),("astro"),("lunar"),("solar"),("gotas"),("bolha"),("ânion")]
chute = ""
tentativas = 6
linha1 = ["-"]*5
linha2 = ["-"]*5
linha3 = ["-"]*5
linha4 = ["-"]*5
linha5 = ["-"]*5
linha6 = ["-"]*5

def verificar_chute(chute, palavra):
    resultado = []
    for i in range(len(chute)):
        if chute[i] == palavra[i]:
            resultado.append(Fore.GREEN + chute[i] + Style.RESET_ALL)

        elif chute[i] in palavra:
            resultado.append(Fore.YELLOW + chute[i] + Style.RESET_ALL)

        else:
            resultado.append(Fore.RED + chute[i] + Style.RESET_ALL)
    
    return resultado

def randomizar_palavra():
    import random
    palavra = random.choice(palavras)
    return palavra

def tabuleiro():
    linhas = [linha1, linha2, linha3, linha4, linha5, linha6]
    for linha in linhas:
        print(" ".join(linha))

print("Bem vindo ao TERMO-FÍSICO!")
with open("ignore/regras_do_termo.txt", "r") as r:
    print(r.read())

palavra = randomizar_palavra()

while True:
    chute = input("\n Digite uma palavra de 5 letras:")
    print("\n")
    if chute == palavra and tentativas <= 6:
        linha_colorida = verificar_chute(chute, palavra)
        if tentativas == 6:
            linha1 = linha_colorida
        elif tentativas == 5:
            linha2 = linha_colorida
        elif tentativas == 4:           
            linha3 = linha_colorida
        elif tentativas == 3:
            linha4 = linha_colorida
        elif tentativas == 2:
            linha5 = linha_colorida
        elif tentativas == 1:
            linha6 = linha_colorida
        tabuleiro()
        print("\n Parabéns! Você acertou a palavra!")
        break
    
    elif chute != palavra and tentativas > 0:
        linha_colorida = verificar_chute(chute, palavra)
        if tentativas == 6:
            linha1 = linha_colorida
        elif tentativas == 5:
            linha2 = linha_colorida
        elif tentativas == 4:           
            linha3 = linha_colorida
        elif tentativas == 3:
            linha4 = linha_colorida
        elif tentativas == 2:
            linha5 = linha_colorida
        elif tentativas == 1:
            linha6 = linha_colorida
        tabuleiro()
        print("\n Você errou! Tente novamente.")
        tentativas -= 1

    else:
        print("Suas tentativas acabaram! A palavra era:", palavra)
        break
