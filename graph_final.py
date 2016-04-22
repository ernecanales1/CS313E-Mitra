#  File: Graph.py

#  Description:

#  Student Name: Adriana Murga 

#  Student UT EID:alm3657

#  Partner Name:Ernesto Canales

#  Partner UT EID:egc536

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 5/5/2015

#  Date Last Modified:


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

  def __str__(self):
    if self.isEmpty():
      return
    else:
      a = []
      while not self.isEmpty():
        a.append(self.pop())
      return str(a)

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


class Edge (object):
  def __init__ (self, fromVertex, toVertex, weight):
    self.u = fromVertex
    self.v = toVertex
    self.weight = weight

  # comparison operators
  def __lt__ (self, other):
      return self.weight < other.weight

  def __le__ (self, other):
      return self.weight <= other.weight

  def __gt__ (self, other):
      return self.weight > other.weight

  def __ge__ (self, other):
      return self.weight >= other.weight

  def __eq__ (self, other):
      return self.weight == other.weight

  def __ne__ (self, other):
      return self.weight != other.weight
    

  
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
    all_ver = []
    # mark the vertex as visited and push on the stack
    (self.Vertices[v]).visited = True
    all_ver.append(self.Vertices[v])
    theStack.push (v)

    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        u = theStack.pop() 
      else:
        (self.Vertices[u]).visited = True
        all_ver.append(self.Vertices[u])
        theStack.push(u)

    # stack is empty reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

    return all_ver

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

  # get a list of neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    vertex_index = -1
    #vertex_index = self.Vertices.index(VertexLabel)
    for i in range(len(self.Vertices)):
        if self.Vertices[i].label == vertexLabel:
            vertex_index = i
    if vertex_index == -1:
      return

    
    neighbors = []
    for i in range (len(self.Vertices)):
      if self.adjMat[vertex_index][i]!= 0:
        neighbors.append(self.Vertices[i])
    neighbors_2 = []
    for j in range(len(neighbors)):
        label = neighbors[j].label
        neighbors_2.append(label)
    return neighbors_2
      

  # get a copy of the list of vertices
  def getVertices (self):
    list_Vert = []
    for i in self.Vertices:
        list_Vert.append(i.label)
    return list_Vert
    



  # prints a list of edges in ascending order of their weights
  # list is in the form [v1 - v2, v2 - v3, ..., vm - vn]
  def edgeList (self):
    edge_list = []
    edge_indx = []
    for i in range(len(self.Vertices)):
      for j in range(len(self.Vertices)):
        if self.adjMat[i][j] > 0:
          v1 = self.Vertices[i].label
          v2 = self.Vertices[j].label
          weight = self.adjMat[i][j]
          item = str(v1) + '--' + str(v2) + ' ' + str(weight)
          edge_list.append(item)
          edge_indx.append(weight)

    edge_indx.sort()
    
    rlist = []
    for i in range(len(edge_indx)):
      for j in edge_list:
        if edge_indx[i] == int(j[-1]):
          rlist.append(j)
          edge_list.remove(j)
          break
    
    return rlist
  
  def hasCycle(self):
    all_vertices = self.Vertices

    for vertex in all_vertices:
      visits = self.dfs(self.getIndex(vertex.label))
      if self.getEdgeWeight(visits[-1].label, visits[0].label) != -1:
        return True
    return False
   
  # return a list of vertices after a topological sort
  def toposort (self):
    stack = Stack()
    if self.hasCycle():
      print("Top sort can't be possible")
      return
    else:
      for i in range(len(self.Vertices)):
        self.Vertices[i].visited = False

      for i in range(len(self.Vertices)):
        vertex = self.Vertices[i]
        if vertex.visited == False:
          self.topDfs(self.getIndex(vertex.label), stack)
    a = []
    while not stack.isEmpty():
      a.append(self.Vertices[stack.pop()].label)

    return a

  def topDfs(self, v, stack):
    v_label = self.Vertices[v]
    v_label.visited = True

    w = self.getAdjUnvisitedVertex(v)
    if w != -1:
      self.topDfs(w, stack)

    stack.push(v)

    # if and only if the graph has no directed cycle

  # determine shortest path from a single vertex
  def shortestPath (self, fromVertexLabel):
    
    
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
      #print('min_d: ', min_d)
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

        
  '''# delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):'''
 

def main():
  # Create Graph object
  cities = Graph()

  # Open file for reading
  inFile = open ("graph.txt", "r")

  # Read the vertices
  numVertices = int ((inFile.readline()).strip())
  #print (numVertices)
  
  for i in range (numVertices):
    city = (inFile.readline()).strip()
    #print (city)
    cities.addVertex (city)

  # Read the edges
  numEdges = int ((inFile.readline()).strip())
  #print (numEdges)

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
  #print (startVertex)

  # Close file
  inFile.close()
  
  # print the adjacency matrix
  '''nVert = len (cities.Vertices)
  for i in range (nVert):
    for j in range (nVert):
      print (cities.adjMat[i][j], end = " ")
    print()
  print ()'''

  #Check SSSP
  #Test shortestPath()
  v = cities.shortestPath('Dallas')
  for i in v:
    print(i[0].label,i[1],i[2])
    
  #Do depth first search from Houston
  index = cities.getIndex(startVertex)
  print ("Depth First Search from Dallas")
  all_vertex = cities.dfs (index)
  for i in range(len(all_vertex)):
    print(all_vertex[i])
  print()

  # Do breadth first search from Houston
  print ("Breadth First Search from Dallas")
  cities.bfs (index)
  print()
  #topo sort
  print('Topological Sort:')
  if cities.toposort():
    for i in cities.toposort():
      print(i)
    print()  

  print('Ascending Edges:')
  for i in (cities.edgeList()):
    print(i)
  print()
  

  #Check SSSP
  #Test shortestPath()
  v = cities.shortestPath('Dallas')
  for i in v:
    print(i[0].label,i[1],i[2])
  
  #Check getEdgeWeight
  #print('edge weight', cities.getEdgeWeight('Austin','Dallas'))

  #Check getNeighbors()
  #print(cities.getNeighbors('Houston'))

  #Check getVertices()
  #print(cities.getVertices())

  #Check cycle

  #print('Has cycle: ', cities.hasCycle())
  

  
main()
    


    
    
