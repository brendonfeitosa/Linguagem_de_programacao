'''5. Faça um programa que realize o cadastro de contas bancarias com as seguintes informações: numero da conta, nome do titular e saldo. O banco permitirá o cadastramento de 15 contas. **Crie uma função para cada opção do menu** a seguir. Utilize a estrutura na passagem de parâmetro:
Menu de opções:
1. Cadastrar contas
2. Visualizar todas as contas
3. Consultar por nome
4. Alterar nome e/ou saldo de um número de conta
5. Excluir a conta com menor saldo
6. Sair

Observação: 

* No item de menu 4. Alterar nome e/ou saldo de um número de conta, entenda que apenas pode ser alterado o nome e o saldo depois que você pesquisar pelo número da conta.
* No item 5 do menu, encontre o menor saldo dentre todos cadastrados, **depois exclua esta ÚNICA conta.**. O assunto de excluir algo de um vetor foi dado na disciplina de Algoritmo.'''

# Percorra todo os vetor e quando a condição de encontrar um menor saldo for executada, guarde o índice
# Fora do laço de repetição, exclua pelo índice, por exemplo com o comando pop(índice), vimos em Vetor/Algoritmo
#item 4, alterar 
from time import sleep
class TipoCliente:
    n_conta = 0.0
    nome = ''
    saldo = 0.0

def menu():
    print('\n {:-^40}'.format(' MENU '))
    print('''\n  [ 1 ] Cadastrar contas
  [ 2 ] Visualizar todas as contas
  [ 3 ] Consultar por nome
  [ 4 ] Alterar nome e/ou saldo de um número de conta
  [ 5 ] Excluir a conta com menor saldo
  [ 6 ] Sair''')
    opcao = int(input('\nDigite a sua opção: '))
    return opcao

def cadastrar():
    vetor_contas = []
    for i in range(2):
        a = TipoCliente()
        a.n_conta = input('\nDigite o número da conta: ')
        a.nome = input('Digite o nome do titular da conta: ')
        a.saldo = float(input('Digite o saldo da conta: R$ '))
        vetor_contas.append(a)
    return vetor_contas

def visualizar(v_conta):
    for i in range(len(v_conta)):
        print('\nRESULTADO DA CONSULTA:')
        print(f'\nNúmero da conta: {v_conta[i].n_conta} \tNome do titular: {v_conta[i].nome} \tSaldo R$ {v_conta[i].saldo}')

def consultar(v_conta):
    nome_consulta = input('\nDigite o nome que quer consultar: ')
    cont = 0
    for i in range(len(v_conta)):
        if nome_consulta == v_conta[i].nome:
            print('\nO nome digitado esta cadastrado....')
        else:
            cont += 1
    if cont >= len(v_conta):
        print('\nO nome digitado não tem uma conta cadastrada....')

def alterar(v_conta):
    if len(v_conta) > 0:
        cont = 0
        consulta_conta = input('\nDigite o número da conta que deseja alterar: ')
        for i in range(len(v_conta)):
            if consulta_conta == v_conta[i].n_conta:
                print('\nConta localizada, qual alteração deseja fazer?')
                print('''\n   [ 1 ] Alterar nome do titular da conta! 
    [ 2 ] Alterar saldo da conta!
    [ 3 ] Voltar ao menu anterior!''')
                opcao = int(input('\nDigite a sua opção: '))
                if opcao == 1:
                    alterar_nome = input('\nDigite o nome do novo titular da conta: ')
                    v_conta[i].nome = alterar_nome
                    print('Nome do titular alterado com sucesso!')
                elif opcao == 2:
                    alterar_saldo = float(input('\nDigite o novo saldo da conta: R$ '))
                    v_conta[i].saldo = alterar_saldo
                    print('Saldo da conta alterado com sucesso!')
                elif opcao == 3:
                    menu()
                else:
                    print('Opção inválida....')
            else:
                cont += 1
        if cont >= len(v_conta):
            print('Não há contas cadastradas...')
    return v_conta

def excluir(v_conta):
    if len(v_conta) > 0:
        print('\nExclusão da conta com o menor saldo....')
        sleep(2)
        for i in range(len(v_conta)):
            if i == 0:
                indice = i
                menor_saldo = v_conta[i].saldo
            if v_conta[i].saldo <= menor_saldo:
                menor_saldo = v_conta[i].saldo
                indice = i
        v_conta.pop(indice)
        print('\nA conta com menor saldo foi excluída.')
    else:
        print('\nNão existem contas cadastradas.')
    return v_conta

def main():
    op = menu()
    while op >= 1 and op <= 6:
        if op == 1:
            vet_conta = cadastrar()
        elif op == 2:
            visualizar(vet_conta)
        elif op == 3:
            consultar(vet_conta)
        elif op == 4:
            alterar(vet_conta)
        elif op == 5:
            vet_conta = excluir(vet_conta)
        elif op == 6:
            print('\nFIM!')
            break
        op = menu()
main()
