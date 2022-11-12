'''2. (Função sem retorno sem parâmetro) Faça uma função/método que leia dois valores positivos e apresente a soma dos N números existentes entre eles (inclusive).'''

def numero():
  n1 = float(input('Digite um número positivo: '))
  n2 = float(input('Digite um número positivo: '))
  soma = 0
  if n1 >= 0 and n2 >= 0:
    if n1 > n2:
      while n1 > n2:
        soma += n2
        n2 += 1
      soma += n1
    elif n2 > n1:
      while n2 > n1:
        soma += n1
        n1 += 1
      soma += n2
    elif n1 == n2:
      soma = n1 + n2      
    print('A soma dos números digitados é:',soma)
  else:
    print('Todos os números precisam ser maiores que 0 (zero)')
def main():
  numero()
main()  