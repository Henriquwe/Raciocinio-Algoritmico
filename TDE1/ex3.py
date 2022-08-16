# https://www12.senado.leg.br/noticias/materias/2022/06/02/salario-minimo-de-r-1-212-e-promulgado
salario_minimo = 1212.0

salario_total = float(input("Digite o salário total (Mensal ou Anual): "))
qtd_salario_minimo = salario_total / salario_minimo
print(f"O salário de {salario_total} é equivalente a {qtd_salario_minimo:.0f} salário(s) minimo(s).")
