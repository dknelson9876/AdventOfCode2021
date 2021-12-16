import copy

with open('Day4.txt') as f:
    lines = f.readlines()

drawnNums = lines[0].split(',')
for i in range(len(drawnNums)):
    drawnNums[i] = int(drawnNums[i])
boardCount = (len(lines)-2) // 6
# initialize a list of boards such that they can be accessed [board][row][column]
boards = [[[0 for k in range(5)] for j in range(5)] for i in range(boardCount+1)]

# Load boards
i = 2
board = 0
while i < len(lines)-1:
    temp = [[0 for x in range(5)] for y in range(5)]
    for y in range(5):
        line = lines[i+y].split()
        for x in range(5):
            temp[y][x] = int(line[x])

    boards[board] = temp

    i += 6
    board += 1

# A parallel list for keeping track of whether a number on a board has been chosen----
boardsPicked = [[[False for k in range(5)] for j in range(5)] for i in range(boardCount+1)]

# initialize winning boards to compare against---------
winTemplate = [[False for y in range(5)] for x in range(5)]
wins = []
for i in range(12):
    wins.append(copy.deepcopy(winTemplate))
# win with a col
# win with a row
# win with a diagonal

# do the first four numbers without checks, since it takes at least 5 draws for someone to win-----
for i in range(4):
    val = drawnNums[i]
    for b, board in enumerate(boards):
        for x, row in enumerate(board):
            for y, num in enumerate(row):
                # print("{}, {}, {}".format(b, x, y))
                if(num == val): 
                    # print("{}, {}, {}".format(b, x, y))
                    boardsPicked[b][x][y] = True
                    break



# continue looping through drawnNums, but checking for a winning board after each draw----
for i in range(4, len(drawnNums)):
    val = drawnNums[i]
    for b, board in enumerate(boards):
        for x, row in enumerate(board):
            for y, num in enumerate(row):
                # print("{}, {}, {}".format(b, x, y))
                if(num == val): 
                    # print("{}, {}, {}".format(b, x, y))
                    boardsPicked[b][x][y] = True
                    break
# check if any boards are now a winning board





