# Variáveis
alunos = [""] * 5
notas = [0] * 5

# Loop para a inserção dos nomes
for aluno in range(5):
    nome = input(f"Digite o nome do {aluno+1}° aluno: ")
    alunos[aluno] = nome
    print(alunos)
print()

# Loop para inserção das notas
for aluno in range(5):
    nota = int(input(f"Digite uma nota entre 0 e 10 para o aluno {alunos[aluno]}: "))
    while nota < 0 or nota > 10:
        print("Nota inválida, digite uma nota entre 0 e 10!")
        nota = int(input(f"Digite uma nota entre 0 e 10 para o aluno {alunos[aluno]}: "))
    notas[aluno] = nota
print()

# Loop para demostrar o nome e a nota correlacionada, dizendo qual a situação do aluno
for aluno in range(5):
    if notas[aluno] >= 7:
        print(f"O aluno {alunos[aluno]} foi aprovado com a nota: {notas[aluno]}")
    elif 4 < notas[aluno] < 7:
        print(f"O aluno {alunos[aluno]} está de recuperação com a nota: {notas[aluno]} ")
    else:
        print(f"O aluno {alunos[aluno]} está reprovado com a nota: {notas[aluno]}")



