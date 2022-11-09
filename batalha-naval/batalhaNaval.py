# Batalha Naval — Henrique Alves
# Imports utilizados
import random

# Variáveis globais
on = True
global count_player, count_pc
global num_linhas
global num_colunas
global player_matriz_game, pc_matriz_game
global player_matriz_display, pc_matriz_display
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
neutro = '\033[0;0m'


# Função que cria a matriz de jogo preenchendo cada espaço com 0, pois na lógica
# um espaço com 0 significará um espaço vazio, alocação de espaços dinâmica através dos parâmetros
# e retornando uma matriz bidimensional.
def init_matriz_game(n_linhas, n_colunas):
    matriz = [0] * n_linhas
    for linha in range(n_linhas):
        matriz[linha] = [0] * n_colunas

    return matriz


# Mesmo processo da matriz de jogo, porém preenchendo com Strings para melhor visualização do jogador
# enquanto estiver jogando, finalidade apenas visual.
def init_matriz_display(n_linhas, n_colunas):
    matriz = ["-"] * n_linhas
    for linha in range(0, n_linhas):
        matriz[linha] = ["-"] * n_colunas

    return matriz


# Função com 2 for aninhado para percorrer uma matriz e mostra-lá de maneira formatada e de bom
# entendimento para o jogador. Recebe o número de linhas e colunas para saber quanto repetir o laço e a matriz
# que irá ser percorrida, para ser possível observar o seu conteúdo interno caso alterado.
def display_matriz(n_linhas, n_colunas, mat_display):
    for linha in range(n_linhas):
        for coluna in range(n_colunas):
            print(f"[{mat_display[linha][coluna]}]", end='')
        print()


# Função para definição da quantidade de barcos que serão posicionados no campo de batalha.
# Com mínimo de 5 e máximo de 10.
def definir_qtd_barcos():
    qtd_barcos = int(input("Digite quantos barcos irá posicionar (Min 5, Máx 10): "))
    # Laço while que verifica se a quantidade de barcos é válida.
    while qtd_barcos < 5 or qtd_barcos > 10:
        print(vermelho + "\nQuantidade inválida, tente um número entre 5 e 10!\n" + neutro)
        qtd_barcos = int(input("Digite quantos barcos irá posicionar (Min 5, Máx 10): "))

    return qtd_barcos


# Função que posiciona os barcos na matriz de jogo, recebe tanto a matriz de jogo quanto a de amostra para o jogador,
# pois ambas estão serão alteradas com as opções do jogador.
def posicionar_barco(mat_game, mat_display, qtd_barcos):
    # Laço for para posicionamento dos barcos, por uma posição de linha e coluna
    for barco in range(qtd_barcos):
        posicao_linha = int(input(f"Em qual linha deseja posicionar o {barco + 1}° barco [x,-]: "))
        posicao_coluna = int(input(f"Em qual coluna deseja posicionar o {barco + 1}° barco [{posicao_linha},x]: "))
        # Verifica se a posição na matriz já não está preenchida com um barco, verificado através do valor 0 ou 1
        # 0 = Posição vazia, 1 = Posição preenchida
        while mat_game[posicao_linha][posicao_coluna] == 1:
            print(vermelho + "\nEssa posição já possuí um barco!\n" + neutro)
            posicao_linha = int(input(f"Em qual linha deseja posicionar o {barco + 1}° barco [x,-]: "))
            posicao_coluna = int(input(f"Em qual coluna deseja posicionar o {barco + 1}° barco [{posicao_linha},x]: "))

        mat_game[posicao_linha][posicao_coluna] = 1
        mat_display[posicao_linha][posicao_coluna] = "@"


# Função para posicionamento dos barcos do computador, feito de forma aleatória através da biblioteca RANDOM.
def pc_posicionar_barco(mat_game, mat_display, qtd_barcos):
    for _ in range(qtd_barcos):
        posicao_linha = random.randint(0, num_linhas - 1)
        posicao_coluna = random.randint(0, num_colunas - 1)

        while mat_game[posicao_linha][posicao_coluna] == 1:
            posicao_linha = random.randint(0, num_linhas - 1)
            posicao_coluna = random.randint(0, num_colunas - 1)

        mat_game[posicao_linha][posicao_coluna] = 1
        # Cheat, retire o comentário e veja a mágica :O
        # mat_display[posicao_linha][posicao_coluna] = "@"


