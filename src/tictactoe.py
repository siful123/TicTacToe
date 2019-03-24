

''' Different ways to get indices from a list
l = [1, 2, 3, 4, 5, 6, 7]
print(l[1])
print(l[-1])
print(l[1:])
print(l[1:2])
'''

x = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]


def tictactoeboard(player, row, column, display):
    print("   a  b  c")

    if not display:
        x[row][column] = player
    for count,row in enumerate(x):
        print(count,row)


tictactoeboard(1,0,1,False)