contador, numero, maior_num = 0, 0, 0

while contador < 3:
    numero = int(input(f"Digite o {contador + 1}° valor inteiro: "))
    if numero > maior_num:
        maior_num = numero
    contador += 1
print("O maior número digitado foi: " + str(maior_num))

# Não entendi se era pra considerar que o usuário não ia informar valores iguais ou se era pra tratar
# então eu fiz esse código abaixo caso fosse pra tratar kkkkkk não sei sou burro

# numero_1 = int(input("Digite o 1° valor inteiro: "))
# numero_2 = int(input("Digite o 2° valor inteiro: "))
# while numero_2 == numero_1:
#     print("Os números informados devem ser diferentes!")
#     numero_2 = int(input("Digite o 2° valor inteiro: "))
# numero_3 = int(input("Digite o 3° valor inteiro: "))
# while numero_3 == numero_1 or numero_3 == numero_2:
#     print("Os números informados devem ser diferentes!")
#     numero_3 = int(input("Digite o 3° valor inteiro: "))
#
# if numero_1 > numero_2 or numero_1 > numero_3:
#     maior_num = numero_1
# elif numero_2 > numero_1 or numero_2 > numero_3:
#     maior_num = numero_2
# else:
#     maior_num = numero_3
# print("O maior número digitado foi: " + str(maior_num))



