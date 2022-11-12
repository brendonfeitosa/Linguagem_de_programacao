'''8. (Função sem retorno com parâmetro) Faça uma função/método que calcule a média de um aluno que realizou duas provas (P1 e P2), a partir desta média, chame/crie OUTRA função que verifique se esta média aprova ou reprova o aluno. Aqui deverá ocorrer nas duas funções, PASSAGEM DE PARÂMETRO POR VALOR.'''

def resultado(med):
  if med >= 6 and med <=10:
    print('Aluno aprovado')
  elif med >=0 and med <6:
    print('Aluno reprovado')

def calculo_media(p1 , p2):
  media = (p1 + p2) / 2
  resultado(media)

def main():
  p1 = float(input('Digite a nota da P1: '))
  p2 = float(input('Digite a nota da P2: '))
  calculo_media(p1, p2)
main()