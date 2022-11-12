'''4. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba duas notas (P1, P2) calcule a média, chame outra função na main que avalie se este aluno esta aprovado ou reprovado retornando a str/string 'Aprovado' ou 'Reprovado'.'''

def media(cal_media):
  if cal_media >= 6:
    print('Aprovado')
  elif cal_media < 6:
    print('Reprovado')

def main():
  p1 = float(input('Digite a nota da P1: '))
  p2 = float(input('Digite a nota da P2: '))
  resultado_media = (p1 + p2) / 2
  media(resultado_media)
main()
