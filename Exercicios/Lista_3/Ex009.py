'''9. (Função com retorno sem parâmetro) Foi realizada uma pesquisa sobre algumas características físicas de cinco habitantes de uma região. Foram coletados os seguintes dados de cada habitante: idade, sexo (M - masculino ou F - feminino), cor dos olhos (A - azuis ou C - castanhos), cor dos cabelos (L - louros, P - pretos ou C - castanhos).
Faça uma função/método que leia esses dados, armazenando-os em vetores (listas);
Faça uma função/método que determine e devolva a função principal a média de idades das pessoas com olhos castanhos e cabelos pretos;
Faça uma função/método que determine e devolva a função principal a maior idade entre os habitantes;
Faça uma função/método que determine e devolva a função principal a quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos(inclusive) e que tenham olhos azuis e cabelos louros.'''

# Declarar os vetores antes de qualquer programação, indica que 
# que estas variáveis serão globais a todo o restante do programa 
# e das funções 
idade = []
sexo = []
olho = []
cabelo = []

def cadastrar(): #tópico 1 do exercicio
  for i in range(5): # o i é sempre o numero que vai passar, o seja, entre 1 e 3, vão passar os números 1 e 2 
    idade.append(int(input('Digite a idade em anos: ')))
    sexo.append(input('Digite o sexo M - (masculino) F - (feminino): '))
    olho.append(input('Digite a cor dos olhos A - (azuis) ou C - (castanhos): '))
    cabelo.append(input('Digite a dos cabelos L - (louros), P - (pretos) ou C - (castanhos) : '))

def mediaidades(): # tópico 2 do exercicio
  media_idade = 0
  cont = 0
  soma_idade = 0
  for i in range(5):
    if olho[i] == 'C' or olho[i] == 'c' and cabelo[i] == 'P' or cabelo[i] == 'p':
      soma_idade = soma_idade + idade[i] #idade esta dentro do vetor na posição i
      cont = cont + 1
  media_idade = soma_idade / cont
  return media_idade

def maior_menor_idade(): #3 tópico do exercicio
  maior_idade = 1
  for i in range(5): # vou encontrar a quantidade de pessoas que têm no vetor idade
    if idade[i] >= maior_idade:
      maior_idade = idade[i]
  return maior_idade

def fem(): # 4 tópico do exercicio
  contador = 0
  for i in range(5):
    if sexo[i] == 'F' or sexo[i] == 'f' and idade[i] >= 18 and idade[i] <= 35 and olho[i] == 'A' or olho[i] == 'a' and cabelo[i] == 'L' or cabelo[i] == 'l':
      contador = contador + 1
  return contador

def main():
  cadastrar()
  print(f'A média das idades das pessoas com cabelo pretos e olhos castanhos é:' ,mediaidades())
  print('A maior das idades digitadas é:' ,maior_menor_idade())
  print('A quantidade de pessoas do sexo feminino, com idades entre 18 e 35 e com cabelo Loiro é:' ,fem())
main()