mnome = []
msalario = []

for linha in range(2): # índice da linha
    vnome = []
    vsalario = []
    for coluna in range(3): # índice da coluna
        vnome.append(input('Digite o nome: '))
        vsalario.append(float(input('Digite o salário: ')))
    mnome.append(vnome)
    msalario.append(vsalario)

for linha in range(len(mnome)): # len(mnome) mostra a quantidade de linhas
    for coluna in range(len(msalario[0])): # lenmsalario[0] mostra a qtde de colunas
        print(mnome[linha][coluna], '- R$' ,msalario[linha][coluna],end='\t')
    print()

for linha in range(len(mnome)): # len(mnome) mostra a quantidade de linhas
    for coluna in range(len(msalario[0])): # lenmsalario[0] mostra a qtde de colunas
        if msalario[linha][coluna] >= 300:
            print(linha,'-', coluna,'-',mnome[linha][coluna], '- R$' ,msalario[linha][coluna])
    
