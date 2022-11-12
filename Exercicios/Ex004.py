'''4. (Função sem retorno sem parâmetro) Faça uma função/método que leia um único valor representado em segundos, converta-o e apresente o resultado em horas, minutos e segundos.'''

def apresentacao():
  segundos = int(input('Digite os segundos: '))
  horas = segundos / 3600
  resto = segundos % 3600
  minutos = resto / 60
  segundos = minutos / 60
  print(f'Os segundos digitados representam: {int(horas)} horas, {int(minutos)} minutos e {int(segundos)} segundos')
def main():
  apresentacao()
main()