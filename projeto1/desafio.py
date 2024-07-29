from random import  randint

geradorAleatorio = randint(1,100)

palpite = int(input("Digite um número entre 1 a 100:"))
while palpite is not geradorAleatorio:
    if palpite > geradorAleatorio:
        palpite = int(input(f"Tente um número menor que {palpite}:"))
    elif palpite < geradorAleatorio:
        palpite = int(input(f"Tente um número maior que {palpite}:"))
print(f"Parabens O número {palpite} é o certo.")