'''3. Elabore uma estrutura para representar e armazenar 10 alunos (matricula, nome, telefone). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura. Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.

Menu de opções:
1. Cadastrar alunos
2. Visualizar todos os dados
3. Sair'''

class TipoAlunos:
    matricula = 0
    nome = ''
    telefone = ''

def cad_alunos(vetor_alunos):
    arquivo = open('cad_alunos.txt','w')
    print('\n{:-^50}'.format(' Cadastro de Alunos '))
    for i in range(1, 11):
        a = TipoAlunos()
        a.matricula = int(input('\nDigite o número da matricula do aluno: '))
        a.nome = input('Digite o nome do aluno: ')
        a.telefone = input('Digite o número do telefone do aluno: ')
        vetor_alunos.append(a)
        arquivo.write(f'{a.matricula},{a.nome},{a.telefone}\n')
    arquivo.close()
    return vetor_alunos

def visualizar():
    arquivo = open('cad_alunos.txt','r')
    print('\n{:-^50}'.format(' Alunos Cadastrados '))
    print('\nMatricula\tNome\tTelefone')
    for linha in arquivo.readlines():
        mat, nome, tel = linha.strip().split(',') #este caractere deve ser igual ao da linha 15
        print(mat,'\t',nome,'\t',tel)
    arquivo.close()

def main():
    op = 1
    while op >= 1 and op <= 3:
        print('\n{:*^50}'.format(' MENU '))
        print('''\n[ 1 ] Cadastrar alunos
[ 2 ] Visualizar todos os dados
[ 3 ] Sair''')
        op = int(input('\nDigite a opção desejada: '))
        if op == 1:
            vet_alunos = []
            vet_alunos = cad_alunos(vet_alunos)
        elif op == 2:
            visualizar()
        elif op == 3:
            break
main()
