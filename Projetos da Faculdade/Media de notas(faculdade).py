total_alunos = 10
total_atividades = 4

for aluno in range(total_alunos):
    print(f"Aluno {aluno + 1}")
    
    soma_notas = 0
    for atividade in range(total_atividades):
        nota = float(input(f"Digite a nota da atividade {atividade + 1}: "))
        soma_notas += nota
    
    media = soma_notas / total_atividades
    
    if media < 5.0:
        print(f"Média: {media:.2f} - Reprovado")
    elif media < 7.0:
        print(f"Média: {media:.2f} - Recuperação")
    else: 
        print(f"Média: {media:.2f} - Aprovado")
    
    
