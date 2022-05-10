import random

def jogar():

    print("***************************************")
    print("Bem vindo no jogo de Adivinhação!!!")
    print("***************************************")

    numero_secreto = random.randrange(1, 101)  # Range 0.0 - 1.0
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #Interpolação de Strings

        chute_str = input("Digite o seu número entre 1 e 100: ")
        chute = int(chute_str)
        print("Você digitou ", chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print ("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print ("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            if(rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))

    print("Fim do Jogo")

if(__name__ == "__main__"):
    jogar()