#  File: Geometry.py

#  Description:

#  Student Name:Adriana Murga

#  Student UT EID:alm3657   

#  Partner Name:Ernesto Canales 

#  Partner UT EID:egc536

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0):
      self.x= x
      self.y=y

  # get distance to another Point object
  def dist (self, other):
      return math.sqrt((self.x-other.x) ** 2 + (self.y - other.y) ** 2)

  # create a string representation of a Point (x, y)
  def __str__ (self):
      return '(' + str(self.x) + ',' + str(self.y) + ')'
      
  # test for equality between two points
  def __eq__ (self, other):
      tol= 1.0e-18
      return (abs(self.x-other.x) + (self.y - other.y)) < tol
      
class Line (object):
  # constructor assign default values if user defined points are the same
  def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
    tol = 1.0e-18
    if ((abs(p1_x - p2_x) < tol) and (abs(p1_y - p2_y) < tol)):
      self.p1 = Point (0, 0)
      self.p2 = Point (1, 1)
    else:
      self.p1 = Point (p1_x, p1_y)
      self.p2 = Point (p2_x, p2_y)
      
  # determine if line is parallel to x axis
  def is_parallel_x (self):
    tol= 1.0e-18
    return abs(self.p1.y - (self.p2.y)) < tol

  # determine if line is parallel to y axis
  def is_parallel_y (self):
    tol= 1.0e-18
    return abs(self.p1.x - self.p2.x) < tol
  # determine slope for the line
  # return float ('inf') if line is parallel to the y-axis
  def slope (self):
    tol= 1.0e-18
    if self.is_parallel_y():
        return float('inf')
    else:
        return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)

  # determine the y-intercept of the line
  def y_intercept (self):
    return (self.p1.y - (self.slope() * self.p1.x))

  # determine the x-intercept of the line
  def x_intercept (self):
    return ( -1 * self.y_intercept()) / self.slope()

  # determine if two lines are parallel
  def is_parallel (self, other):
    tol= 1.0e-18
    return abs( self.slope() - other.slope()) < tol

  # determine if two lines are perpendicular to each other
  def is_perpendicular (self, other):
    tol= 1.0e-18
    return abs((self.slope() - (-1/ other.slope()))) < tol
  # determine if a point is on the line or on an extension of it
  def is_on_line (self, p):
    tol=1.0e-18
    return (abs (self.p.y - (self.slope()*self.x) - self.y)) < tol


  # determine the intersection point of two lines if not parallel
  def intersection_point (self, other):
      x= (other.y_intercept() - self.y_intercept())/ (self.slope() - other.slope())
      y= self.slope() * x - self.y_intercept()
      return Point(x,y)

  # determine the perpendicular distance of a point to the line
  def perp_dist (self, p):
    l= Line(p.x, p.y, (p.x + (self.p1.x - self.p2.y)), (p.y - (self.p1.y - self.p2.y)))
    return p.dist(self.intersection_point(l))
    
  # determine if two points are on the same side of the line
  # return False if one or both points are on the line
  def on_same_side (self, p1, p2):
      p1_intercept= p1.y - (self.slope() * p1.x)
      p2_intercept= p2.y - (self.slope() * p2.x)
      return ((p1_intercept > self.y_intercept() and (p2_intercept > self.y_intercept())) or ((p1_intercept < self.y_intercept()) and (p2_intercept < self.y_intercept())))
      

  # string representation of the line - one of three cases
  # y = c
  # x = c
  # y = m * x + b
  def __str__ (self):
    return "y = " + str(self.slope()) + "x " + str(self.y_intercept())
    if self.y_intercept() > 0:
      str_intercept = '+ ' + str(int(self.y_intercept()))
    else:
      str_intercept = str(int(self.y_intercept()))
    if self.slope() == 1:
      str_slope = ''
    else:
      str_slope = str(int(self.slope()))
      
    if self.is_parallel_x():
      return 'y = ' + str_intercept
    elif self.is_parallel_y():
      return 'x = '+ str_intercept
    else:
      return 'y = ' + str_slope + 'x ' + str_intercept

class Circle (object):
  # constructor with default values
  def __init__ (self, radius = 1, x = 0, y = 0):
      self.radius= radius
      self.center= Point(x,y)

  # compute circumference
  def circumference (self):
      return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
      return math.pi * self.radius * self.radius

  # determine if a point is inside the circle
  def is_inside_point (self, p):
      return (self.center.dist(p)) < self.radius

  # determine if the other circle is strictly inside self
  def is_inside_circle (self, other):
      distance= self.center.dist(other.center)
      return (distance + other.radius) < self.radius

  # determine if the other circle intersects self
  def does_intersect_circle (self, other):
      distance= self.center.dist(other.center)
      return (self.radius + other.radius) > distance 

  # determine if the line intersects circle
  def does_intersect_line (self, line):
      return line.perp_dist(self.center) < self.radius
              
  # determine if the line is tangent to the circle
  def is_tangent (self, line):
    tol = 1.0e-18
    return (abs(self.radius - line.perp_dist(self.center)) < tol)

  # string representation of a circle
  # Radius: radius, Center: (x, y)
  def __str__ (self):
    return 'Radius: ' + str(self.radius) +', Center: ' + str(self.center)
      
      
