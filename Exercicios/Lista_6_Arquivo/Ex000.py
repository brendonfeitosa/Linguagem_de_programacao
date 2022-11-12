# GERENCIAMENTO DE FUNCIONÁRIOS COM ARQUIVO
class TipoFuncionario: 
    matricula = 0
    nome = ''
    salario = 0.0

def Cadastrar(vetFuncionario):
    arquivo = open('arq_Funcionario.txt', 'w')
    print('Cadastro de Funcionários.........................')
    for i in range(3):
        f = TipoFuncionario()
        f.matricula = int(input('Digite a matrícula: '))
        f.nome = input('Digite o nome: ')
        f.salario = float(input('Digite o salário: '))
        vetFuncionario.append(f)
        arquivo.write(f'{f.matricula},{f.nome},{f.salario:.2f}\n')
        #ou
        #arquivo.write('%d %s %.2f\n' % (f.matricula, f.nome, f.salario))
    arquivo.close()
    return vetFuncionario


def Mostrar():
    arquivo = open('arq_Funcionario.txt', 'r')
    print('Apresentação dos dados dos funcionários .........')
    print('Matrícula\tNome\tSalário')
    for linha in arquivo.readlines():
        mat, nome, sal = linha.strip().split(",") #strip retirar caracteres em branco no inicio e no fim das frases, split separa as informações como eu quero
        print(mat,'\t',nome,'\t',sal)
    arquivo.close()

def main():
    op = 1
    while op >=1 and op <= 2:
        print('*** Gerenciamento de Funcionários COM ARQUIVO ***')
        print('1- Cadastrar')
        print('2- Mostrar')
        print('3- Sair')
        op = int(input('Digite a opção: '))
        if op == 1:
            vetF=[]
            vetF = Cadastrar(vetF)
        elif op == 2:
            Mostrar()            

main()
