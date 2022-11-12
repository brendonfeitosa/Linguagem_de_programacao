'''4. Baixe o arquivo futebol.txt que esta na pasta Material do aula do Teams. Leia este arquivo e o apresente. Com os dados lidos, armazene na estrutura Futebol (posicao_jogo, altura, peso, imc), calcule o IMC (Índice de Massa Corporal), armazene na estrutura e também em outro arquivo, mas agora chamado futebol_imc.txt. Apresente este novo arquivo.
Observação: esse exercício deve ser testado fora do Colab, no Idle ou qualquer outra IDE, porque usará um arquivo que estará na pasta material de aula do Teams.'''

# imc = peso / (altura ** 2)
class TipoJogador:
    posicao_jogo = ''
    altura = 0.0
    peso = 0.0
    imc = 0.0

def visualizar_futebol():
    vetor = []
    arquivo = open('futebol.txt','r')
    print('\n{:-^50}'.format(' Jogadores Cadastrados '))
    print('\nPosição \tAltura \tPeso')
    for linha in arquivo.readlines():
        pos, alt, pes = linha.strip().split(',')
        print(pos,'\t',alt,'\t',pes)
        f = TipoJogador()
        f.posicao_jogo = pos
        f.altura = alt
        f.peso = pes
        f.imc = f'{float(pes) / (float(alt) ** 2):.2f}'
        vetor.append(f)
    arquivo.close()
    return vetor

def gravar_futebol_imc(vet_fut_imc):
    if len(vet_fut_imc) > 0:
        arquivo_imc = open('futebol_imc.txt','w')
        for i in range(len(vet_fut_imc)):
            pos = vet_fut_imc[i].posicao_jogo
            alt = vet_fut_imc[i].altura
            peso1 = vet_fut_imc[i].peso
            imc1 = vet_fut_imc[i].imc
            arquivo_imc.write(f'{pos},{alt},{peso1},{imc1}\n')
        arquivo_imc.close()

def visualizar_fut_imc():
    arquivo_imc = open('futebol_imc.txt','r')
    print('\n{:-^50}'.format(' Jogadores Cadastrados com IMC '))
    print('\nPosição \tAltura \tPeso \tIMC')
    for linha in arquivo_imc.readlines():
        pos, alt, pes, imc = linha.strip().split(',')
        print(pos,'\t',alt,'\t',pes,'\t',imc)
    arquivo_imc.close()

def main():
    vet = visualizar_futebol()
    gravar_futebol_imc(vet)
    visualizar_fut_imc()
main()