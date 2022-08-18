# Exercício 2

def calcular_aluguel(quantidade_de_dias):
    valor_aluguel = quantidade_de_dias * 100
    return print("O aluguel total ficou em:", valor_aluguel)


qtd_dias = int(input("Por quantos dias deseja alugar o carro?: "))

calcular_aluguel(qtd_dias)
