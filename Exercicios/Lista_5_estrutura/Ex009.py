'''9. (OPCIONAL A IMPLEMTAÇÃO) Uma empresa prestadora de serviços armazena informações sobre os serviços prestados. Sabe-se que a empresa pode realizar no máximo três serviços diariamente. É de interesse de sua direção manter um histórico mensal (30 dias) sobre os serviços prestados.
A empresa realiza quatro tipos de serviços: 
1) pintura; 
2) jardinagem; 
3) faxina e
4) reforma em geral.
Cada serviço realizado deve ser cadastrado com as seguintes informações: número do serviço, valor do serviço, código do serviço e código do cliente, **numa matriz 30x3 referente a estrutura Servico_prestado**.

Cadastre/digite os quatro tipos de serviços (código e descrição) que a empresa poderá realizar. Para isso, utilize um vetor de quatro posições referente a **estrutura Tipo_servico**.
O programa deverá mostrar o seguinte menu de opções:
1. Cadastrar os tipos de serviços
2. Mostrar todos os tipos de serviço
3. Cadastrar os serviços prestados
4. Mostrar todos os serviços prestados
5. Mostrar os serviços prestados em determinado dia
6. Mostrar os serviços prestados dentro de um intervalo de valor
7. Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço
8. Sair

**Para a opção 1**: deve-se cadastrar os tipos de serviços oferecidos pela empresa, com código e descrição.

**Para a opção 3**: deve-se considerar que deverão ser cadastrados os serviços prestados ao logo do mês. Em cada dia podem ser cadastrados, no máximo, três serviços prestados.

Utilize uma matriz capaz de armazenar em cada posição todas as informações referentes a um serviço prestado (número, valor, código do serviço, código do cliente). **Cada linha representa um dia do mês**. Dessa maneira, considere a matriz com dimensão 30 × 3.

Solicite o dia em que o serviço foi prestado e as demais informações.
Lembre-se de que a empresa só pode prestar os serviços que já tenham sido cadastrados no vetor de tipo de serviços.

Caso o usuário digite um código de tipo de serviço inválido, o programa deverá mostrar uma mensagem de erro.

Quando o usuário tentar cadastrar mais de três serviços prestados em um mesmo dia, também deverá mostrar uma mensagem de erro.

**Para a opção 5**: o programa deverá receber o dia que se deseja consultar e mostrar os respectivos serviços prestados.

**Para a opção 6**: o programa deverá receber o valor mínimo e o valor máximo e mostrar os serviços prestados que estiverem nesse intervalo.

**Para a opção 7**: o programa deverá mostrar todos os serviços prestados, conforme o exemplo a seguir.

                  DIA 01


No do serviço| Valor do serviço R$| Código do serviço| Descrição| Código do cliente
---|---|---|---|---
100| 200,00| 1| Pintura| 1
150| 100,00| 3| Faxina| 5
201| 640,00| 4| Reforma em geral| 2

                  DIA 02

No do serviço| Valor do serviço R$| Código do serviço| Descrição| Código do cliente
---|---|---|---|---
301| 600,00| 4| Reforma em geral| 3
280| 352,00| 1| Pintura| 2
306| 200,00| 2| Jardinagem| 1'''


class TipoServico():
    codigo = 0
    descricao = " "

class ServicoPrestado():
    numero = 0
    valor = 0
    codigo_servico = 0
    codigo_cliente = 0


def Menu(vet_servico):
    while True:
        print("\n{:*^66}".format(" CADASTRO DE SERVIÇOS "))
        print('''\n1. Cadastrar os tipos de serviços
2. Mostrar todos os tipos de serviço
3. Cadastrar os serviços prestados
4. Mostrar todos os serviços prestados
5. Mostrar os serviços prestados em determinado dia
6. Mostrar os serviços prestados dentro de um intervalo de valor
7. Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço
8. Sair''')
        op = int(input("\nDigite a opção desejada: "))
        if op == 1:
            p = TipoServico()
            j = TipoServico()
            f = TipoServico()
            r = TipoServico()
            print("\nCadastrar os tipos de serviço!")
            print('''\nTipos de Serviço: 
\n1. Pintura;
2. Jardinagem;
3. Faxina;
4. Reforma em geral;''')
            op_cad_serv = int(input("\nQual serviço deseja cadastrar? "))
            while op_cad_serv == 1 or op_cad_serv == 2 or op_cad_serv == 3 or op_cad_serv == 4:
                i = 0
                if op_cad_serv == 1:
                    while i < 1:
                    #for i in range(1):
                        print("\n{:*^60}".format(" Cadastro do serviço [PINTURA] "))
                        p.codigo = int(input("\nDigite o código do serviço: "))
                        p.descricao = input("Digite a descrição do serviço: ")
                        i += 1
                    vet_servico.append(p)

                elif op_cad_serv == 2:
                    for i in range(1):
                        print("\n{:*^60}".format("Cadastro do serviço [JARDINAGEM]"))
                        j.codigo = int(input("\nDigite o código do serviço: "))
                        j.descricao = input("Digite a descrição do serviço: ")
                    vet_servico.append(j)

                elif op_cad_serv == 3:
                    for i in range(1):
                        print("\n{:*^60}".format("Cadastro do serviço [FAXINA]"))
                        f.codigo = int(input("\nDigite o código do serviço: "))
                        f.descricao = input("Digite a descrição do serviço: ")
                    vet_servico.append(f)

                elif op_cad_serv == 4:
                    for i in range(1):
                        print("\n{:*^60}".format("Cadastro do serviço [REFORMA EM GERAL]"))
                        r.codigo = int(input("\nDigite o código do serviço: "))
                        r.descricao = input("Digite a descrição do serviço: ")
                    vet_servico.append(r)
            print("\nProdutos Cadastrados!")
            print(vet_servico)
            return(vet_servico)

                    


                






def main():
    matriz_servico = []
    vetor_servico = []
    Menu(vetor_servico)
main()
