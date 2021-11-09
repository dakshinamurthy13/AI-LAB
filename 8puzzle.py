def draw_board(board):
    print("|----|----|----|")
    print("|    |    |    |")
    print("|  "+board[0]+" | "+board[1]+"  | "+board[2]+"  |")
    print("|    |    |    |")
    print("|----|----|----|")
    print("|    |    |    |")
    print("|  "+board[3]+" | "+board[4]+"  | "+board[5]+"  |")
    print("|    |    |    |")
    print("|----|----|----|")
    print("|    |    |    |")
    print("|  "+board[6]+" | "+board[7]+"  | "+board[8]+"  |")
    print("|    |    |    |")
    print("|----|----|----|")

def dup_board(board):
  dup=[]
  for b in board:
    dup.append(b)
  return dup

def move_number(b,pos):
  board=dup_board(b)
  i=board.index("0")
  temp=board[pos]
  board[i]=temp
  board[pos]="0"
  return board

def move
src=["0","1","2","3","4","5","6","7","8"]
draw_board(src)
  
