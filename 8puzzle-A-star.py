import math
board=[[-1,1,0,1],[0,1,0,1],[0,1,0,1],[0,1,0,1],]
def print_board(board):
  for b in board:
    print(b)

def getIndex(board):
    indices = []
    for list in board:
        if -1 in list:
            indices.append(board.index(list))
            indices.append(list.index(-1))
    return indices


def distance(board,target):
  p=getIndex(board)
  d=math.sqrt(math.pow(p  


print(getIndex(board))
  
  
