# Jogo do pedra-papel-tesoura
on = True
while on:
    # Definindo variáveis que podem ou não ser utilizadas durante a execução do programa:
    nomeJogador, nomeJogador2, maquina1, maquina2 = "", "", "", ""
    winsJogador1, winsJogador2, winsMaquina1, winsMaquina2 = 0, 0, 0, 0

    print("Bem vindo ao Jokenpô virtual! \n")
    opcao = int(input("Escolha o modo de jogo \n"
                      "[1] - Jogador x Jogador \n"
                      "[2] - Jogador x Máquina \n"
                      "[3] - Máquina x Máquina \n"
                      "[4] - Sair do programa \n"
                      "Opção: "))

    if opcao < 1 or opcao > 4:
        print("Opção inválida, tente novamente! \n")
        continue

    if opcao == 1:
        nomeJogador = input("Digite o nick do 1° jogador: ")
        nomeJogador2 = input("Digite o nick do 2° jogador: ")

        print("Opções pra jogada: \n"
              "[1] - Pedra \n"
              "[2] - Papel \n"
              "[3] - Tesoura \n")

        opcaoJogador1 = int(input(f"Opção do 1° jogador {nomeJogador}: "))
        while opcaoJogador1 < 1 or opcaoJogador1 > 3:
            opcaoJogador1 = int(input("Essa opção não é válida, tente novamente! \n"
                                      ": "))

        opcaoJogador2 = int(input(f"Opção do 2° jogador {nomeJogador2}: "))
        while opcaoJogador2 < 1 or opcaoJogador2 > 4:
            opcaoJogador2 = int(input("Essa opção não é válida, tente novamente! \n"
                                      ": "))




