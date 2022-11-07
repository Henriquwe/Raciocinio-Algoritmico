n_linhas = 5
n_colunas = 10

matriz = ["-"] * n_linhas
for linha in range(0, n_linhas):
    matriz[linha] = ["-"] * n_colunas

for linha in range(n_linhas):
    for coluna in range(n_colunas):
        print(f"[{matriz[linha][coluna]}]", end='')
    print()

