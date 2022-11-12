'''Uma escola precisa montar o cadastro geral de seus alunos. Este cadastro deverá conter as seguintes informações por aluno: nome completo, data de nascimento, telefone, endereço e série atual. Levando em conta que esta escola possui no máximo 500 alunos, como você faria para estruturar estas informações num sistema de gerenciamento para a escola? Implemente utilizando estrutura. Também **use a criação de funções para cada operação**. Use o menu a seguir:
Menu de opções:
1. Cadastrar alunos
2. Consulta por nome
3. Visualizar todos os dados
4. Sair'''

class TipoAlunos:
  nome = ''
  data_nascimento = ''
  telefone = 0
  endereco = ''
  serie_atual = 0

def menu():
    print('\n {:-^30}'.format(' MENU '))
    print('''\n  [ 1 ] Cadastrar
  [ 2 ] Consulta por nome
  [ 3 ] Visualizar todos os dados
  [ 4 ] Sair''')
    opcao = int(input('\nDigite a sua opção: '))
    return opcao

def cadastrar():
    vetor_alunos = []
    for i in range(2):
        a = TipoAlunos()
        a.nome = input('\nDigite o nome completo: ')
        a.data_nascimento = input('Digite a data de nascimento no formato xx/xx/xxxx: ')
        a.telefone = input('Digite o telefone no formato (00) 00000-0000: ')
        a.endereco = input('Digite o endereço: ')
        a.serie_atual = (input('Digite a série atual do aluno: '))
        vetor_alunos.append(a)
    return vetor_alunos

def consultar(vet):
    nome_digitado = input('\nDigite o nome que quer consultar: ')
    cont = 0
    for i in range(len(vet)):
        if nome_digitado == vet[i].nome:
            print('\nNOME CADASTRADO ...')
        else:
            cont += 1
    if cont >= len(vet):
        print('\nNOME NÃO CADASTRADO ...')

def visualizar(vet):
    for i in range(len(vet)):
        print('\nRESULTADO DA CONSULTA!')
        print(f'\tNome: {vet[i].nome}\tData de Nascimento: {vet[i].data_nascimento};\tTelefone: {vet[i].telefone};\tEndereço: {vet[i].endereco};\tSérie atual: {vet[i].serie_atual}')

def main():
    op = menu()
    while op >= 1 and op <= 5:
        if op == 1:
            v_prod = cadastrar()
        elif op == 2:
            consultar(v_prod)
        elif op == 3:
            visualizar(v_prod)
        elif op == 4:
            print('FIM!!!')
            break
        op = menu()
main()
