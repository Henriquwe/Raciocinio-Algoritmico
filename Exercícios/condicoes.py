def __verificar_condicoes__(cond_idade, cond_media):
    if cond_idade >= 18:
        print("Já pode tirar habilitação!")
    else:
        print("Não pode tirar habilitação!")

    if cond_media >= 7:
        print("Com essa média você está aprovado!")
    else:
        print("Com essa media você deve fazer o exame final")


def __elo__(pdls):
    if pdls < 999:
        print(f"Com {pdls} pdls, você está no elo Ferro!")
    elif 1000 <= pdls <= 1999:
        print(f"Com {pdls} pdls, você está no elo Bronze!")
    elif 2000 <= pdls <= 2999:
        print(f"Com {pdls} pdls, você está no elo Prata")
    elif 3000 <= pdls <= 3999:
        print(f"Com {pdls} pdls, você está no elo Ouro!")
    elif 4000 <= pdls <= 4999:
        print(f"Com {pdls} pdls, você está no elo Platina!")
    elif 5000 <= pdls <= 5999:
        print(f"Com {pdls} pdls, você está no elo Diamante!")
    elif 6000 <= pdls <= 6999:
        print(f"Com {pdls} pdls, você está no elo Mestre!")
    elif 7000 <= pdls <= 7999:
        print(f"Com {pdls} pdls, você está no elo Grão-Mestre!")
    else:
        print(f"Com {pdls} pdls, você está no elo CHALLENGER!")


idade = int(input("Digite a idade a ser verificada: "))
media = float(input("Digite a média a ser verificada: "))
qtd_pdls = int(input("Digite a quantidade de pdl no lolzinho: "))

__verificar_condicoes__(idade, media)
__elo__(qtd_pdls)
