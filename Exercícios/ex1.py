# Exercício 1

def calcular_idade(ano_de_nascimento, ano_atual):
    idade = ano_atual - ano_de_nascimento
    print("A sua idade é de: ", end="")
    return print(idade)


ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2022

calcular_idade(ano_nascimento, ano_atual)
