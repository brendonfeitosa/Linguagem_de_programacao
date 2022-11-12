'''1. (Função sem retorno sem parâmetro) Faça um programa contendo uma função/método que apresente o valor 1 se o número digitado for positivo e 0 se for negativo.'''

def positivo_negativo (): # uso def para iniciar uma função
   numero = float(input('Digite um número: '))
   if numero >= 0: #crio a loógica de programação
    print('1')
   else:
    print('0')

def main(): # usando este comando estou definindo a função positivo_negativo como função principal
  positivo_negativo() # posso chamar a função diretamente, sem definir ela como principal
main() 


#def positivo_negativo (): # uso def para iniciar uma função
#   numero = float(input('Digite um número: '))
#   if numero >= 0: #crio a loógica de programação
#    print('1')
#   else:
#    print('0')

#def cumprimentar():
#  print('Bom dia')

#def main(): # usando este comando estou definindo a função positivo_negativo como função principal
#  cumprimentar()
#  positivo_negativo() # posso chamar a função diretamente, sem definir ela como principal
#main()
