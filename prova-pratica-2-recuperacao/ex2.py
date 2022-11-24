# Variáveis
lista_de_inteiros = [0] * 10


# Função para imprimir somente os números pares
def imprime_par(lista):
    print("Números pares:")
    for par in range(10):
        if (lista[par] % 2) == 0:
            print(f"Número par:{lista[par]} encontrado na posição: {par}")


# Função para imprimir somente os números ímpares
def imprime_impar(lista):
    print("Números ímpares:")
    for impar in range(10):
        if (lista[impar] % 2) == 1:
            print(f"Número ímpar: {lista[impar]} encontrado na posição: {impar}")


# Main do programa
def main():
    for inteiro in range(10):
        lista_de_inteiros[inteiro] = int(input("Digite um valor inteiro: "))
        print(lista_de_inteiros)

    imprime_par(lista_de_inteiros)
    print()
    imprime_impar(lista_de_inteiros)


main()
