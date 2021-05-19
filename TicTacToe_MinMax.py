# -*- coding: utf-8 -*-
import random

# Faz uma cópia do tabuleiro e retorna essa cópia
def copiaTabuleiro(tabuleiro):
  Tabs = []
  for i in tabuleiro:
    Tabs.append(i)
  
  return Tabs

# Imprimir o tabuleiro
def desenhaTabuleiro(tabuleiro):
  copia = copiaTabuleiro(tabuleiro)
  for i in range(1,10):
    if(tabuleiro[i] == ''):
      copia[i] = str(i)
    else:
      copia[i] = tabuleiro[i]
    
  print(' ' + copia[7] + '|' + copia[8] + '|' + copia[9])
  print('-------')
  print(' '+ copia[4] + '|' + copia[5] + '|' + copia[6])
  print('-------')
  print(' '+ copia[1] + '|' + copia[2] + '|' + copia[3])
  print('-------')

# O jogador escolhe a letra  "X" ou "O"
# Retorna uma lista com a letra do jogador e a letra do agente
def escolheLetra():
  letra = ''
  while not (letra == 'X' or letra == 'O'):
    print('Insira a letra desejada X(xis) ou O (oh) ?')
    letra = input('').upper()
    if(letra != 'X' and letra != 'O'):
      print('Entre apenas com a letra X (xis) ou O (oh) !!!')
  if (letra == 'X'):
    return ['X', 'O']
  else:
    return ['O', 'X']

difiMinMax = 0

def escolhaDificuldade():
    dificuldade = -1
    while not (dificuldade == 2 or dificuldade == 5 or dificuldade == 10 ):
        print('Escolha a dificuldade colocando 1 pra facil, 2 pra médio e 3 pra dificil')
        escolha = input('')

        if (escolha == '1'):
            dificuldade = 2
            difiMinMax = 0

        if (escolha == '2'):
            dificuldade = 5
            difiMinMax = 1

        if (escolha == '3'):
            dificuldade = 10
            difiMinMax = 2

    return dificuldade


#Função define que joga primeiro
def jogaPrimeiro():
  if(random.randint(0,1) == 0):
      return 'agente'
  else:
      return 'humano'

# Realiza o movimento no tabuleiro
def fazMovimento(tabuleiro, letra, movimento):
  tabuleiro[movimento] = letra 

# A função retorna se a letra passada vence o jogo
def vencedor(tab, let):
  return((tab[7] == let and tab[8] == let and tab[9] == let) or #linha de cima
		(tab[4] == let and tab[5] == let and tab[6] == let) or #linha do meio
		(tab[1] == let and tab[2] == let and tab[3] == let) or #linha de baixo
		(tab[7] == let and tab[4] == let and tab[1] == let) or #coluna da esquerda
		(tab[8] == let and tab[5] == let and tab[2] == let) or #coluna do meio
		(tab[9] == let and tab[6] == let and tab[3] == let) or #coluna da direito
		(tab[7] == let and tab[5] == let and tab[3] == let) or #diagonal principal
		(tab[9] == let and tab[5] == let and tab[1] == let)) #diagonal secundaria

# Retorna se o movimento escolhido está livre
def espacoLivre(tabuleiro, movimento):
  if(tabuleiro[movimento] == ''):
    return True
  else:
    return False

#Solicita o movimento do jogador humano
def movimentoDoJogador(tabuleiro):
	#Recebe o movimento
	move = ''
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not espacoLivre(tabuleiro, int(move)):
		print('Qual eh o seu proximo movimento? (1-9)')
		move = input();
		if(move not in '1 2 3 4 5 6 7 8 9'):
			print ('MOVIMENTO INVALIDO! INSIRA UM NUMERO ENTRE 1 E 9!')
		
		if(move in '1 2 3 4 5 6 7 8 9'):
			if(not espacoLivre(tabuleiro, int(move))):
				print ('ESPACO INSDISPONIVEL! ESCOLHA OUTRO ESPACO ENTRE 1 E 9 O QUAL O NUMERO ESTA DISPONIVEL NO QUADRO!')

	return int(move)

#Retorna um movimento aleatório
#Retorna None se não possui movimentos válidos
def movimentosAleatorios(tabuleiro, listaMovimentos):
  possiveisMovimentos = []
  for i in listaMovimentos:
    if espacoLivre(tabuleiro, i):
      possiveisMovimentos.append(i)
  
  if len(possiveisMovimentos != 0):
    return random.choice(possiveisMovimentos)
  else:
    return None

#Retorna True se todos os espacos do quadro estão indisponíveis
def tabuleiroCheio(tabuleiro):
  for i in range(1, 10):
    if espacoLivre(tabuleiro, i):
      return False
  return True

#Retorna uma lista com todos os espaços no quadro que estão disponíveis
def possiveisOpcoes(tabuleiro):
  opcoes = []
  for i in range (1,10):
    if espacoLivre(tabuleiro, i):
      opcoes.append(i)
  return opcoes

