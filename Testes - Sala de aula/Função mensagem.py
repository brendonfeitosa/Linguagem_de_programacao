#Definição da Função
def mensagem():
    print('Boa noite!')
    print('Tudo bem?')
    print('Até Logo...')


def calcular_idade():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = 2022 - ano_nascimento
    print("A idade é: ",idade)


def calcular_media():
    p1 = float(input('Cadastre a primeira prova: '))
    p2 = float(input('Cadastre a segunda prova: '))
    media = (p1 + p2) / 2
    print('Sua média é:',media)


def main(): #Esta função, reune a chamada de todas as outras
    #funções que foram desenvolvidas, similar a uma interface principal de um sistema
    #Chamada da Função
    print('Entrei na função main')
    mensagem()#Chamada da Função
    calcular_idade() #chamada da função
    calcular_media()

main() #Chamada da Função Principal


