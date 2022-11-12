'''1. Elabore uma estrutura para representar e armazenar 10 produtos (código, nome, preço). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura.'''

class TipoProdutos:
    codigo = 0
    nome = ''
    preco = 0.00

def cadastrar_produtos():
    vet_prod = []
    arquivo = open('cadastrar_produtos.txt','w')
    print('{:-^70}'.format(' Cadastro de Produtos '))
    for i in range(1, 2):
        p = TipoProdutos()
        p.codigo = int(input('\nDigite o código do produto: '))
        p.nome = input('Digite o nome do produto: ')
        p.preco = float(input('Digite o preço do produto: R$ '))
        vet_prod.append(p)
        arquivo.write(f'{p.codigo},{p.nome},{p.preco}')
    arquivo.close()
    return vet_prod

def main():
    cadastrar_produtos()
main()
