hora_atual = int(input("Digite qual é a hora nesse exato momento: "))
minutos_atuais = int(input("Digite os minutos nesse exato momento: "))
segundos_atuais = int(input("Digite os segundos nesse exato momento: "))

print(f"Se passaram {hora_atual}h {minutos_atuais}m {segundos_atuais}s desde o começo do dia, óbvio;")

hora_atual = hora_atual - 24
minutos_atuais = minutos_atuais - 60
segundos_atuais = segundos_atuais - 60

print(f"Faltam {hora_atual}h {minutos_atuais}m {segundos_atuais}s para acabar o dia.")
