'''8. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Função para construir um menu de opções para uma calculadora:

*** Minha Calculadora ***
Digite um número.....: 
Digite outro número..: 
    + Soma dois números
    - Subtrai dois números
    * Multiplica dois números
    / Divide dois números
Qual opção deseja? 

b) Desenvolva uma função para cada opção de cálculo, que deverá ter retorno.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.

A função de desenho/construção do menu, chamará todas as outras passando a elas os valores digitados.'''

def soma(r,num):
    somar = r + num
    return somar

def subtrai(r,num):
    subtracao = r - num
    return subtracao

def multiplica(r,num):
    multiplicacao = r * num
    return multiplicacao

def divide(r,num):
    divisao = r / num
    return divisao

def menu():
    print('\n** Minha Calculadora ** \n+ Soma dois números \n- Subtrai dois números \n* Multiplica dois números \n/ Divide dois números\n')

def main():
  menu()
  opcao = (input('Qual é a opção desejada?: '))
  while opcao == '+' or opcao == '-' or opcao == '*' or opcao == '/':
    if opcao == '+':
      n1 = int(input('Digite um número inteiro: '))
      n2 = int(input('Digite outro número inteiro: '))
      print('\nA soma é: ',soma(n1,n2))

    if opcao == '-':
      n1 = int(input('Digite um número inteiro: '))
      n2 = int(input('Digite outro número inteiro: '))
      print('\nA subtração é: ',subtrai(n1,n2))

    if opcao == '*':
      n1 = int(input('Digite um número inteiro: '))
      n2 = int(input('Digite outro número inteiro: '))
      print('\nA multiplicação é: ',multiplica(n1,n2))

    if opcao == '/':
      n1 = int(input('Digite um número inteiro: '))
      n2 = int(input('Digite outro número inteiro: '))
      print('\nA divisão é: ',divide(n1,n2))

    print('\n** Minha Calculadora ** \n + Soma dois números \n - Subtrai dois números \n * Multiplica dois números \n / Divide dois números\n')
    opcao = (input('\nQual é a opção desejada?: '))
main()
