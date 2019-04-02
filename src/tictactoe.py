''' Different ways to get indices from a list
l = [1, 2, 3, 4, 5, 6, 7]
print(l[1])
print(l[-1])
print(l[1:])
print(l[1:2])
'''

#can change value of object but not object itself
'''x = [1,2,3]
print(id(x))

def tictactoeboard():
    #x = "A game"
    x[1]=95
    print(id(x))
    print(x)
tictactoeboard()
print(x)
print(id(x))
'''

#global word allows us to change the stuff inside the game variable
'''game = "I want to play a game"
print(id(game))

def game_board():
    global game
    game = "A game"
    print(id(game))
    print(game)

game_board()
print(game)
print(id(game))
'''

''' Mini Quiz to understand Mutability
x = 1
def test():
    x = 2
test()
print(x)#1


x = 1
def test():
    global x
    x = 2
test()
print(x)#2


x = [1]
def test():
    x = [2]
test()
print(x)#[1]


x = [1]
def test():
    global x
    x = [2]
test()
print(x)#[2]


x = [1]
def test():
    x[0] = 2
test()
print(x)#[2]
'''

x = [[1, 2, 1],
     [0, 1, 2],
     [0, 2, 1]]



def tictactoeboard(game_map, player, row, column, display=False):
    try:
        print("   0  1  2")

        if not display:
            game_map[row][column] = player
        for count,row in enumerate(game_map):
            print(count,row)
        return game_map
    except IndexError as e:
        print("Error: Make sure you input row/column as 0,1, or 2", e)

    except Exception as e:
        print("Something went very wrong!", e)

def horizontalwin (current_game):
    for row in x:
        print(row)
        if row.count(row[0]) == len(row) and row[0] !=0:
            print("Winner")


def verticalwin (current_game):
    for col in range(len(x)):
        #print(col)
        check = []
        for row in x:
            check.append(row[col])
            #print(check)
        if check.count(check[0]) == len(check) and check[0] != 0:
            print("Winner")

def diagonalwin(current_game):
    diagonals = []
    cols = reversed(range(len(x)))
    rows = range(len(x))

    for indexOfX in range(len(x)):
        diagonals.append(x[indexOfX][indexOfX])
    if diagonals.count(diagonals[0]) == len(diagonals) and diagonals[0] != 0:
        print("Winner")
    for col,row in zip(cols,rows):
        diagonals.append(x[row][col])



diagonalwin(x)










'''
x = range(3)
y = [2,1,0]

zip(x,y)

z = [5,6,7]

for i in zip(x,y,z):
    print(i)
'''










'''
l = [[0,1],
     [2,3],
     [3,4]]
def messaround(list):
    #len(list) <- for l it contains 3 lists so the size is 3 not 2 
    for column in range(len(list)):
        print (column)
        new = []
        for row in list:
            new.append(row[column])
            # index becomes out of range but it the new list is vertical elements
            print(new)
            
messaround(l)
'''