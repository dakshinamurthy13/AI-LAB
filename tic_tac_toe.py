board=[" "]*9

def draw_board(board):
    print("|----|----|----|")
    print("|    |    |    |")
    print("|   "+board[0]+"| "+board[1]+"  | "+board[2]+"  |")
    print("|    |    |    |")
    print("|----|----|----|")
    print("|    |    |    |")
    print("|   "+board[3]+"| "+board[4]+"  | "+board[5]+"  |")
    print("|    |    |    |")
    print("|----|----|----|")
    print("|    |    |    |")
    print("|   "+board[6]+"| "+board[7]+"  | "+board[8]+"  |")
    print("|    |    |    |")
    print("|----|----|----|")

def check_win(player_mark,board):
    return(
        (board[0]==board[1]==board[2]==player_mark) or
        (board[3]==board[4]==board[5]==player_mark) or
        (board[6]==board[7]==board[8]==player_mark) or
        (board[0]==board[3]==board[6]==player_mark) or
        (board[1]==board[4]==board[7]==player_mark) or
        (board[2]==board[5]==board[8]==player_mark) or
        (board[0]==board[4]==board[8]==player_mark) or
        (board[6]==board[4]==board[2]==player_mark)
    )


def check_draw(board):
    return " " not in board

def duplicate_board(board):
    dup=[]
    for j in board:
        dup.append(j)
    return dup

def test_win_move(board,player_mark,move):
    bcopy=duplicate_board(board)
    bcopy[move]=player_mark
    return check_win(player_mark,bcopy)

def win_strategy(board):
    #If no place is there to win
    #then it comes here
    #Usually person wins by playing
    #in the corners
    for i in [0,8,2,6]:
        if board[i]==" ":
            return i
    #next best chance is in the middle
    if board[4]== " ":
        return 4
    for i in [1,3,5,7]:
        if board[i]==" ":
            return i

def fork_move(board, player_mark, move):
    #checking ahead in time if that position
    #can cause a fork move
    bcopy=duplicate_board(board)
    bcopy[move]=player_mark
    #If winning moves that is,
    #The player or agent plays in that position
    # 2 places in which he can play to win
    winning_moves=0
    for i in range(0,9):
        if bcopy[i]==" " and test_win_move(bcopy,player_mark,i):
            winning_moves+=1
    return winning_moves>=2

def get_agent_move(board):
    #Return agent move
    #If there exist a move which will make the agent win
    for i in range(0,9):
        if board[i]== " " and test_win_move(board,'X',i):
            return i
    #Return player win move
    #Blocks the player from winning
    for i in range(0,9):
        if board[i]== " " and test_win_move(board,"O",i):
            return i
    #Return position of fork move
    #Agent to try and make a fork move
    for i in range(0,9):
        if board[i]== " " and fork_move(board,"X",i):
            return i
    #Return position of fork move
    #To block the player from making a fork move
    for i in range(0,9):
        if board[i]== " " and fork_move(board,"O",i):
            return i
    #if none of these positions are available
    #then return the best postion to place the agent move
    return win_strategy(board)

def tic_tac_toe():
    Playing=True
    while Playing:
        InGame=True
        board=[" "]*9
        #X is fixed as agent marker
        #O is fixed as player marker
        player_mark="X"
        print("Playing 1st or 2nd??(Enter 1 or 2)")
        pref=input()
        if pref=="1":
            player_mark="O"
        while InGame:
            if player_mark=="O":
                print("Player's turn")
                move=int(input())
                if board[move]!=" ":
                    print("Invalid move")
                    continue
            else:
                move=get_agent_move(board)
            board[move]=player_mark
            if check_win(player_mark,board):
                InGame= False
                draw_board(board)
                if player_mark=="X":
                    print("Agent wins")
                else:
                    print("Player wins")
                continue
            if check_draw(board):
                InGame=False
                draw_board(board)
                print("Its a draw")
                continue
            draw_board(board)
            if player_mark=="O":
                player_mark="X"
            else:
                player_mark="O"
        print("Do you want to continue playing??(Y or N)")
        inp=input()
        if inp!= "Y" or inp!="y":
                Playing=False

tic_tac_toe()
