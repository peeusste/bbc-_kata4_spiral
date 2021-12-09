matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13, 14, 15, 16]]
print ('input: ', matrix)

x,y = 0, 0 # current position
dx, dy = 1 ,0 # current direction
m, n = len(matrix), len(matrix[0])
c = 0
output = []

#loop until all cells visited
while c < m*n:
        # turn if boundary or null in front
        if (x == n-1 or matrix[y][x+1] == None) and dx == 1: dx, dy = 0, 1
        if (y == m-1 or matrix[y+1][x] == None) and dy == 1: dx, dy = -1, 0
        if (x == 0 or matrix[y][x-1] == None) and dx == -1: dx, dy = 0, -1
        if (matrix[y-1][x] == None and dy == -1): dx, dy = 1, 0

        output.append(matrix[y][x])
        matrix[y][x] = None # set visited cells to none
        x += dx
        y += dy
        c += 1

print ('output: ', output)
