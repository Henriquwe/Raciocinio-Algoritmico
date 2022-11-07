saldo = 0.0

while True:
    print("Bem vindo ao banco Roubaseudinheiro!\n")
    opcao = int(input("Menu de opções:\n"
                      "1 - Consultar Saldo\n"
                      "2 - Sacar\n"
                      "3 - Depositar\n"
                      "4 - Sair\n"
                      "Opção: "))

    while opcao < 1 or opcao > 4:
        opcao = int(input("Opção inválida, tente novamente!"
                          "1 - Consultar Saldo\n"
                          "2 - Sacar\n"
                          "3 - Depositar\n"
                          "4 - Sair\n"
                          "Opção: "))

    if opcao == 1:
        print(f"O saldo atual da sua conta bancária é: {saldo}\n")

    elif opcao == 2:
        saque = float(input("Digite o quanto deseja sacar: "))
        if saque > saldo:
            print("Você não possui esse saldo em sua conta bancária!\n")
            continue
        saldo = saldo - saque
        print(f"Saque no valor de: {saque}R$ feito com sucesso!")

    elif opcao == 3:
        # Podia fazer direto no saldo, mas para mostrar a quantidade eu utilizo mais uma variável
        deposito = float(input("Digite a quantidade a ser depositada: "))
        saldo = saldo + deposito
        print(f"Quantidade de {deposito}R$ depositado com sucesso!")

    else:
        print("\nSaindo do programa e lembre-se o Banco Roubaseudinheiro está sempre com você!\n")
        break