def atirar(mat_game, mat_display):
    posicao_linha = int(input(f"Em qual linha deseja coordenar o ataque [x,-]: "))
    posicao_coluna = int(input(f"Em qual coluna deseja coordenar o ataque [{posicao_linha},x]: "))

    if mat_game[posicao_linha][posicao_coluna] == 1:
        print(verde + "\nTiro certeiro!\n" + neutro)

        mat_game[posicao_linha][posicao_coluna] = 1
        mat_display[posicao_linha][posicao_coluna] = "X"

        display_matriz(num_linhas, num_colunas, mat_display)

        return count_pc - 1
    else:
        print(vermelho + "\nTiro n'água!\n" + neutro)
        mat_display[posicao_linha][posicao_coluna] = "X"

    display_matriz(num_linhas, num_colunas, mat_display)

    return count_pc


def pc_atirar(mat_game, mat_display):
    posicao_linha = random.randint(0, num_linhas-1)
    posicao_coluna = random.randint(0, num_colunas-1)

    if mat_game[posicao_linha][posicao_coluna] == 1:
        print(verde + "\nO inimigo ACERTOU um de seus navios!\n" + neutro)

        mat_game[posicao_linha][posicao_coluna] = 1
        mat_display[posicao_linha][posicao_coluna] = "X"

        display_matriz(num_linhas, num_colunas, mat_display)
        return count_player - 1
    else:
        print(vermelho + "\nParece que o inimigo é cego!\n" + neutro)
        mat_display[posicao_linha][posicao_coluna] = "X"

    display_matriz(num_linhas, num_colunas, mat_display)

    return count_player


print(azul + "Bem vindo ao campo de batalha Almirante!\n" + neutro)
while on:
    # O programa inicia recebendo do jogador os parâmetros do tamanho do campo de batalha
    print("Defina o tamanho do campo de batalha. (Linhas, Colunas)")
    num_linhas = int(input("Linhas: "))
    num_colunas = int(input("Colunas: "))

    qtd_de_barcos = definir_qtd_barcos()
    count_player = qtd_de_barcos
    count_pc = qtd_de_barcos

    # Passa os parâmetros definidos para a matriz do ‘player’ e do computador, iniciando-as
    # com os parâmetros recebidos de número de linhas e colunas.
    player_matriz_game = init_matriz_game(num_linhas, num_colunas)
    player_matriz_display = init_matriz_display(num_linhas, num_colunas)

    pc_matriz_game = init_matriz_game(num_linhas, num_colunas)
    pc_matriz_display = init_matriz_display(num_linhas, num_colunas)

    # Chamada da função para o posicionamento dos barcos no campo de batalha
    # Recebe as matrizes de jogo e amostra definidas nas funções acima como parâmetros
    posicionar_barco(player_matriz_game, player_matriz_display, qtd_de_barcos)
    pc_posicionar_barco(pc_matriz_game, pc_matriz_display, qtd_de_barcos)

    # Mostra para o jogador como está o campo de batalha após posicionamento dos barcos
    print("\nAssim estão posicionados os seus barcos:")
    display_matriz(num_linhas, num_colunas, player_matriz_display)

    ''' Mostrar o campo de batalha do computador, utilizado durante a codificação para testes, caso o cheat esteja ativo
    revela o local do posicionamento dos barcos do pc
    print()
    display_matriz(num_linhas, num_colunas, pc_matriz_display)'''

    print(azul + "\nALMIRANTE, INIMIGO AVISTADO! PERMISSÃO PARA ABRIR FOGO?\n" + neutro)
    while count_player != 0 or count_pc != 0:
        atirar(pc_matriz_game, pc_matriz_display)
        pc_atirar(player_matriz_game, player_matriz_display)

    if count_pc == 0:
        print(verde + "\nMais uma vitória para a conta, ALMIRANTE!\n" + neutro)
    else:
        print(vermelho + "\nRECUAR!\n" + neutro)

    opcao = int("[0] - Engajar o inimigo novamente"
                "[1] - Se retirar dos mares")

    if opcao == 1:
        print("Frota se retirando, esperemos o próximo combate!")
        on = False
