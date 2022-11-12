'''1. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método que leia um número e o multiplique por 2, apresente o resultado. Este é um exemplo de PASSAGEM DE PARÂMETRO POR VALOR.'''

def multiplicar(num):# a variável num é nomeada como parâmetro na DEFINIÇÃO
# DA FUNÇÃO, ocorre num = numero, implicitamente, ou seja, o valor de numero é
# COPIADO/ATRIBUÍDO na num, isto é chamado de passagem de parâmetro por valor
    r = num * 2
    print('O resultado da multiplicação é',r)

def main():
    numero = int(input('Digite um número: '))
    multiplicar(numero) # a variável numero nomeada como argumento NA CHAMADA DA FUNÇÃO
main()  