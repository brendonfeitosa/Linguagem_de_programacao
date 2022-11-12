'''8. (Função sem retorno sem parâmetro) Faça uma função/método que leia uma hora de início e de término de um jogo, ambas divididas em dois valores distintos: hora e minuto. Deverá ser apresentado a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.'''

def duracao():
  hora_inicio = float(input('Digite a hora de início do jogo: '))
  minuto_inicio = float(input('Digite os minutos do início do jogo: '))
  hora_fim = float(input('Digite a hora do término do jogo: '))
  minuto_fim = float(input('Digite os minutos do fim do jogo: '))

  if minuto_fim < minuto_inicio:
    minuto_fim = minuto_fim + 60
    hora_fim = hora_fim - 1

  if hora_fim < hora_inicio:
    hora_fim = hora_fim + 24

  total_minutos = minuto_fim - minuto_inicio
  total_horas = hora_fim - hora_inicio
  total_horas_minutos = (total_horas * 60) + total_minutos

  print(f'Este jogo terá uma duração de {total_horas_minutos:.0f} minutos')

def main():
  duracao()
main()