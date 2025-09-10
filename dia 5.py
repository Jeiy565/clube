import random

lancar = 1


def inicializar():
  print("Cara (1) - Coroa (2) - Sair (0)")
  return input("Cara ou Coroa?: ")

def testa_lancar(cara_ou_coroa, lancar):
  if lancar == "0":
    print("Jogo fechado")
    lancar = "0"

  elif cara_ou_coroa == 1 and lancar == "1":
    print("Ganhou, deu Cara!")

  elif cara_ou_coroa == 2 and lancar == "2":
    print("Ganhou, deu Coroa!")

  else:
    print("Perdeu, deu {}".format("Cara" if cara_ou_coroa == 1 else "Coroa"))
  print()
  print()

def testa_lancar_valido(lancar):

  temp = True

  lancar = inicializar()

  if lancar == "1" or lancar == "2" or lancar == "0":
    print()
    return lancar
  else:
    while temp:

      print()
      print(f"{lancar} não é um input válido")
      print("Escolha um dos valores abaixo!")
      print()
      lancar = inicializar()

      if lancar == "1" or lancar == "2" or lancar == "0":
        print()
        temp = False
        return lancar


while lancar != "0":

  lancar = testa_lancar_valido(lancar)

  cara_ou_coroa = random.randint(1,2)

  testa_lancar(cara_ou_coroa, lancar)
