'''9. (Função sem retorno sem parâmetro) Faça uma função/método que leia cinco valores inteiros, determine e mostre o maior e o menor deles. Não pode usar vetor e função pronta da linguagem Python.'''

def maior_menor():
  maior = 0
  menor = 0

  for contador in range(5):
    numero = int(input('Digite um número inteiro: '))
    if contador == 0:
      maior = numero
      menor = numero
    
    else:
      if numero < menor:
        menor = numero
      if numero > maior:
        maior = numero

  print('O maior número é:',maior)
  print('O menor número é:',menor)

def main():
  maior_menor()
main()