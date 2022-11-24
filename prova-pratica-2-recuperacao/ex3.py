# Variáveis
on = True


# Função para calcular um círculo com base no número de PI e no raio informado
def calcular_circulo():
    pi = 3.14
    raio = float(input("Digite o raio do círculo: "))
    raio = raio ** 2
    print(f"\nA área do círculo é de: {pi * raio:.4}cm²\n")


# Função para calcular a área de um quadrado com base em um dos seus lados
def calcular_quadrado():
    lado = float(input("Digite a área de uma das laterais do quadrado: "))
    print(f"\nA área do quadrado é de: {lado ** 2:.4}\nEm centimetros: {lado * 4}cm²")


# Função para calcular um retângulo através da sua base e da sua altura
def calcular_retangulo():
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    print(f"\nA área do retângulo é de {base * altura}cm²")


# Laço que mantém o programa ativo até o usuário decidir encerrar
while on:

    opcao = int(input("Opções:\n[1] - Calcular um círculo\n"
                      "[2] - Calcular um quadrado\n"
                      "[3] - Calcular retângulo\n"
                      "[4] - Sair do programa\n"
                      "Opção: "))
    while opcao < 1 or opcao > 4:
        print("\nOpção inválida, tente novamente!")
        opcao = int(input("Opções:\n[1] - Calcular um círculo\n"
                          "[2] - Calcular um quadrado\n"
                          "[3] - Calcular retângulo\n"
                          "[4] - Sair do programa\n"
                          "Opção: "))

    if opcao == 1:
        calcular_circulo()
    elif opcao == 2:
        calcular_quadrado()
    elif opcao == 3:
        calcular_retangulo()
    else:
        print("\nEncerrando o programa, até mais! =)")
        on = False
