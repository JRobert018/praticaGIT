from random import randint


geradorAleatorio = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

for i in geradorAleatorio:
    print(f"O  número sorteado foi: {i}")
print("_"*30)
print(f"O maior número soteado foi: {max(geradorAleatorio)}")#procura o maior número de uma tupla/lista
print(f"O menor número soteado foi: {min(geradorAleatorio)} ")#procura o menor número de uma tupla/lista


