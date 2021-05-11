# https://stackoverflow.com/questions/67491045/how-to-replace-items-in-a-list/67491142#67491142

board2 =[0,0,0,0,0,0,0,0,0]
inp = input('Input Number 0-8:')
if int(inp) in range(0, 9):
    board2[int(inp)] = 1
print(board2)
    