class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if vertex was visited
  def wasVisited (self):
    return self.visited 

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the label
  def __str__(self):
    return str (self.label)

'''
class Edge (object):
  def __init__ (self, fromVertex, toVertex, weight):
    self.u = fromVertex
    self.v = toVertex
    self.weight = weight

  # comparison operators
  def __lt__ (self, other):

  def __le__ (self, other):

  def __gt__ (self, other):

  def __ge__ (self, other):

  def __eq__ (self, other):

  def __ne__ (self, other):
'''
  
class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # checks if a vertex label already exists
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # add a vertex with given label
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex (label))

      # add a new column in the adjacency matrix for new Vertex
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
    
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # does a depth first search in a graph
  def dfs (self, v):
    # create a stack
    theStack = Stack()

    # mark the vertex as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        u = theStack.pop() 
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)

    # stack is empty reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False


  # does a breadth first search in a graph
  def bfs (self, v):
    # create a queue
    theQueue = Queue ()

    # mark the vertex as visited and enqueue
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)

    while (not theQueue.isEmpty()):
      # get the vertex at the front
      v1 = theQueue.dequeue()
      # get an adjacent unvisited vertex
      v2 = self.getAdjUnvisitedVertex (v1)
      while (v2 != -1):
        (self.Vertices[v2]).visited = True
        print (self.Vertices[v2])
        theQueue.enqueue (v2)
        v2 = self.getAdjUnvisitedVertex (v1)

    # queue is empty reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False


 

  # determine if the graph has a cycle
  def hasCycle (self):
    for i in self.adjMat:
      if (len(i) - i.count(0)) % 2:
        return False
    return True

  # get index from vertex label
  def getIndex (self, label):

    for i in range(len(self.Vertices)):
        if label == self.Vertices[i].label:
            return i

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    for i in range(len(self.Vertices)):
        if self.Vertices[i].label == fromVertexLabel:
            from_index = i
    for i in range(len(self.Vertices)):
        if self.Vertices[i].label == toVertexLabel:
            to_index = i
    
    if self.adjMat[from_index][to_index] > 0:
      return self.adjMat[from_index][to_index]
    else:
      return -1
      
    



  def shortestPath(self, fromVertexLabel):
    
    #define included list
    included = []
    for i in range(len(self.Vertices)):
      included.append(None) 
    #find the fromVertex in self.Vertices
    for i in self.Vertices:
      if i.label == fromVertexLabel:
        parent = i
    #initialize grid
    results = []
    for i in range (len(self.Vertices)):
      results.append([self.Vertices[i],0,parent])
    #find the index of the parent on the results grid
    indx_p = self.getIndex(parent.label)

    for i in range(len(self.Vertices)):
      F = self.Vertices[i]
      
      if F == parent:
    
        results[indx_p][1] = 0
        results[indx_p][2] = None
        included[indx_p] = True

      elif self.getEdgeWeight(parent.label, F.label) != -1:
        results[i][1] = self.getEdgeWeight(parent.label, F.label)
        results[i][2] = parent
        included[i] = False

      else:
        results[i][1] = 10000
        results[i][2] = None
        included[i] = False
    while included.count(False) > 1:
      # find the vertex F that is not yet included
      for i in range (len(included)):
        if included[i] == False:
          #and has the minimal distance in the results grid
          for j in range (len(results)):
            if results[j][1] < results[i][1]:
              min_d = self.Vertices[j]
            else:
              pass
      min_idx = self.getIndex(min_d.label)
      included[min_idx] = True
      for k in range(len(included)):
        if included[k] == False:
          if self.getEdgeWeight(min_d.label, self.Vertices[k].label) > 0:
            new_dist = results[min_idx][1] + self.getEdgeWeight(min_d.label, self.Vertices[k].label)

            if new_dist <= results[k][1]:
              results[k][1] = new_dist
              results[k][2] = min_d
              included[k] = True

    return results
        
  
      
      
  
def main():
  # Create Graph object
  cities = Graph()

  # Open file for reading
  inFile = open ("./graph.txt", "r")

  # Read the vertices
  numVertices = int ((inFile.readline()).strip())
  print (numVertices)

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    print (city)
    cities.addVertex (city)

  # Read the edges
  numEdges = int ((inFile.readline()).strip())
  print (numEdges)

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    #print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])
    cities.addDirectedEdge (start, finish, weight)

  # Read the starting vertex for dfs, bfs, and shortest path
  startVertex = (inFile.readline()).strip()
  print (startVertex)

  # Close file
  inFile.close()

  # print the adjacency matrix
  """
  nVert = len (cities.Vertices)
  for i in range (nVert):
    for j in range (nVert):
      print (cities.adjMat[i][j], end = " ")
    print()
  print ()
  """

  # Do depth first search from Houston
  #print ("Depth First Search from Houston")
  #cities.dfs (11)
  #print()

  # Do breadth first search from Houston
  #print ("Breadth First Search from Houston")
  #cities.bfs (11)

  # Test hasCycle()
  #print(cities.hasCycle())

  # Test edgeList()
  #print(cities.edgeList())

  #Test shortestPath()
  v = cities.shortestPath('Seattle')
  for i in v:
    print(i[0].label,i[1],i[2])
    

main()
