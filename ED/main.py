from lista import *
from random import randint
from jogo import Jogo
from datetime import *

try:
  num_participantes = int(
      input("Quantas pessoas participarão da brincadeira? "))
  if num_participantes <= 0:
    raise ValueError
  num_vencedores = int(input("Quantas pessoas vão vencer o jogo? "))
  if num_vencedores >= num_participantes or num_vencedores < 0:
    raise IndexError

  jogo = Jogo(num_participantes, num_vencedores)
  condicao = int(
      input(
          '''Escolha o formato do qual serão adicionado os dados dos jogadores:
                        
                        1- Manualmente
                        2- Arquivo
                        
                        : '''))
  if condicao == 1:
    jogo.playersManual()

  elif condicao == 2:
    arq = './jogadores/jogadores.txt'
    jogo.playersAut(arq)

  else:
    raise AttributeError
  start = randint(1, num_participantes)
  print(f"valor do start {start}")
  jogo.definirPrimeiro(start)
  jogo.iniciarJogo(start)
  data = datetime.now()
  dataformatada = (f'{data.day}-{data.month}-{data.hour}-{data.minute}')
  arq = open(f'./vencedores/vencedores{dataformatada}.txt', 'a')
  for i in range(len(jogo)):
    jogador = jogo.mostrarJogador(i)
    arq.write(f"{jogador} ")

except AttributeError:
  print('opção inválida.')

except ValueError:
  print('O número de participantes precisa ser maior que 0.')

except IndexError:
  print('O número de vencedores precisa ser maior que 0 e menor que o número de participantes.')

except ListException as le:
  print(le)
  
except Exception as e:
  print('Nossos engenheiros vao analisar esse problema')
  print(e.__class__.__name__)
  print(e)
