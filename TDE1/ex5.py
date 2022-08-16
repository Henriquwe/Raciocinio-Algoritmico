preco_do_produto = float(input("Digite o preço do produto: "))

# 5% de juros em 3 parcelas resultaria em 15% de juros totais ou estou enganado?
valor_em_tres_parcelas = preco_do_produto + (preco_do_produto / 100) * 15
valor_em_duas_parcelas = preco_do_produto / 2
valor_a_vista = preco_do_produto - (preco_do_produto / 100) * 5
print(f"Valor do produto em 3° parcelas com 5% de Juros: {valor_em_tres_parcelas}.")
print(f"Valor do produto em 2° parcelas: {valor_em_duas_parcelas}.")
print(f"Valor do produto à vista e com desconto de 5%: {valor_a_vista}.")