def verificar_maior(n1, n2):
    if n1 > n2:
        print(f"O primeiro número é maior que o segundo ({n1} > {n2})")
    else:
        print(f"O segundo número é maior que o primeiro ({n2}) > ({n1})")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

verificar_maior(num1, num2)