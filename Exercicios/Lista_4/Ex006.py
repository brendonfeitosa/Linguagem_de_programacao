'''6. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Função para construir um menu de opções para uma calculadora, como neste exemplo: 
Menu de cálculos
1.   Número ao quadrado
2.   Número ao cubo
3.   Raiz do número
4.   Raiz cúbica do número
Qual é a opção desejada?

b) Desenvolva uma função para cada opção de cálculo.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos números do menu.

A função da construção do menu, chamará todas as outras passando a elas o valor digitado.'''

def quadrado(q):
  quadr = q ** 2
  print('O quadrado do número {} é {}'.format(q,quadr))

def cubo(c):
  cub = c ** 3
  print('O cubo do número {} é {}'.format(c,cub))

def raizquad(r):
  raiz = r ** (1/2)
  print('A raiz quadrada do número {} é {}'.format(r,raiz))

def raizcubica(rc):
  raiz_cub = rc ** (1/3)
  print('A raiz cúbica do número {} é {}'.format(rc,raiz_cub))

def main():
  print('Menu de cálculos: \n\n1. Número ao quadrado \n2. Número ao cubo \n3. Raiz do número \n4. Raiz cúbica do número \n\nQual a opção desejada?')
  print()
  menu = int(input())
  print()
  while menu == 1 or menu == 2 or menu == 3 or menu == 4:
    if menu == 1:
      numero = float(input('Digite um número: '))
      print()
      quadrado(numero)
    if menu == 2:
      numero = float(input('Digite um número: '))
      print()
      cubo(numero)
    if menu == 3:
      numero = float(input('Digite um número: '))
      print()
      raizquad(numero)
    if menu == 4:
      numero = float(input('Digite um número: '))
      print()
      raizcubica(numero)
    else:
      break
main()
