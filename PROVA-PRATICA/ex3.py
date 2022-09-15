letra_secreta = "h"

contador = 0
while contador <= 5:
    if contador == 5:
        print("Acabaram suas chances =(")
        break
    print(f"{contador + 1}° chance de 5")
    escolha = input("Digite uma letra: ")

    if escolha == letra_secreta:
        print("Parabéns, você acertou!")
        break
    else:
        print("Errou!")
    contador += 1
