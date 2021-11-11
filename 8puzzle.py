def draw_board(board, label):
    print(label)
    print()
    for list in board:
        print(list)


def dup_board(board):
    dup = []
    for b in board:
        dup.append(b)
    return dup


def move_number(board, positionTo,postionFrom):
    dup = dup_board(board)
    temp=dup[positionTo[0]][positionTo[1]]
    dup[positionTo[0]][positionTo[1]]=dup[postionFrom[0]][postionFrom[1]]
    dup[postionFrom[0]][postionFrom[1]]=temp
    return dup


def getIndex(board, num):
    indices = []
    for list in board:
        if num in list:
            indices.append(board.index(list))
            indices.append(list.index(num))
    return indices


# print(getIndex(board, 8))

def getManhattanDistance(board, target, num):
    indexOfNum1 = getIndex(board, num)
    indexOfNum2 = getIndex(target, num)
    d = abs(indexOfNum1[0]-indexOfNum2[0])+abs(indexOfNum1[1]-indexOfNum2[1])
    return d


def getTotalManhattanDistance(board, target):
    total = 0
    for i in range(1, 9):
        total += getManhattanDistance(board, target, i)
    return total


def getPossibleMoves(board):
    moves = ["up", "down", "right", "left"]
    emptySpaceIndex = getIndex(board, 0)
    # print(emptySpaceIndex)
    # If 0 is in the the first row
    if emptySpaceIndex[0] == 0:
        moves.remove("up")
    # If 0 is in the the last row
    if emptySpaceIndex[0] == 2:
        moves.remove("down")
    # If 0 is in the the first column
    if emptySpaceIndex[1] == 0:
        moves.remove("left")
    # If 0 is in the the last column
    if emptySpaceIndex[1] == 2:
        moves.remove("right")
    return moves

board = [[1, 2, 3], [4, 0, 6], [7, 8, 5]]
target = [[5, 3, 6], [1, 2, 4], [7, 8, 0]]


draw_board(board, "Source")
draw_board(target, "Target")
# print(getManhattanDistance(board, target, 5))
print(getTotalManhattanDistance(board, target))
print(getPossibleMoves(board))
print(move_number(board,[0,0],[1,0]))