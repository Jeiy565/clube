import random

numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 10

print("Bem-vindo ao Jogo de Adivinhação!")

while tentativas < max_tentativas:
    palpite = int(input("Tente adivinhar o numero: "))
    tentativas += 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou! Agora mim de bala pq foi um saco programar essa bosta")
        break
    elif palpite > numero_secreto:
        print("Tente um número menor.")
    else:
        print("Tente um número maior.")

if tentativas == max_tentativas and palpite != numero_secreto:
    print(f"Fim do jogo. O número era {numero_secreto}.")
