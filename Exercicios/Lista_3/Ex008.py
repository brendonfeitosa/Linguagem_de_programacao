'''8. (Função com retorno sem parâmetro) Faça uma função/método retorne um vetor com os três primeiros números perfeitos. Sabe-se que um número é perfeito quando é igual a soma de seus divisores (exceto ele mesmo).
Exemplo: os divisores de 6 são 1, 2 e 3, e 1 + 2 + 3 = 6, logo 6 é perfeito. Não use função pronta.

1º número perfeito: 6

2º número perfeito: 28

3º número perfeito: 496'''

# número 1 não é perfeito
# ...
# número 4 não é perfeito, exemplo: 4 % 1 == 0, 4 % 2 == 0, 4 % 3 != 0, a soma 
# resulta em 2
# ...
# número 6 é perfeito  6 % 1 == 0, 6 % 2 == 0, 6 % 3 == 0, 6 % 4 != 0, 6 % 5 != 0
# quando é perfeito a soma de seus divisores da o mesmo valor de número que é 6

def numero_perfeito():
  vet = []
  for n in range (1, 10000): # n é o intervalo de 1 à 497
    soma = 0
    for j in range(1,n):
      if n % j == 0:
        soma = soma + j # j neste caso é o número que esta dentro da chave na divisão
    if n == soma:
      vet.append(soma)
  print(vet)

def main():
  numero_perfeito()
main()