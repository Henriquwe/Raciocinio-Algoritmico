# Batalha Naval — Henrique Alves
# Imports utilizados
import random

# Variáveis globais
on = True
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


# Função que verifica se a linha do posicionamento do barco está correta
def verificar_posicionamento_linha(coordenada, barco):
    while coordenada < 0 or coordenada > (num_linhas - 1):
        print(vermelho + "Essa posição de linha está fora do nosso alcance!." + neutro)
        coordenada = int(input(f"Em qual linha deseja posicionar o {barco + 1}° barco [x,-]: "))

    return coordenada


# Função que verifica se a coluna do posicionamento do barco está correta
def verificar_posicionamento_coluna(pos_linha, barco, coordenada):
    while coordenada < 0 or coordenada > (num_colunas - 1):
        print(vermelho + "Essa posição de coluna está fora do nosso alcance!" + neutro)
        coordenada = int(input(f"Em qual coluna deseja posicionar o {barco + 1}° barco [{pos_linha},x]: "))

    return coordenada


# Função que posiciona os barcos na matriz de jogo, recebe tanto a matriz de jogo quanto a de amostra para o jogador,
# pois ambas estão serão alteradas com as opções do jogador.
def posicionar_barco(mat_game, mat_display, qtd_barcos):
    # Laço for para posicionamento dos barcos, por uma posição de linha e coluna
    for barco in range(qtd_barcos):
        posicao_linha = int(input(f"Em qual linha deseja posicionar o {barco + 1}° barco [x,-]: "))
        posicao_linha = verificar_posicionamento_linha(posicao_linha, barco)
        posicao_coluna = int(input(f"Em qual coluna deseja posicionar o {barco + 1}° barco [{posicao_linha},x]: "))
        posicao_coluna = verificar_posicionamento_coluna(posicao_linha, barco, posicao_coluna)
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
        # Cheat, retire o comentário e observe a mágica
        # mat_display[posicao_linha][posicao_coluna] = "@"


# Seguindo a lógica da verificação do posicionamento, mas agora para posição do ataque
def verificar_coordenada_linha(coordenada):
    while coordenada < 0 or coordenada > (num_linhas - 1):
        print(vermelho + "Essa posição de linha está fora do nosso alcance! Mire novamente." + neutro)
        coordenada = int(input(f"Em qual linha deseja coordenar o ataque [x,-]: "))

    return coordenada


# Seguindo a lógica da verificação do posicionamento, mas agora para posição do ataque
def verificar_coordenada_coluna(pos_linha, coordenada):
    while coordenada < 0 or coordenada > (num_colunas - 1):
        print(vermelho + "Essa posição de coluna está fora do nosso alcance! Mire novamente." + neutro)
        coordenada = int(input(f"Em qual coluna deseja coordenar o ataque [{pos_linha},-]: "))

    return coordenada


# Função de atirar, talvez pudesse ser desmembrada em partes menores, entretanto como tudo aqui
# tem o propósito de realizar um disparo eu achei correto deixar assim.
# Recebe a matriz do jogo e de display para atualização dos valores e retorna o contador do PC
# com -1 caso tenha acertado ou igual caso tenha errado, marcando a posição no campo
def atirar(mat_game, mat_display, contador_pc):
    cont_pc = contador_pc

    # Recebe e verifica a linha
    posicao_linha = int(input(f"Em qual linha deseja coordenar o ataque [x,-]: "))
    posicao_linha = verificar_coordenada_linha(posicao_linha)
    # Recebe e verifica a coluna
    posicao_coluna = int(input(f"Em qual coluna deseja coordenar o ataque [{posicao_linha},x]: "))
    posicao_coluna = verificar_coordenada_coluna(posicao_linha, posicao_coluna)
    # mat_game = verifica_coordenada_utilizada(mat_display, mat_game, posicao_linha, posicao_coluna)
    # Caso tenha o valor 1 na posição escolhida foi um acerto

    # Verifica se a posição que foi escolhida já não foi atacada, caso já tenha sido
    # o laço while irá avisar e tentar uma nova posição até a entrada de uma posição válida
    while mat_display[posicao_linha][posicao_coluna] == "X":
        print(vermelho + "\nJá atiramos nessa posição!\n" + neutro)

        posicao_linha = int(input(f"Em qual linha deseja coordenar o ataque [x,-]: "))
        posicao_linha = verificar_coordenada_linha(posicao_linha)

        posicao_coluna = int(input(f"Em qual coluna deseja coordenar o ataque [{posicao_linha},x]: "))
        posicao_coluna = verificar_coordenada_coluna(posicao_linha, posicao_coluna)

    if mat_game[posicao_linha][posicao_coluna] == 1:
        print(verde + "\nTiro certeiro!" + neutro)
        # Substitui na matriz de amostra o campo por um X
        mat_display[posicao_linha][posicao_coluna] = "X"
        # Mostra como está o campo de batalha inimigo após o tiro
        print("Campo de batalha inimigo:")
        display_matriz(num_linhas, num_colunas, mat_display)

        cont_pc = contador_pc - 1
        print(f"dos navios avistados, sobram {cont_pc} almirante!")
        return cont_pc
    else:
        # Se não é 1, foi um erro.
        print(vermelho + "\nTiro n'água!" + neutro)
        mat_display[posicao_linha][posicao_coluna] = "X"

    print("Campo de batalha inimigo:")
    display_matriz(num_linhas, num_colunas, mat_display)

    return cont_pc


