n = 100

with open("day18.txt", "r") as f:
    grid = [[1 if c == "#" else 0 for c in s.strip('\n')] for s in f.readlines()]

grid[0][0] = 1
grid[n-1][0] = 1
grid[0][n-1] = 1
grid[n-1][n-1] = 1

def count_neighbors (grid, i, j):
    return sum([sum([grid[a][b] for a in range(max(i-1,0), min(i+2, n))]) for b in range (max(j-1,0), min(j+2,n)) ]) - grid[i][j]

for g in grid: print (g)

print('\n'.join([''.join(['#' if c else '.' for c in g]) for g in grid]))

print ('\n'.join([' '.join([str(count_neighbors(grid,i,j)) for j in range(n)]) for i in range(n)]))

iterations = 100
for step in range(iterations):
    g2 = [[count_neighbors(grid,i,j) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                g2[i][j] = (1 if g2[i][j] in [2,3] else 0)
            else:
                g2[i][j] = (1 if g2[i][j] == 3 else 0)
    grid = g2
    grid[0][0] = 1
    grid[n-1][0] = 1
    grid[0][n-1] = 1
    grid[n-1][n-1] = 1


print (sum([sum(grid[i]) for i in range(n)]))