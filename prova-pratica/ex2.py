idade = int(input("Digite a sua idade: "))
tempo_de_servico = int(input("Digite, em anos, o seu tempo de serviço: "))

if idade >= 65:
    print("A aposentadoria está disponível pela faixa de idade!")
elif tempo_de_servico >= 30:
    print("A aposentadoria está disponível pelo tempo de serviço!")
elif idade >= 60 or tempo_de_servico >= 25:
    print("A aposentadoria está disponível pela idade em conjunto com o tempo de serviço!")
else:
    print("A aposentadoria ainda não está disponível!")
