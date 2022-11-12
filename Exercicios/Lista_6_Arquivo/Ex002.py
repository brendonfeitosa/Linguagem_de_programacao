'''2. Elabore uma estrutura para representar e armazenar 10 produtos (código, nome, preço). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura.Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.

Menu de opções:
1. Cadastrar produtos
2. Visualizar todos os dados
3. Sair'''

class TipoProdutos:
    codigo = 0
    nome = ''
    preco = 0.00

def menu():
    print('\n{:*^40}'.format(' MENU '))
    print('\n1. Cadastrar Produtos \n2. Visualizar todos os dados \n3. Sair')
    opcao = int(input('\nDigite uma opção: '))
    while opcao >= 1 and opcao <= 3:
        if opcao == 1:
            vetor_prod = []
            vetor_prod = cad_produtos(vetor_prod)
        elif opcao == 2:
            visualizar()
        elif opcao == 3:
            print('FIM!')
            break
        else:
            print('\nOpção inválida!')
        print('\n{:*^40}'.format(' MENU '))
        print('\n1. Cadastrar Produtos \n2. Visualizar todos os dados \n3. Sair')            
        opcao = int(input('\nDigite uma opção: '))

def cad_produtos(vet_prod):
    arquivo = open('cad_produtos.txt','w')
    print('\n{:-^70}'.format(' Cadastro de Produtos '))
    for i in range(1, 2):
        p = TipoProdutos()
        p.codigo = int(input('\nDigite o código do produto: '))
        p.nome = input('Digite o nome do produto: ')
        p.preco = float(input('Digite o preço do produto: R$ '))
        vet_prod.append(p)
        arquivo.write(f'{p.codigo},{p.nome},{p.preco}\n')
    arquivo.close()
    return vet_prod

def visualizar():
    arquivo = open('cad_produtos.txt','r')
    print('\n{:-^70}'.format('Apresentação de produtos cadastrados'))
    print('\nCodigo\tNome\tPreço')
    for linha in arquivo.readlines():
        cod, nome, prec = linha.strip().split(',')
        print(cod,'\t',nome,'\t',prec)
    arquivo.close()

def main():
    menu()
main()