# Função do pc atirar, mais simples que a de usuário, pois não há a necessidade
# de fazer verificações a posição escolhida sempre vai ser válida
# a lógica é a mesma, caso 1 acerto caso 0 erro, retorna o contador.
def pc_atirar(mat_game, mat_display, contador_player):
    cont_player = contador_player
    # Utiliza-se a biblioteca random para realizar o disparo
    posicao_linha = random.randint(0, num_linhas - 1)
    posicao_coluna = random.randint(0, num_colunas - 1)

    while mat_display[posicao_linha][posicao_coluna] == "X":
        posicao_linha = random.randint(0, num_linhas - 1)
        posicao_coluna = random.randint(0, num_colunas - 1)

    if mat_game[posicao_linha][posicao_coluna] == 1:
        print(verde + "\nO inimigo ACERTOU um de seus navios!" + neutro)

        mat_game[posicao_linha][posicao_coluna] = 1
        mat_display[posicao_linha][posicao_coluna] = "X"

        print("Seu campo de batalha:")
        display_matriz(num_linhas, num_colunas, mat_display)
        cont_player = contador_player - 1
        return cont_player
    else:
        print(vermelho + "\nParece que o inimigo é cego!" + neutro)
        mat_display[posicao_linha][posicao_coluna] = "X"

    print("Seu campo de batalha:")
    display_matriz(num_linhas, num_colunas, mat_display)

    return cont_player


# Print fofo de início de jogo =)
print(azul + "Bem vindo ao campo de batalha Almirante!\n" + neutro)
# While para manter o programa sempre rodando a menos que o usuário deseje sair
while on:
    # O programa inicia recebendo do jogador os parâmetros do tamanho do campo de batalha
    print("Defina o tamanho do campo de batalha. (Linhas, Colunas)")
    num_linhas = int(input("Linhas: "))
    num_colunas = int(input("Colunas: "))

    # Recebe a quantidade de barcos que serão posicionados e já repassa o valor para os contadores
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

    # Mostrar o campo de batalha do computador, utilizado durante a codificação para testes, caso o cheat esteja ativo
    # revela o local do posicionamento dos barcos do pc
    # (remover comentário) print()
    # (remover comentário) display_matriz(num_linhas, num_colunas, pc_matriz_display)

    print(azul + "\nALMIRANTE, INIMIGO AVISTADO! PERMISSÃO PARA ABRIR FOGO?\n" + neutro)
    while count_player != 0 and count_pc != 0:
        count_pc = atirar(pc_matriz_game, pc_matriz_display, count_pc)
        count_player = pc_atirar(player_matriz_game, player_matriz_display, count_player)

    if count_pc == 0:
        print(verde + "Afundamos todos navios inimigos\nMais uma vitória para a conta, ALMIRANTE!\n" + neutro)
    else:
        print(vermelho + "\nRECUAR!\n" + neutro)

    opcao = int(input("[0] - Engajar o inimigo novamente\n[1] - Se retirar dos mares\n:"))
    if opcao == 1:
        print("Frota se retirando, esperemos o próximo combate!")
        on = False
