import numpy as np
from termcolor import colored

background = ''

chessBoardState = np.array([
  [8, 9,10,11,12,10, 9, 8],
  [7, 7, 7, 7, 7, 7, 7, 7],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [2, 3, 4, 5, 6, 4, 3, 2]])

redPieceDict = {
  1: '  P  ',
  2: '  R  ',
  3: '  N  ',
  4: '  B  ',
  5: '  Q  ',
  6: '  K  '
  
}

cyanPieceDict = {
  7: '  P  ',
  8: '  R  ',
  9: '  N  ',
  10:'  B  ',
  11:'  Q  ',
  12:'  K  '
}

numToCoord = {
  0: 'a',
  1: 'b',
  2: 'c',
  3: 'd',
  4: 'e',
  5: 'f',
  6: 'g',
  7: 'h'
}

def getArray():
  return chessBoardState

def printBoard():
  emptySpace = "     "
  pointerX = 0
  pointerY = 0
  chessBoardStr = emptySpace * 5 + '\n'

  print('entered function')
  for x in range(64):
    
    pieceNumber = chessBoardState[pointerY, pointerX]

    if pointerY % 2 == 0:
      if pointerX % 2 == 1:
        if pieceNumber <= 6:
          pieceValue = redPieceDict.get(pieceNumber, '     ')
          pieceValue = colored(pieceValue, 'red', 'on_green')
        else:
          pieceValue = cyanPieceDict.get(pieceNumber, '     ')
          pieceValue = colored(pieceValue, 'cyan', 'on_green')
      else:
        if pieceNumber <= 6:
          pieceValue = redPieceDict.get(pieceNumber, '     ')
          pieceValue = colored(pieceValue, 'red', 'on_white')
        else:
          pieceValue = cyanPieceDict.get(pieceNumber, '     ')
          pieceValue = colored(pieceValue, 'cyan', 'on_white')
    else:
      if pointerX % 2 == 0:
        if pieceNumber <= 6:
          pieceValue = redPieceDict.get(pieceNumber, '     ')
          pieceValue = colored(pieceValue, 'red', 'on_green')
        else:
          pieceValue = cyanPieceDict.get(pieceNumber, '     ')
          pieceValue = colored(pieceValue, 'cyan', 'on_green')
      else:
        if pieceNumber <= 6:
          pieceValue = redPieceDict.get(pieceNumber, '     ')
          pieceValue = colored(pieceValue, 'red', 'on_white')
        else:
          pieceValue = cyanPieceDict.get(pieceNumber, '     ')
          pieceValue = colored(pieceValue, 'cyan', 'on_white')
    chessBoardStr = chessBoardStr + pieceValue


        #if we have reached the end of the line then we should move to the next line
          
    if pointerX == 7:
      pointerX = 0
      pointerY += 1
      chessBoardStr = chessBoardStr + '\n'
          
        #else increment the x position counter
    else:
      pointerX += 1

  print(chessBoardStr)

def redPiecesLogic():
  locX = int(input('Please input the X coordinate of the piece you would like to move.'))
  locY = int(input('Please input the Y coordinate of the piece you would like to move.'))
  destX = int(input('Please input the X coordinate of the destination.'))
  destY = int(input('Please input the Y coordinate of the destination.'))

  if chessBoardState[locY, locX] == 1:
    pawnLogic(locX, locY, destX, destY, 1)

    #the redPieceDict check is to see whether the destination
    #has a friendly piece on it
  elif chessBoardState[locY, locX] == 3 and redPieceDict.get(chessBoardState[destY, destX], True) == True:
    knightLogic(locX, locY, destX, destY, 3)

  elif chessBoardState[locY, locX] == 2 and redPieceDict.get(chessBoardState[destY, destX], True) == True:
    rookLogic(locX, locY, destX, destY, 2)
    
  elif chessBoardState[locY, locX] == 4 and redPieceDict.get(chessBoardState[destY, destX], True) == True:
    bishopLogic(locX, locY, destX, destY, 4)

  elif chessBoardState[locY, locX] == 6 and redPieceDict.get(chessBoardState[destY, destX], True) == True:
    kingLogic(locX, locY, destX, destY, 6)

