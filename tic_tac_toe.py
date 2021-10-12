import random
board=[" "]*9
already_placed=[]

def draw_board3():
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

draw_board3()
print("")
print("")
list1 = [1,2,3,4,5,6,7,8,9]
for b in range(len(board)):
    selectedN=random.choice(list1)
    list1.remove(selectedN)
    board[b]=str(selectedN)

for b in range(len(board)):
    p=input("Enter the index of position  ")
    while p not in already_placed:
        p=input("Enter the valid of position  ")
    board[b]=str(p)
    draw_board()
draw_board3()
