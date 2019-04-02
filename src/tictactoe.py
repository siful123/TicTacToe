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
import itertools

def tictactoeboard(game_map, player=1, row=0, column=0, display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is currently occupied!")
            return game_map, False
        print("   0  1  2")

        if not display:
            game_map[row][column] = player
        for count,row in enumerate(game_map):
            print(count,row)
        return game_map, True
    except IndexError as e:
        print("Error: Make sure you input row/column as 0,1, or 2", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False


def win (current_game):


    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False


    #Horizontal winner
    for row in x:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} has gotten three in a row!")
            return True


    #Vertical Winner
    for col in range(len(x)):
        #print(col)
        check = []
        for row in x:
            check.append(row[col])
            #print(check)
        if all_same(check):
            print(f"Player {check[0]} has gotten three down!")
            return True


    #Diagonal winner
    diagonals = []
    cols = reversed(range(len(x)))
    rows = range(len(x))

    for indexOfX in range(len(x)):
        diagonals.append(x[indexOfX][indexOfX])
    if all_same(diagonals):
        print(f"Player {diagonals[0]} has gotten three diagonally!")
        return True

    diags = []
    for col,row in zip(cols,rows):
        diags.append(x[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} has gotten three diagonally!")
        return True

    return False







play = True
players = itertools.cycle([1, 2])
while play:
    x = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

    game_won = False
    x,_ = tictactoeboard(x, display=True)
    while not game_won:
        current_player = next(players)
        print(f"Players Turn: {current_player}")
        played = False

        while not played:
            column_choice = int(input("Play in column (0, 1, 2): "))
            row_choice = int(input("Play in row (0, 1, 2): "))
            x, played = tictactoeboard(x, current_player, row_choice, column_choice)

        if win(x):
            game_won = True
            again = input("Do you want to play again? (yes or no)")
            if again.upper() == "YES":
                print("restarting")
            if again.upper() == "NO":
                print("deuces mooses, hope to see you again!")
                play = False
            else:
                print("Not valid, goodbye and hope to see you again!")
                play = False





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