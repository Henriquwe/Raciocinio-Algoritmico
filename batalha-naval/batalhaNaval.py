# Batalha Naval - Henrique Alves
# Imports utilizados
import random

# Variáveis
on = True
num_linhas, num_colunas = 5, 10


def init_matriz_game(n_linhas, n_colunas):
    matriz = [0] * n_linhas
    for linha in range(n_linhas):
        matriz[linha] = [0] * n_colunas

    return matriz


def init_matriz_display(n_linhas, n_colunas):
    matriz = ["-"] * n_linhas
    for linha in range(0, n_linhas):
        matriz[linha] = ["-"] * n_colunas

    return matriz


def display_matriz(n_linhas, n_colunas, mat_display):
    for linha in range(n_linhas):
        for coluna in range(n_colunas):
            print(f"[{mat_display[linha][coluna]}]", end='')
        print()


print("Bem vindo ao campo de batalha Almirante!\n")
while on:
    print("Defina o tamanho do campo de batalha. (Linhas, Colunas)")
    num_linhas = int(input("Linhas: "))
    num_colunas = int(input("Colunas: "))

    matriz_game = init_matriz_game(num_linhas, num_colunas)
    matriz_display = init_matriz_display(num_linhas, num_colunas)

    display_matriz(num_linhas, num_colunas, matriz_display)
