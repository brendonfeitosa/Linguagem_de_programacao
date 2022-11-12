'''
p1 = float(input('Digite a primeira nota: '))
p2 = float(input('Digite a segunda nota: '))
media = (p1 + p2) / 2
if media >= 6 and media < 10:
    print('Aprovado')
elif media == 10:
    print('Aprovado com louvor!!!!')
else:
    print('Reprovado')

### ESTRUTURA DE REPETIÇÃO while COM CONTADOR
qtde_alunos = 0
while qtde_alunos < 3:
    p1 = float(input('Digite a primeira nota: '))
    p2 = float(input('Digite a segunda nota: '))
    media = (p1 + p2) / 2
    print('Sua média é',media)
    qtde_alunos = qtde_alunos + 1
    
### ESTRUTURA DE REPETIÇÃO while SEM CONTADOR
p1 = float(input('Digite a primeira nota..: '))
while p1 > -1 and p1 <= 10:
    p2 = float(input('Digite a segunda nota: '))
    media = (p1 + p2) / 2
    print('Sua média é',media)
    p1 = float(input('Digite a primeira nota: '))

### ESTRUTURA DE REPETIÇÃO for
for qtde_alunos in range(1,3): # <
    p1 = float(input('Digite a primeira nota: '))
    p2 = float(input('Digite a segunda nota: '))
    media = (p1 + p2) / 2
    print('Sua média é',media)

# VETOR
'''
media = []
for qtde_alunos in range(4):
    media.append(float(input('Digite a média: ')))

for i in range(len(media)):
    if media[i] > 8:
        print(i, 'média:',media[i])
    








