'''7. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Função para construir um menu de opções para uma calculadora:
*** Minha Calculadora ***
Digite um número.....: 
Digite outro número..: 
    + Soma dois números
    - Subtrai dois números
    * Multiplica dois números
    / Divide dois números
Qual opção deseja? 

b) Desenvolva uma função para cada opção de cálculo, mas estas não terão retorno.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.

A função da construção do menu, chamará todas as outras passando a elas os valores digitados.'''

def somar(som,s):
  soma = som + s
  print('A soma entre os números {} e {} é {}'.format(som,s,soma))

def subtrair(sub,subtr):
  subtracao = sub - subtr
  print('A subtração dos números {} e {} é {}'.format(sub,subtr,subtracao))

def vezes(multip,multiplicar):
  multiplicacao = multip * multiplicar
  print('A multiplicação dos números {} e {} é {}'.format(multip,multiplicar,multiplicacao))

def dividir(divis,div):
  divisao = divis / div
  print('A divisão entre os números {} e {} é {}'.format(divis,div,divisao))
 
def main():
  print('----------------------------------------- **** MINHA CALCULADORA **** -----------------------------------------')
  print('\nSelecione uma opção: \n')
  print('+ somar dois números \n- Subtrair dois números \n* Multiplicar dois números \n/ Dividir dois números \n')
  menu = input() 
  n1 = int(input('Digite um número inteiro.......: '))
  n2 = int(input('Digite outro número inteiro....: '))
  while menu == '+' or menu == '-' or menu == '*' or menu == '/':
    if menu == '+':
      somar(n1,n2)
      break

    if menu == '-':
      subtrair(n1,n2)
      break
    
    if menu == '*':
      vezes(n1,n2) 
      break
    
    if menu == '/':
      dividir(n1,n2)
      break  
main()