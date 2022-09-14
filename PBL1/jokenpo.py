# Eu tentei usar o básico necessário com exceção do continue e do break 👍
# Importando bibliotecas necessárias:
import random

# Definindo variáveis globais
on = True

# Inicializando o 'loop' infinito do jogo
while on:
    opcao = int(input("Bem vindo ao jokenpô!\n"
                      "Opções:\n"
                      "[0] - Sair do programa\n"
                      "[1] - Humano x Humano\n"
                      "[2] - Humano x Computador\n"
                      "[3] - Computador x Computador\n"
                      "Digite sua opção: "))

    # Tratamento de opção, somente aqui foi utilizado if com continue, pois,
    # ele irá ignorar o restante do código e reiniciar o 'loop' logo acima
    if opcao < 0 or opcao > 3:
        print("Opção inválida, tente novamente!")
        continue

    # Opção 0 o programa se encerra
    if opcao == 0:
        on = False
        break
    # Opção 1, Humano x Humano
    elif opcao == 1:
        # Definindo os contadores e o nome antes do 'loop' para a persistência dos dados na memória
        # caso contrário, seriam redefinidos sempre que o jogo acabasse e a opção fosse jogar novamente
        vitorias_jogador_1, vitorias_jogador_2, num_de_empates = 0, 0, 0
        nome_jogador_1 = input("Digite o nome do 1° jogador: ")
        nome_jogador_2 = input("Digite o nome do 2° jogador: ")

        while on:
            print("\nOpções:\n"
                  "[1] - Pedra 🗿\n"
                  "[2] - Papel 📜\n"
                  "[3] - Tesoura ✂️")

            # O tratamento de opções com while é feito assim o restante do código, então esse serve de exemplo
            # enquanto a opção estiver inválida o 'loop' se repete, caso seja válida apenas prossegue no código
            opcao_jogador_1 = int(input(f"Opção do jogador {nome_jogador_1}: "))
            while opcao_jogador_1 < 0 or opcao_jogador_1 > 3:
                print("Opção inválida, tente novamente!")
                opcao_jogador_1 = int(input("\nOpções:\n"
                                            "[1] - Pedra 🗿\n"
                                            "[2] - Papel 📜\n"
                                            "[3] - Tesoura ✂️\n"))

            opcao_jogador_2 = int(input(f"Opção do jogador {nome_jogador_2}: "))
            while opcao_jogador_2 < 0 or opcao_jogador_2 > 3:
                print("Opção inválida, tente novamente!")
                opcao_jogador_2 = int(input("\nOpções:\n"
                                            "[1] - Pedra\n"
                                            "[2] - Papel 📜\n"
                                            "[3] - Tesoura ✂️\n"))

            # Lógica do pedra, papel e tesoura, formatada para ficar mais bonitinha
            # 1 empata com 1, perde de 2 e ganha de 3
            # 2 ganha de 1, empata com 2 e perde de 3
            # 3 perde de 1, ganha de 2 e empata com 3
            if opcao_jogador_1 == 1:
                if opcao_jogador_2 == 1:
                    print("Empate!")
                    # Adicionando no número de empates totais
                    num_de_empates += 1
                elif opcao_jogador_2 == 2:
                    print(f"Jogador 2 {nome_jogador_2} ganhou!")
                    # Adicionando no número de vitórias do 2° jogador
                    vitorias_jogador_2 += 1
                else:
                    print(f"Jogador 1 {nome_jogador_1} ganhou!")
                    # Adicionando no número de vitórias do 1° jogador
                    vitorias_jogador_1 += 1
            elif opcao_jogador_1 == 2:
                if opcao_jogador_2 == 1:
                    print(f"Jogador 1 {nome_jogador_1} ganhou!")
                    vitorias_jogador_1 += 1
                elif opcao_jogador_2 == 2:
                    print("Empate!")
                    num_de_empates += 1
                else:
                    print(f"Jogador 2 {nome_jogador_2} ganhou!")
                    vitorias_jogador_2 += 1
            else:
                if opcao_jogador_2 == 1:
                    print(f"Jogador 2 {nome_jogador_2} ganhou!")
                    vitorias_jogador_2 += 1
                elif opcao_jogador_2 == 2:
                    print(f"Jogador 1 {nome_jogador_1} ganhou!")
                    vitorias_jogador_1 += 1
                else:
                    print("Empate!")
                    num_de_empates += 1

            opcao = int(input("[1] - Jogar novamente\n"
                              "[2] - Encerrar programa e mostrar dados finais\n"
                              "Opção: "))
            while opcao < 1 or opcao > 2:
                opcao = int(input("Opção inválida, tente novamente!"
                                  "[1] - Jogar novamente\n"
                                  "[2] - Encerrar programa e mostrar dados finais\n"
                                  "Opção: "))
            # Formato padrão em que as estatísticas são mostradas e o programa encerrado
            # apenas algumas mudanças no nome das variáveis apresentadas nas outras opções de jogo
            if opcao == 2:
                print(f"\nObrigado aos Jogadores:\n"
                      f"{nome_jogador_1} e {nome_jogador_2} por jogar! ❤️\n"
                      f"Estatísticas:\n"
                      f"Vitórias do jogador {nome_jogador_1}:{vitorias_jogador_1}\n"
                      f"Vitórias do jogador {nome_jogador_2}:{vitorias_jogador_2}\n"
                      f"Empates:{num_de_empates}\n"
                      f"Encerrando programa =).")
                on = False
                break
    # Opção 2, Humano x Computador
    elif opcao == 2:
        vitorias_jogador_1, vitorias_computador, num_de_empates = 0, 0, 0
        nome_jogador_1 = input("Digite o nome do jogador: ")

        while on:
            print("Opções:\n"
                  "[1] - Pedra 🗿\n"
                  "[2] - Papel 📜\n"
                  "[3] - Tesoura ✂️\n")

            opcao_jogador_1 = int(input(f"Opção do jogador {nome_jogador_1}: "))
            while opcao_jogador_1 < 0 or opcao_jogador_1 > 3:
                print("Opção inválida, tente novamente!")
                opcao_jogador_1 = int(input("\nOpções:\n"
                                            "[1] - Pedra 🗿\n"
                                            "[2] - Papel 📜\n"
                                            "[3] - Tesoura ✂️\n"))

            # Opção randômica de 1 a 3 para o computador, outros usos no código são idênticos a esse
            opcao_computador = random.randint(1, 3)

            if opcao_jogador_1 == 1:
                if opcao_computador == 1:
                    print("Empate!")
                    num_de_empates += 1
                elif opcao_computador == 2:
                    print(f"O Computador ganhou!")
                    vitorias_computador += 1
                else:
                    print(f"Jogador 1 {nome_jogador_1} ganhou!")
                    vitorias_jogador_1 += 1
            elif opcao_jogador_1 == 2:
                if opcao_computador == 1:
                    print(f"Jogador 1 {nome_jogador_1} ganhou!")
                    vitorias_jogador_1 += 1
                elif opcao_computador == 2:
                    print("Empate!")
                    num_de_empates += 1
                else:
                    print(f"O Computador ganhou!")
                    vitorias_computador += 1
            else:
                if opcao_computador == 1:
                    print(f"O Computador ganhou!")
                    vitorias_computador += 1
                elif opcao_computador == 2:
                    print(f"Jogador 1 {nome_jogador_1} ganhou!")
                    vitorias_jogador_1 += 1
                else:
                    print("Empate!")
                    num_de_empates += 1

            opcao = int(input("[1] - Jogar novamente\n"
                              "[2] - Encerrar programa e mostrar dados finais\n"
                              "Opção: "))
            while opcao < 1 or opcao > 2:
                opcao = int(input("Opção inválida, tente novamente!"
                                  "[1] - Jogar novamente\n"
                                  "[2] - Encerrar programa e mostrar dados finais\n"
                                  "Opção: "))
            if opcao == 2:
                print(f"\nObrigado ao Jogador:\n"
                      f"{nome_jogador_1} por jogar! ❤️\n"
                      f"Estatísticas:\n"
                      f"Vitórias do jogador {nome_jogador_1}:{vitorias_jogador_1}\n"
                      f"Vitórias do computador:{vitorias_computador}\n"
                      f"Empates:{num_de_empates}\n"
                      f"Encerrando programa =).")
                on = False
                break
    # Opção 3, Computador x Computador
    else:
        vitorias_computador_1, vitorias_computador_2, num_de_empates = 0, 0, 0

        while on:
            nome_computador_1, nome_computador_2 = "Computador 1", "Computador 2"

            opcao_computador_1 = random.randint(1, 3)
            opcao_computador_2 = random.randint(1, 3)

            if opcao_computador_1 == 1:
                if opcao_computador_2 == 1:
                    print("Empate!")
                    num_de_empates += 1
                elif opcao_computador_2 == 2:
                    print(f"O {nome_computador_2} ganhou!")
                    vitorias_computador_2 += 1
                else:
                    print(f"Jogador 1 {nome_computador_1} ganhou!")
                    vitorias_computador_1 += 1
            elif opcao_computador_1 == 2:
                if opcao_computador_2 == 1:
                    print(f"Jogador 1 {nome_computador_1} ganhou!")
                    vitorias_computador_1 += 1
                elif opcao_computador_2 == 2:
                    print("Empate!")
                    num_de_empates += 1
                else:
                    print(f"O {nome_computador_2}ganhou!")
                    vitorias_computador_2 += 1
            else:
                if opcao_computador_2 == 1:
                    print(f"O {nome_computador_2} ganhou!")
                    vitorias_computador_2 += 1
                elif opcao_computador_2 == 2:
                    print(f"Jogador 1 {nome_computador_1} ganhou!")
                    vitorias_computador_1 += 1
                else:
                    print("Empate!")
                    num_de_empates += 1

            opcao = int(input("[1] - Jogar novamente\n"
                              "[2] - Encerrar programa e mostrar dados finais\n"
                              "Opção: "))
            while opcao < 1 or opcao > 2:
                opcao = int(input("Opção inválida, tente novamente!"
                                  "[1] - Jogar novamente\n"
                                  "[2] - Encerrar programa e mostrar dados finais\n"
                                  "Opção: "))
            if opcao == 2:
                print(f"\nObrigado por utilizar o programa! ❤️\n"
                      f"Estatísticas:\n"
                      f"Vitórias do {nome_computador_1}:{vitorias_computador_1}\n"
                      f"Vitórias do {nome_computador_2}:{vitorias_computador_2}\n"
                      f"Empates:{num_de_empates}\n"
                      f"Encerrando programa =).")
                on = False
                break
