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

x = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]


def tictactoeboard(game_map, player, row, column, display):
    print("   a  b  c")

    if not display:
        game_map[row][column] = player
    for count,row in enumerate(game_map):
        print(count,row)

    return game_map


x = tictactoeboard(x, 1, 0, 1, False)
