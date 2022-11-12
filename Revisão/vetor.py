'''
nome = []
media = []

for i in range(4):
    nome.append(input('Digite o nome: '))
    media.append(input('Digite a média: ')))

for i in range(len(nome)):
    if media[i] >= 6:
        print('Índice: ',i,'Nome do aluno:',nome[i],'Média: ',media[i])
'''

#somar o salário de alguns funcionários
vsalario = []
vnome = []
soma = 0
i = 0
salario = float(input('Digite o salário...: '))
while salario > 0:
    vsalario.append(salario)
    vnome.append(input('Digite o nome: '))
    soma = soma + vsalario[i]
    salario = float(input('Digite o salário: '))
    i += 1

print('Resultado da soma',soma,'\n')
print(vnome)
print(vsalario)



    