import math
def main():
  
  # open file "geometry.txt" for reading
  geometry= open('geometry.txt', 'r')
  #read the coordinates of the first Point P
  geometry_p = geometry.readline().split()
  p1_x= float(geometry_p[0])
  p1_y= float(geometry_p[1])
  geometry_p= Point(p1_x,p1_y)

  # read the coordinates of the second Point Q
  geometry_q= geometry.readline().split()
  p2_x= float(geometry_q[0])
  p2_y= float(geometry_q[1])
  geometry_q= Point(p2_x, p2_y)
  
  # print the coordinates of points P and Q
  print('Coordinates of P:', geometry_p,)
  print('Coordinates of Q: ', geometry_q)

  # print distance between P and Q
  distance= geometry_p.dist(geometry_q)
  print('Distance between P and Q: ', distance)

  # print the slope of the line PQ
  line_pq= Line(p1_x, p1_y, p2_x, p2_y)
  print("line pq: " + str(line_pq))
  print('Slope of PQ:', line_pq.slope())

  # print the y-intercept of the line PQ
  print('Y intercept of PQ:', line_pq.y_intercept())

  # print the x-intercept of the line PQ
  print('X intercept of PQ:', line_pq.x_intercept())

  # read the coordinates of the third Point A
  geometry_a = geometry.readline().split()
  p3_x= float(geometry_a[0])
  p3_y= float(geometry_a[1])
  geometry_a= Point(p3_x,p3_y)
			 
  # read the coordinates of the fourth Point B
  geometry_b = geometry.readline().split()
  p4_x= float(geometry_b[0])
  p4_y= float(geometry_b[1])
  geometry_b= Point(p4_x,p4_y)

  # print the string representation of the line AB
  line_ab=Line(p3_x, p3_y, p4_x, p4_y)
  print('Line AB: ',line_ab)

  # print if the lines PQ and AB are parallel or not
  if line_ab.is_parallel(line_pq):
    print('PQ is parallel to AB')
  else:
    print('PQ is not parallel to AB')

  # print if the lines PQ and AB (or extensions) are perpendicular or not
  if line_ab.is_perpendicular(line_pq):
    print('PQ is perpendicular to AB')
  else:
    print('PQ is not perpendicular to AB')

  # print coordinates of the intersection point of PQ and AB if not parallel
  if not line_ab.is_parallel(line_pq):
    print('Intersection point of PQ and AB:', line_ab.intersection_point(line_pq))

  # read the coordinates of the fifth Point G
  geometry_g = geometry.readline().split()
  p5_x= float(geometry_g[0])
  p5_y= float(geometry_g[1])
  geometry_g= Point(p5_x,p5_y)


  # read the coordinates of the sixth Point H
  geometry_h = geometry.readline().split()
  p6_x= float(geometry_h[0])
  p6_y= float(geometry_h[1])
  geometry_h= Point(p6_x,p6_y)
 
  

  #print if the the points G and H are on the same side of PQ
  if (line_pq.on_same_side(geometry_h, geometry_g)):
    print('G and H are on the same side of PQ')
  else:
    print('G and H are not on the same side of PQ')

  #print if the the points G and H are on the same side of AB
  if (line_ab.on_same_side(geometry_g, geometry_h)):
    print('G and H are on the same side of AB')
  else:
    print('G and H are not on the same side of AB')

  # read the radius of the circleA and the coordinates of its center
  geometry_circA = geometry.readline().split()
  radius1= float(geometry_circA[0])
  p7_x= float(geometry_circA[1])
  p7_y= float(geometry_circA[2])
  geometry_circA= Circle(radius1, p7_x,p7_y)
  
 
  # read the radius of the circleB and the coordinates of its center
  geometry_circB = geometry.readline().split()
  radius2 = float(geometry_circB[0])
  p8_x= float(geometry_circB[1])
  p8_y= float(geometry_circB[2])
  geometry_circB= Circle(radius2,p8_x,p8_y)
  
  
  # print the string representation of circleA and circleB
  print("circleA: Radius: " + str(radius1) + " Center: " + str(geometry_circA.center))
  print("circleB: Radius: " + str(radius2) + " Center: " + str(geometry_circB.center))
  
  # determine if circleB is inside circleA
  if geometry_circA.is_inside_circle(geometry_circB):
    print("circleB is inside circleA")
  else:
    print("circleB is not inside circleA")
    

  # determine if circleA intersects circleB
  if geometry_circA.does_intersect_circle(geometry_circB):
    print("circleA does intersect circleB")
  else:
    print("circleA does not intersect circleB")
    
  
  # determine if line PQ (or extension) intersects circleA
  if geometry_circA.does_intersect_line(line_pq):
    print("PQ does intersect circleA")
  else:
    print("PQ does not intersect circleA")
    
  
  # determine if line AB (or extension) is tangent to circleB
  if geometry_circB.is_tangent(line_ab):
    print("AB is tangent to circleB")
  else:
    print("AB is not a tangent to circleB")

  # close file "geometry.txt"
main()
