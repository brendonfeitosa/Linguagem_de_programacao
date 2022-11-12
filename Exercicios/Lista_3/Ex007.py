'''7. (Função com retorno sem parâmetro) Faça uma função/método que leia e armazene 5 elementos inteiros no vetor A, deverá ser gerado um vetor B, de mesmo tamanho, que armazenará o fatorial de cada elemento de A. Não use função pronta de cálculo de fatorial. Retorne/apresente o vetor B.'''

# Exemplo:
# A = [5  ,4 ,3,2,1] este é o número que quero digitar
# B = [120,24,6,2,1] este é o fatorial do numero de cima
a = []
b = []
def fatorial():
  for j in range(5):
    fatorial = 1
    numero = int(input('Digite um número inteiro: '))
    a.append(numero)
    for i in range(numero):
      fatorial = fatorial * (i + 1)
    b.append(fatorial)
  print(a)
  print(b)

def main():
  fatorial()
main()
