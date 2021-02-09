import csv
import timeit

def tempoDuracao():
  inicio = timeit.default_timer()
  numeroLinha('c:/Users/matheus.avelar/Desktop/dadosEnem.txt')
  lerPrimeiraLinha('c:/Users/matheus.avelar/Desktop/dadosEnem.txt')
  fim = timeit.default_timer()
  print ('Tempo de execução: %f' % (fim - inicio))

def numeroLinha(arquivo):
  from pathlib import Path

  caminho = Path('./',arquivo)

  if caminho.is_file():
    print('Arquivo existe!')
    with open(caminho, 'r') as f:
      n_linhas = len(f.readlines())
    print('Esse arquivo tem {} linhas.'.format(n_linhas))
  else:
    print('Arquivo inexistente :(')
    
def lerPrimeiraLinha(arquivo):
  print('Primeira linha:')
  archive = open(arquivo, 'r')
  print(archive.readlines()[1])
  archive.close

tempoDuracao()