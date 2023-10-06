from lista import LinkedList
from pilha import *
from random import randint
from time import sleep

class Jogo:
  """ 
    A classe jogo, inicia o jogo circuito bomba. 
  """
  
  def __init__(self, quantity: int, winners: int):

    """ 
    def __ini__ é o método construtor do jogo, ele necessita da quantidade de jogadores, o número de vencedores e a identificação de seus respectivos nomes e posições que serão inseridos na lista.
    """

    self.__quantity = quantity
    self.__winners = winners
    self.__players = LinkedList()
    self.__eliminados = Pilha()

  def playersAut(self, arq):

    """ 
    def playersAut, este método define os player automaticamente a partir de um arquivo de texto com os nomes dos jogadores. 
    """

    arqOpen = open(arq, 'r')
    string_jogadores = arqOpen.readlines()
    string_jogadores = string_jogadores[0]
    print(string_jogadores)
    arr_jogadores = string_jogadores.split(', ')
    for i in range(self.__quantity):
      player = arr_jogadores[i].title()
      if self.__players.isEmpty() == False:
        self.__players.verifyElement(player)
      self.__players.insert(player, 1)


  def playersManual(self):

    """ 
    def playersManual é o método usado para definir os jogadores manualmente, usando seu nome e posição. 
    """

    for i in range(self.__quantity):
      player = input("Nome do jogador: ").title()
      if self.__players.isEmpty() == False:
        self.__players.verifyElement(player)
      position = int(input("Posição do jogador: "))
      self.__players.insert(player, position)


  def passarJogador(self, quantity):

    """ 
    def passarJogador é o método usado para definir os jogadores manualmente, usando seu nome e posição. 
    """

    for i in range(quantity):
      print(self.__players.advance())
      sleep(1)

  def definirPrimeiro(self, quantity):

    """
    Esse método recebe a quantidade de vezes que deve percorre a lista pela função advance() até o jogador que foi escolhido pelo "randint start" na função iniciarJogo() para ser o primeiro a jogar. 
    """

    if quantity == 1:
      return
    for i in range(quantity-1):
      self.__players.advance()

  def selecionarJogador(self, start, quantity):

    """ 
    Este método, denominado selecionarJogador, é utilizado para determinar qual jogador será eliminado com base na lógica do jogo. Essa seleção é influenciada pelo valor gerado aleatoriamente denominado "music" (música) no método iniciarJogo().

    O método selecionarJogador recebe dois argumentos:

    start: Este argumento representa a posição inicial a partir da qual o ponteiro começará a avançar.

    quantity: Este argumento indica quantas vezes o ponteiro avançará na lista de jogadores.

    O objetivo é mover o ponteiro através da lista de jogadores, começando na posição especificada por start, avançando quantity vezes e, ao final desses avanços, identificar qual jogador será eliminado.

    A função retorna a posição do jogador que está prestes a ser eliminado.  
    """
    eliminado = self.__players.goTo(start, quantity)
    posicaoEliminado = self.__players.index(eliminado) + 1
    return posicaoEliminado

  def eliminarJogador(self, position):

    """
    Esse método recebe a posição do jogador que será eliminado e remove ele da lista, além de adicionar o jogador eliminado a uma pilha que irá aparecer durante cada rodada. 
    """

    removido = self.__players.remove(position)
    self.__eliminados.empilha(removido)
    return removido

  def mostrarJogador(self, quantity):

    """ 
    Essa função recebe a posição do jogador é mostra o self.__data dele, ou seja o nome do jogador.
    """

    jogador = self.__players.element(quantity)
    return jogador

  def posicaoJogador(self, elemen):

    """
      Esse método recebe o nome do jogador e retorna a sua posição na lista.
    """
    posicao = self.__players.index(elemen) + 1
    return posicao

  def __str__(self) -> str:

    """ 
    Metódo para mostrar os jogadores.
    """
    str = '[ '
    for i in range(len(self.__players)):
      str += f'{self.__players.element(i)}, '
    str = str[:-2] + " ]"
    return str

  def __len__(self):

    """
    Método para mostrar os jogadores
    """
    return len(self.__players)


  def iniciarJogo(self, start: int):

    """
     Método que inicia o jogo, recebendo o start do main, faz a interface do jogo chama as funções e conta os rounds.
    """

    round = 1
    while self.__winners < len(self):
      music = randint(4, 15)
      print("--------------------COMEÇO DO ROUND------------------")
      print(f"participantes: {self}")
      print(f"Rodada: {round}")
      print(f"Start: {self.mostrarJogador(start-1)} K={music}")
      for i in range(music):
        proximoEliminado = self.__players.advance()
        print(proximoEliminado)
        sleep(1)
      eliminado = self.posicaoJogador(proximoEliminado) - 1
      start = eliminado
      print(f"Jogador eliminado: {self.eliminarJogador(eliminado)}")
      print(f'Pilha com os eliminados: {self.__eliminados}')
      print("--------------------FIM DO ROUND------------------")
      print()
      round += 1
      sleep(2)
    print()
    print(f"O(s) participante(s) vencedor(es): {self}")
    print(f'Pilha com os eliminados: {self.__eliminados}')
