# Versão incorreta do trabalho, estava apenas fazendo testes kkkkkk
# Jogo do pedra-papel-tesoura
# Realizando imports:
import random

# Definindo variáveis que podem ou não ser utilizadas durante a execução do programa:
nomeJogador1, nomeJogador2 = "", ""
nomeMaquinaRandom, nomeMaquina1, nomeMaquina2 = "Máquina Random", "Máquina 1", "Máquina 2"
empates, winsJogador1, winsJogador2, winsMaquinaRandom, winsMaquina1, winsMaquina2 = 0, 0, 0, 0, 0, 0
on = True

while on:
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
        nomeJogador1 = input("Digite o nick do 1° jogador: ")
        nomeJogador2 = input("Digite o nick do 2° jogador: ")

        print("Opções pra jogada: \n"
              "[1] - Pedra \n"
              "[2] - Papel \n"
              "[3] - Tesoura \n"
              "[4] - Voltar \n")

        opcaoJogador1 = int(input(f"Opção do 1° jogador {nomeJogador1}: "))
        if opcaoJogador1 == 4:
            continue
        while opcaoJogador1 < 1 or opcaoJogador1 > 4:
            opcaoJogador1 = int(input("Essa opção não é válida, tente novamente! \n"
                                      ": "))

        opcaoJogador2 = int(input(f"Opção do 2° jogador {nomeJogador2}: "))
        if opcaoJogador2 == 4:
            continue
        while opcaoJogador2 < 1 or opcaoJogador2 > 4:
            opcaoJogador2 = int(input("Essa opção não é válida, tente novamente! \n"
                                      ": "))

        if opcaoJogador1 == 1:
            if opcaoJogador2 == 1:
                print("Deu empate!")
                empates += 1
            elif opcaoJogador2 == 2:
                print(f"Jogador {nomeJogador2} ganhou!")
                winsJogador2 += 1
            else:
                print(f"Jogador {nomeJogador1} ganhou!")
                winsJogador1 += 1

        elif opcaoJogador1 == 2:
            if opcaoJogador2 == 1:
                print(f"Jogador {nomeJogador1} ganhou!")
                winsJogador1 += 1
            elif opcaoJogador1 == 2:
                print("Deu empate!")
                empates += 1
            else:
                print(f"Jogador {nomeJogador2} ganhou!")
                winsJogador2 += 1

        else:
            if opcaoJogador2 == 1:
                print(f"Jogador {nomeJogador2} ganhou!")
                winsJogador2 += 1
            elif opcaoJogador2 == 2:
                print(f"Jogador {nomeJogador1} ganhou!")
                winsJogador1 += 1
            else:
                print("Deu empate!")
                empates += 1

    elif opcao == 2:
        nomeJogador1 = input("Digite o nick do 1° jogador: ")

        print("Opções pra jogada: \n"
              "[1] - Pedra \n"
              "[2] - Papel \n"
              "[3] - Tesoura \n"
              "[4] - Voltar \n")

        opcaoJogador1 = int(input(f"Opção do 1° jogador {nomeJogador1}: "))
        if opcaoJogador1 == 4:
            continue
        while opcaoJogador1 < 1 or opcaoJogador1 > 4:
            opcaoJogador1 = int(input("Essa opção não é válida, tente novamente! \n"
                                      ": "))

        opcaoJogador2 = random.randint(1, 3)

        if opcaoJogador1 == 1:
            if opcaoJogador2 == 1:
                print("Deu empate!")
                empates += 1
            elif opcaoJogador2 == 2:
                print(f"Jogador {nomeMaquinaRandom} ganhou!")
                winsMaquinaRandom += 1
            else:
                print(f"Jogador {nomeJogador1} ganhou!")
                winsJogador1 += 1

        elif opcaoJogador1 == 2:
            if opcaoJogador2 == 1:
                print(f"Jogador {nomeJogador1} ganhou!")
                winsJogador1 += 1
            elif opcaoJogador1 == 2:
                print("Deu empate!")
                empates += 1
            else:
                print(f"Jogador {nomeMaquinaRandom} ganhou!")
                winsMaquinaRandom += 1

        else:
            if opcaoJogador2 == 1:
                print(f"Jogador {nomeMaquinaRandom} ganhou!")
                winsMaquinaRandom += 1
            elif opcaoJogador2 == 2:
                print(f"Jogador {nomeJogador1} ganhou!")
                winsJogador1 += 1
            else:
                print("Deu empate!")
                empates += 1

    elif opcao == 3:
        opcaoJogador1 = random.randint(1, 3)
        opcaoJogador2 = random.randint(1, 3)

        if opcaoJogador1 == 1:
            if opcaoJogador2 == 1:
                print("Deu empate!")
                empates += 1
            elif opcaoJogador2 == 2:
                print(f"Jogador {nomeMaquina2} ganhou!")
                winsMaquina2 += 1
            else:
                print(f"Jogador {nomeMaquina1} ganhou!")
                winsMaquina1 += 1

        elif opcaoJogador1 == 2:
            if opcaoJogador2 == 1:
                print(f"Jogador {nomeMaquina1} ganhou!")
                winsMaquina1 += 1
            elif opcaoJogador1 == 2:
                print("Deu empate!")
                empates += 1
            else:
                print(f"Jogador {nomeMaquina2} ganhou!")
                winsMaquina2 += 1

        else:
            if opcaoJogador2 == 1:
                print(f"Jogador {nomeMaquina2} ganhou!")
                winsMaquina2 += 1
            elif opcaoJogador2 == 2:
                print(f"Jogador {nomeMaquina1} ganhou!")
                winsMaquina1 += 1
            else:
                print("Deu empate!")
                empates += 1

    else:
        print(f"======== SUMÁRIO ======== \n"
              f"O número de vitórias do Jogador 1 foi de: {winsJogador1}! \n"
              f"O número de vitórias do Jogador 2 foi de: {winsJogador2}! \n"
              f"O número de empates totais foi de: {empates}! \n"
              f"A máquina randômica ganhou do Jogador um total de: {winsMaquinaRandom} vezes! \n"
              f"O número de vitórias da Máquina 1 foi de: {winsMaquina1}! \n"
              f"O número de vitórias da Máquina 2 foi de: {winsMaquina2}! \n"
              "Encerrando o programa, até a próxima =)")
        on = False
