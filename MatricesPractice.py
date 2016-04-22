x = [[1,2],[3,4]]
print(x[0],x[0][1],x[0][0],x[1])
print(x)
x[0][1] = "f"
print(x)

grid = []
for i in range(3):
  grid.append([])
for i in grid:
  for j in range(3):
    i.append(j)
print(grid)
grid[0][1] = "f"
print(grid)
