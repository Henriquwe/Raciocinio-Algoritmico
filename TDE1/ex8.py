raio = float(input("Digite o raio dos tanques cilíndricos: "))
altura = float(input("Digite a altura dos tanques a serem pintados: "))

area_total = raio * altura
qtd_de_latas = area_total / 15
custo_em_reais = qtd_de_latas * 50.00

print(f"Para pintar essa parede, "
      f"são necessárias {qtd_de_latas:.0f} latas de tinta, totalizando no custo de: {custo_em_reais:.2f}R$")
