# https://stackoverflow.com/questions/67491045/how-to-replace-items-in-a-list/67491142#67491142

board2 =[0,0,0,0,0,0,0,0,0]
inp = input('Input Number 0-8:')
if 0 <= int(inp) < len(board2):
    board2[int(inp)] = 1
print(board2)
    