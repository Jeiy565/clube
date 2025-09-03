import random

opcoes = ["Pedra", "Papel", "Tesoura"]

while 1:
    
    escolha_usuario = input("Escolha Pedra, Papel ou Tesoura: ")
    print(f"Você escolheu: {escolha_usuario}")
    escolha_computador = random.choice(opcoes)
    print(f"Computador escolheu: {escolha_computador}")
    if escolha_usuario == escolha_computador:
        print("É um empate!")
    elif (escolha_usuario == "Pedra" and escolha_computador == "Tesoura") or \
         (escolha_usuario == "Papel" and escolha_computador == "Pedra") or \
         (escolha_usuario == "Tesoura" and escolha_computador == "Papel"):
        print("Você ganhou!")
    else:
        print("Computador ganhou!")
    
    pergunta1 = input("quer jogar novamente?: ")
    if pergunta1 == ('sim'): 
        continue
    if pergunta1 == ('nao'):
        break
