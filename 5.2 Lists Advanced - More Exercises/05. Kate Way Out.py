import os                          
os.system('clear')                        #TODO  only 60pts
import sys                              

def find_path(row, col, direction):
    global step

    if (row == 0 or col == 0 or row == len(maze)-1 or col == len(maze[0])-1 ) and maze[row][col] == ' ':   # Check if we have found the exit
        print(f'Kate got out in {len(step) + 1} moves')
        sys.exit()  
            
    if maze[row][col] == ' ':   # The current cell is free. Mark it as visited
       step.append(direction)   # Append the direction to the path
       maze[row][col] = 'v'
                                # Invoke recursion to explore all possible directions
       find_path(row, col - 1, 'L') # left
       find_path(row - 1, col, 'U') # up
       find_path(row, col + 1, 'R') # right
       find_path(row + 1, col, 'D') # down
                                 

direction = ''
step = []
maze = []
row, col = 0, 0

for i in range(int(input())):
    current_row = []
    token = input()
    for j in range(len(token)):
        if 'k' in token[j]:
            row = i  
            col = j
            current_row.append(' ')
        else:      
            current_row.append(token[j])   
    maze.append(current_row)
   

find_path(row,col, direction)

print('Kate cannot get out')

