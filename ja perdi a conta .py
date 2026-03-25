while 1:
    N = int(input('Digite a quantidade de numeros a serem falados: '))
    if N >= 1 and N <= 100000:
        break
    else:
        print("Valor invalido! Digite um numero entre 1 e 100000")





x = []

i = 0

while 1:
    if 1 == N:
        break
    while 1:
        digito = int(input("Digite um numero"))
        if digito >= 0 and digito <= 100 :
            break 
        else :
            print("Valor invalido! Digite um numero entre 1 e 100000")


    if digito == 0:
        x.pop()
    elif digito > 0:
        x.append(digito)

    i = i + 1

resultado = sum(x)

if resultado < 0 and resultado > 100000:
    resultado = 0
else :
    print(resultado)

