# Variáveis
on = True
linhas = 3
colunas = 3


# Função para soma dos valores na diagonal, valendo-se da informação que a matriz é 3x3
# logo, a diagonal será 0,0 - 1,1 - 2,2
def soma_diagonal_principal():
    soma = 0
    diagonal = 0
    for valor in range(3):
        soma += matriz[diagonal][diagonal]
        diagonal += 1
    print(f"A soma dos números da diagonal principal é de: {soma}")


# Função para a verificação do maior valor encontrado na diagonal, feito através de um IF
# o maior valor por definição é o primeiro e se caso encontrado um maior ao decorrer da verificação
# ele é atribuído ao maior
def maior_valor_diagonal():
    global maior
    diagonal = 0
    maior = matriz[diagonal][diagonal]
    for valor in range(3):
        if matriz[diagonal][diagonal] > maior:
            maior = matriz[diagonal][diagonal]
        diagonal += 1

    print(f"O maior valor encontrado na diagonal principal da matriz é: {maior}")


# Função para verificação do menor, mesma coisa que a verificação do maior mas verificando se é menor no IF
def menor_valor_diagonal():
    global menor
    diagonal = 0
    menor = matriz[diagonal][diagonal]
    for valor in range(3):
        if matriz[diagonal][diagonal] < menor:
            menor = matriz[diagonal][diagonal]
        diagonal += 1

    print(f"O menor valor encontrado na diagonal principal da matriz é: {menor}")


# Criando a matriz 3x3, faltou capricho nesse código
matriz = [0] * linhas
for linha in range(linhas):
    matriz[linha] = [0] * colunas

# Inserindo os valores na matriz
for linha in range(linhas):
    for coluna in range(colunas):
        matriz[linha][coluna] = int(input(f"Digite um valor para a posição [{linha}, {coluna}]: "))


# Chamada das função e retorno para o usuário
soma_diagonal_principal()
maior_valor_diagonal()
menor_valor_diagonal()
