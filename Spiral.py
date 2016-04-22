def main():
  """
  file = open(spiral.txt, "r")
  dimension = file.readline()
  dimension.rstrip()
  dimension = int(dimension)
  target = file.readline()
  target.rstrip()
  target = int(target)
  file.close()
  """
  dimension = 100
  dimension2 = dimension
  target = 9000
  if (dimension % 2 == 0):
    dimension += 1
  top = dimension ** 2
  if target > top:
    print("The target number is not within range")
  grid = []
  for i in range(dimension):
    grid.append([])
  for i in grid:
    for j in range(dimension):
      i.append(j)
  count1 = 1
  count2 = 2
  count0 = 0
  while top >= 1:
    for i in range (count1, dimension + 1):
      grid[count1 - 1][dimension - i + count0] = top
      top -= 1
      
    for i in range (count1, dimension):
      grid[i][count0] = top
      top -= 1
      
    for i in range (count1, dimension):
      grid[dimension - 1][i] = top
      top -= 1
      
    for i in range (count2, dimension):
      grid[dimension - i + count0][dimension - 1] = top
      top -= 1

    count1 += 1
    count2 += 1
    count0 += 1

    dimension -= 1

  
  for i in grid:
    for j in i:
      if j == target:
        x = grid.index(i)
        y = i.index(target)
        if (x == 0) or (x == (dimension2 - 1)) or (y == 0) or (y == (dimension2 - 1)):
          print("Number on outer edge")
          return False
        else:
          print(x,y)
          print(grid[x-1][y-1], grid[x-1][y], grid[x-1][y+1])
          print(grid[x][y-1], grid[x][y], grid[x][y+1])
          print(grid[x+1][y-1], grid[x+1][y], grid[x+1][y+1])
    
  
  #print(grid)
  
main()
    
  
  

  
 

  
    
    
    
    