def cyanPiecesLogic():
  locX = int(input('Please input the X coordinate of the piece you would like to move.'))
  locY = int(input('Please input the Y coordinate of the piece you would like to move.'))
  destX = int(input('Please input the X coordinate of the destination.'))
  destY = int(input('Please input the Y coordinate of the destination.'))

  if chessBoardState[locY, locX] == 7:
    pawnLogic(locX, locY, destX, destY, 7)

    #the cyanPieceDict check is to see whether the destination
    #has a friendly piece on it
    
  elif chessBoardState[locY, locX] == 9 and cyanPieceDict.get(chessBoardState[destY, destX], True) == True:
    knightLogic(locX, locY, destX, destY, 9)

  elif chessBoardState[locY, locX] == 8 and cyanPieceDict.get(chessBoardState[destY, destX], True) == True:
    rookLogic(locX, locY, destX, destY, 8)
    
  elif chessBoardState[locY, locX] == 10 and cyanPieceDict.get(chessBoardState[destY, destX], True) == True:
    bishopLogic(locX, locY, destX, destY, 10)

  elif chessBoardState[locY, locX] == 6 and cyanPieceDict.get(chessBoardState[destY, destX], True) == True:
    kingLogic(locX, locY, destX, destY, 12)

def pawnLogic(locX, locY, destX, destY, pieceNum):
  #move logic for red side pawn
  if pieceNum == 1:
    #first move logic is here, a lot of ifs, making sure that if a pawn is on, of piece number 1 it can move 2 if its on Y 6
    if locY == 6 and destY == 4:
      if locX - destX == 0 and chessBoardState[destY, destX] == 0:
        chessBoardState[locY, locX] = 0
        chessBoardState[destY, destX] = 1
      else:
          print('invalid move location')
      #normal pawn movement
    elif locY - destY == 1 and locX - destX == 0:
      if chessBoardState[destY, destX] == 0:
        chessBoardState[locY, locX] = 0
        chessBoardState[destY, destX] = 1

  else:
    if locY == 1 and destY == 3:
      if locX - destX == 0 and chessBoardState[destY, destX] == 0:
        chessBoardState[locY, locX] = 0
        chessBoardState[destY, destX] = 7

      elif destY - locY == 1 and locX - destX == 0:
        if chessBoardState[destY, destX] == 0:
          chessBoardState[locY, locX] = 0
          chessBoardState[destY, destX] = 7
    

def rookLogic(locX, locY, destX, destY, pieceNum):
    #if the X coordinate doesnt change, i.e. moving up and down
    
  if locX - destX == 0:
    chessBoardState[locY, locX] == 0
    chessBoardState[destY, destX] == 2
    #if the Y coordinate doesnt change, i.e. moving left and right
      
  elif locY - destY == 0:
    chessBoardState[locY, locX] == 0
    chessBoardState[destY, destX] == 2
  else:
    print('invalid move')

def knightLogic(locX, locY, destX, destY, pieceNum):
     # up and right
  if destX - locX == 1 and locY - destY == 2:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    # up and left
  elif locX - destX == 1 and locY - destY == 2:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    # down and right
  if destX - locX == 1 and destY - locY == 2:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    # down and left
  elif locX - destX == 1 and destY - locY == 2:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    # left and up
  elif locX - destX == 2 and locY - destY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    #right and up
  elif destX - locX == 2 and locY - destY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    # left and down
  elif locX - destX == 2 and destY - locY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    #right and down
  elif destX - locX == 2 and destY - locY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum

def bishopLogic(locX, locY, destX, destY, pieceNum):
  #basically if moving to the left?, check to see if there is a friendly
  #piece in the way
  if locX - destX < 0:
    for x in range(8 - locX):
      pointerX = x + locX
      pointerY = pointerX
      #easy way to see if there is a piece, if the dict returns
      #null value, theres no piece
      if redPieceDict.get(chessBoardState[pointerY, pointerX], True) == True:
        possibleMove = True
      else:
        possibleMove = False
        break
  else:
    #same deal, just the opposite direction
    for x in range(locX):
      pointerX = locX - x
      pointerY = pointerX
      if redPieceDict.get(chessBoardState[pointerY, pointerX], True) == True:
        possibleMove = True
      else:
        possibleMove = False
        break
        
  #move piece if checks completed successfully
  if possibleMove == True:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum

  else:
    print('error')

def queenLogic(locX, locY, destX, destY, pieceNum):
  pass

def kingLogic(locX, locY, destX, destY, pieceNum):

  #moves down
  if locX - destX == 0 and destY - locY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum

  #moves up
  elif locX - destX == 0 and locY - destY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum

  #moves right
  elif locY - destY == 0 and destX - locX == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum

  #moves left
  elif locY - destY == 0 and locX - destX == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum

  #stole the knight logic and tweaked the values lmao
  elif destX - locX == 1 and locY - destY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    # up and left
  elif locX - destX == 1 and locY - destY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    # down and right
  if destX - locX == 1 and destY - locY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    # down and left
  elif locX - destX == 1 and destY - locY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    # left and up
  elif locX - destX == 1 and locY - destY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    #right and up
  elif destX - locX == 1 and locY - destY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    # left and down
  elif locX - destX == 1 and destY - locY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum
    #right and down
  elif destX - locX == 1 and destY - locY == 1:
    chessBoardState[locY, locX] = 0
    chessBoardState[destY, destX] = pieceNum