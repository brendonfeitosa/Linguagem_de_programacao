'''3. Elabore uma estrutura para representar um produto (código, nome, preço). Crie uma função para cadastrar 5 produtos. Crie outra função para aplicar 10% de aumento no preço do produto e apresente, por meio de outra função, todos os dados do produtos cadastrados, após o aumento. Construa uma função para cada opção do menu a seguir:
Menu do Sistema

Cadastrar
Reajustar
Visualizar
Sair
Qual opção deseja?'''

class TipoProdutos():
    codigo = 0
    nome = ''
    preco = 0.00

def menu():
    print('\n {:-^30}'.format(' MENU '))
    print('''  [ 1 ] Cadastrar
  [ 2 ] Reajustar
  [ 3 ] Visualizar
  [ 4 ] Pesquisar
  [ 5 ] Excluir por menor preço
  [ 6 ] Sair''')
    opcao = int(input('\nDigite a sua opção: '))
    return opcao

def cadastrar():
    vet_p = []
    for i in range(2):
        a = TipoProdutos()
        a.codigo = int(input('\nDigite o código do produto: '))
        a.nome = input('Digite o nome do produto: ')
        a.preco = float(input('Informe o preço do produto: R$ '))
        vet_p.append(a)
    return vet_p

def reajustar(vet_p):
    for i in vet_p:
        i.preco = i.preco * (10 / 100)
    print('Reajuste realizado.....')
    return vet_p

def visualizar(vet_p):
    if len(vet_p) > 0:
        for i in range(len(vet_p)):
            print(f'\nCódigo: {vet_p[i].codigo} \tNome: {vet_p[i].nome} \tPreço: {vet_p[i].preco:.2f}')
    else:
        print('Não há produtos cadastrados...')
    

def reajustar(vet_p):
    if len(vet_p) > 0:
        for i in range(len(vet_p)):
            vet_p[i].preco = vet_p[i].preco + (vet_p[i].preco * (10 / 100))
        print('\nReajuste realizado com sucesso.....')
    else:
        print('\nNão há produtos cadastrados....')
    return vet_p

def pesquisar(nome_pesquisado, vet_p): #usar esta lógica para o exercico 4
    cont = 0
    for i in range(len(vet_p)):
        if nome_pesquisado in vet_p[i].nome:
            print('\nProduto encontrado!')
        else:
            cont += 1 #implemento desta forma para que o print não se repita para cada nome cadastrado
    if cont >= len(vet_p): #assim ele vai retornar apenas 1 vez se não tiver o produto cadastrado
        print('\nProduto não encontrado!')

def excluir(vet_p):
    if len(vet_p) > 0:
        print('\nExclusão do Produto com menor valor')
        for i in range(len(vet_p)):
            if i == 0:
                indice = i
                menor_preco = vet_p[i].preco
            if vet_p[i].preco <= menor_preco:
                menor_preco = vet_p[i].preco
                indice = i
        vet_p.pop(indice) #aqui ocorreu uma alteração no vetor, então devemos retornar o vetor alterado
        print('\nExclusão realizada com sucesso.\n')
    else:
        print('\nNão há produtos cadastrados...\n')
    return vet_p

def main():
    v_prod = []
    op = menu()
    while op >= 1 and op <= 5:
        if op == 1:
            v_prod = cadastrar()
        elif op == 2:
            reajustar(v_prod)
        elif op == 3:
            visualizar(v_prod)
        elif op == 4:
            nome_pesquisar = input('Digite produto que deseja pesquisar? ')
            pesquisar(nome_pesquisar, v_prod)
        elif op == 5:
            v_prod = excluir(v_prod)
        elif op == 6:
            print('FIM!!!')
            break
        op = menu()
main()
