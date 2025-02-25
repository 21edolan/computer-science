#2 players, x and o
#spaces= top left, top middle, top right, middle left,---
#--- middle, middle right, bottom left, bottom middle,---
#--- bottom right ?????????
grid=('''_ |_ | _
_ | _ | _
   |    |''')
rules=print('''RULES!!:
1) Player one uses 'x', player 2 uses 'o'
2) Once a letter is placed it cannot be undone
3) The placements are labelled 0-8, going from top left-bottom right
4) Get three letters in a row to win''')
player1=input('palyer one, please enter a name:')
player2=input('player two, please enter a name:')
print('greetings',player1,'and',player2,', Game start!!')
print(grid)
lstup=[0,1,2]
lstmid=[3,4,5]
lstdn=[6,7,8]
numgrid='''0|1|2
3|4|5
6|7|8'''
rnd1=input('player one, where will you place an x?:')