#Verifica estado terminal
#Retorna -1 se o jogador ganha
#Retorna 1 se o computador ganha
#Retorna 0 se o jogo termina empatado
#Retorna None se o jogo não terminou
def jogoFinalizado(tabuleiro, completra):
  if compLetra == 'X':
    jogadorLetra = 'O'
  else:
    jogadorLetra = 'X'
  if (vencedor(tabuleiro, compLetra)):
    return 1
  elif (vencedor(tabuleiro, jogadorLetra)):
    return -1
  elif (tabuleiroCheio(tabuleiro)):
    return 0
  else:
    return None

#Algoritmo minmax poda alphabeta
def minMaxAlphaBeta(tabuleiro, compLetra, vez, alpha, beta):
  if compLetra == 'X':
    jogadorLetra = 'O'
  else:
    jogadorLetra = 'X'
  
  if vez == compLetra:
    proximaVez = jogadorLetra
  else:
    proximaVez = compLetra
  
  fim = jogoFinalizado(tabuleiro, compLetra)
  if (fim != None):
    return fim
  
  possiveis = possiveisOpcoes(tabuleiro)

  if vez == compLetra:
    for movimento in possiveis:
      fazMovimento(tabuleiro, vez, movimento)
      val = minMaxAlphaBeta(tabuleiro, compLetra, proximaVez, alpha, beta)
      fazMovimento(tabuleiro, '', movimento)
      if val > alpha:
        alpha = val
      if alpha >= beta:
        return alpha
    return alpha
  else:
    for movimento in possiveis:
      fazMovimento(tabuleiro, vez, movimento)
      val = minMaxAlphaBeta(tabuleiro, compLetra, proximaVez, alpha, beta)
      fazMovimento(tabuleiro, '', movimento)
      if val < beta:
        beta = val
      if alpha >= beta:
        return beta
    return beta

#Define o movimento do agente
def pegaMovimentoComp(tabuleiro, vez, compLetra, dificuldade):
  a = -2
  opcoes = []

  if compLetra == 'X':
    jogadorLetra = 'O'
  else:
    jogadorLetra = 'X'
  
  #Começamos com MinMAx
  #Primeiro checamos se podemos ganhar no próximo movimento
  for i in range(1, dificuldade):
    copia = copiaTabuleiro(tabuleiro)
    if espacoLivre(copia, i):
      fazMovimento(copia, compLetra, i)
      if vencedor(copia, compLetra):
        return i
  
  #Checa se o jogador pode vencer no próximo movimento e bloqueia
  for i in range(1, dificuldade):
    copia = copiaTabuleiro(tabuleiro)
    if espacoLivre(copia, i):
      fazMovimento(copia, jogadorLetra, i)
      if vencedor(copia, jogadorLetra):
        return i
  
  possiveisOp = possiveisOpcoes(tabuleiro)

  for movimento in possiveisOp:
    fazMovimento(tabuleiro, compLetra, movimento)
    val = minMaxAlphaBeta(tabuleiro, compLetra, jogadorLetra,  (difiMinMax * -1), difiMinMax)
    fazMovimento(tabuleiro, '', movimento)

    if val > a:
      a = val
      opcoes = [movimento]
    elif val == a:
      opcoes.append(movimento)
    
  return random.choice(opcoes)

print("     Trabalho 2 de IA      ")
print(" Busca Competitiva MinMax  ")
print("      Jogo da Velha        ")
print("Grupo: Lucas Paulo, Ricardo")

jogar = True

while jogar:
  #Reseta o jogo
  tabuleiro = [''] * 10
  jogadorLetra, compLetra = escolheLetra()
  vez = jogaPrimeiro()
  dificuldade = escolhaDificuldade()
  print('O '+vez+' joga primeiro')
  jogoIniciado = True
  while jogoIniciado:
    if vez == 'humano':
      #Vez do humado
      desenhaTabuleiro(tabuleiro)
      movimento = movimentoDoJogador(tabuleiro)
      fazMovimento(tabuleiro, jogadorLetra, movimento)

      if vencedor(tabuleiro, jogadorLetra):
        desenhaTabuleiro(tabuleiro)
        print("Você venceu!!! Parabéns !!!")
        jogoIniciado = False
      else:
        if tabuleiroCheio(tabuleiro):
          desenhaTabuleiro(tabuleiro)
          print("Jogo Empatado!!!")
          break
        else:
          vez = 'agente'
    else:
      #Vez do agente
      #Na função abaixo é definido o movimento do agente
      movimento = pegaMovimentoComp(tabuleiro, vez, compLetra, dificuldade)
      fazMovimento(tabuleiro, compLetra, movimento)

      if vencedor(tabuleiro, compLetra):
        desenhaTabuleiro(tabuleiro)
        print("O agente venceu !!!")
        jogoIniciado = False
      else:
        if tabuleiroCheio(tabuleiro):
          desenhaTabuleiro(tabuleiro)
          print("Jogo Empatado!!!")
          break
        else:
          vez = 'humano'
  novoJogo = ''
  while not(novoJogo == 'S' or novoJogo == 'N'):
    print("Quer jogar novamente, Digite S para sim ou N para não?")
    novoJogo = input().upper()
    if (novoJogo != 'S' and novoJogo != 'N'):
      print("Entrada inválida, Digite S para sim ou N para não")
    if novoJogo == 'N':
      print("Até a próxima")
      jogar = False