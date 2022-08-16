# Calcular área do círculo através do raio elevado ao quadrado (2) * n° de PI (Aproximadamente 3,1416)
pi = 3.14
raio = float(input("Digite o raio do círculo que terá a área calculada: "))
area_do_circulo = pi * (raio ** 2)
print(f"Tendo como raio {raio:.2f}, esse círculo têm {area_do_circulo:.2f} de área!")
