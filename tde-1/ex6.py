import math

cateto1 = int(input("Digite o 1° cateto: "))
cateto2 = int(input("Digite o 2° cateto: "))

hipotenusa = cateto1 ** 2 + cateto2 ** 2
hipotenusa = math.sqrt(hipotenusa)
print(f"A hipotenusa desse triângulo retângulo é {hipotenusa}")
