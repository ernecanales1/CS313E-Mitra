#  File: Train.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:


import turtle, math
turtle.setup(800,800,0,0)
ttl = turtle.Turtle()
def drawCircle(pos_x,pos_y,circumference,color):
  ttl.penup()
  ttl.goto (pos_x, pos_y)
  ttl.pendown()
  ttl.color (color)
  ttl.circle (circumference)
  
def drawLine (x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()
  
def drawPolygon (x, y, num_side, radius):
  sideLen = 2 * radius * math.sin (math.pi / num_side)
  sideLen2 = sideLen / 3
  angle = 360 / num_side
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  for i in range (num_side//2):
    ttl.forward (sideLen)
    ttl.left (angle)
    ttl.forward(sideLen2)
    ttl.left (angle)
    
def drawWindows (x, y, num_side, radius):
  ttl.begin_fill()
  ttl.color('gray')
  sideLen = 2 * radius * math.sin (math.pi / num_side)
  sideLen2 = sideLen / 1.2
  angle = 360 / num_side
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  ttl.pencolor('blue')
  
  for i in range (num_side//2):
    ttl.forward (sideLen2)
    ttl.left (angle)
    ttl.forward(sideLen)
    ttl.left (angle)
  ttl.end_fill()
  ttl.penup
  
def drawRoof(x, y, num_side, radius):
  ttl.pencolor('blue')
  sideLen = 2 * radius * math.sin (math.pi / num_side)
  sideLen2 = sideLen / 15
  angle = 360 / num_side
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  for i in range (num_side//2):
    ttl.forward (sideLen)
    ttl.left (angle)
    ttl.forward(sideLen2)
    ttl.left (angle)
    
def drawHouse():
  ttl.pencolor('blue')
  ttl.penup()
  ttl.goto(-300,300)
  ttl.right(90)
  ttl.pendown()
  ttl.forward(240)
  ttl.left(90)
  ttl.forward(40)
  ttl.right(90)
  ttl.circle(60,-180)
  ttl.right(90)
  ttl.forward(40)
  ttl.left(90)
  ttl.forward(240)
  
def drawBody():
  ttl.pencolor('blue')
  ttl.penup()
  ttl.goto(-100,250)
  ttl.pendown()
  ttl.right(90)
  ttl.forward(350)
  ttl.right(90)
  ttl.forward(190)
  ttl.right(90)
  ttl.forward(40)
  ttl.right(90)
  ttl.circle(60,180)
  ttl.right(90)
  ttl.forward(30)
  ttl.right(90)
  ttl.circle(60,180)
  ttl.right(90)
  ttl.goto(-100, 60)
  
def drawRails():
  ttl.pencolor('black')
  drawLine(-300,10,350,10)
  drawLine(-300,0,350,0)
  for i in range (13):
    drawPolygon(-290 + (i * 50),-5,4,10)
    
def drawRectangle(x,y,len1,len2):
  ttl.pencolor('blue')
  ttl.penup()
  ttl.goto(x,y)
  ttl.pendown()
  ttl.goto(x + len1,y)
  ttl.goto(x + len1, y + len2)
  ttl.goto(x, y + len2)
  ttl.goto(x,y)
  ttl.penup()
  
def drawTop():
  ttl.pencolor('blue')
  #Draw top rectangles
  drawRectangle(10,250,45,20)
  drawRectangle(17.5,270,30,10)
  #Draw trapezoids
  ttl.penup()
  ttl.goto(125,250)
  ttl.pendown()
  ttl.goto(110,290)
  ttl.right(180)
  ttl.forward(60)
  ttl.goto(155,250)
  ttl.penup()
  ttl.goto(110,290)
  ttl.pendown()
  ttl.goto(115,300)
  ttl.forward(50)
  ttl.goto(170,290)
def drawDetail():
  ttl.penup()
  ttl.goto(10,250)
  ttl.pendown()
  ttl.right(90)
  ttl.forward(95)
  ttl.goto(-100,155)
  ttl.goto(-100,145)
  ttl.goto(250,145)
  ttl.goto(250,155)
  ttl.goto(140,155)
  ttl.goto(140,250)
  ttl.goto(134,250)
  ttl.goto(134,155)
  ttl.goto(16,155)
  ttl.goto(16,250)
  
  

def drawFront():
  ttl.pencolor('blue')
  drawRectangle(250,240,15,-150)
  drawRectangle(265,(240 - (75/2)),5,-75)
  ttl.penup()
  ttl.goto(250,80)
  ttl.pendown()
  ttl.goto(280,80)
  ttl.goto(300,40)
  ttl.goto(250,40)
  ttl.goto(250,80)

def drawWheels(x,y,xd,yd,r1,r2):
  drawLine(x,y,xd-3,yd+1)
  drawLine(x,y,xd+3,yd+1)
  drawLine(x+r1,y+r1,xd+r2,y+r1+3)
  drawLine(x+r1,y+r1,xd+r2,y+r1-3)
  drawLine(x,y+(2*r1),xd+3,yd+(2*r2))
  drawLine(x,y+(2*r1),xd-3,yd+(2*r2))
  drawLine(x-r1,y+r1,xd-r2,y+r1+3)
  drawLine(x-r1,y+r1,xd-r2,y+r1-3)
"""
  ttl.goto(x + (r1 * math.cos(math.pi/2)), y + (r1 * math.sin(math.pi/2)))
  ttl.pendown()
  ttl.goto((xd + (r2 * math.cos(math.pi/2)), yd + (r2 * math.sin(math.pi/2)))
 """         

"""
  x = x + r1 * math.cos(5 * math.pi/4)
  y = y + r1 * math.sin(5 * math.pi/4)
  xd = xd + r2 * math.cos(5 * math.pi/4)
  yd = yd + r2 * math.sin(5 * math.pi/4)
  drawLine(x,y,xd-3,yd+1)
  drawLine(x,y,xd+3,yd+1)
  drawLine(x+r1,y+r1,xd+r2,y+r1+3)
  drawLine(x+r1,y+r1,xd+r2,y+r1-3)
  drawLine(x,y+(2*r1),xd+3,yd+(2*r2))
  drawLine(x,y+(2*r1),xd-3,yd+(2*r2))
  drawLine(x-r1,y+r1,xd-r2,y+r1+3)
  drawLine(x-r1,y+r1,xd-r2,y+r1-3)
  

  
  
  

  
  for i in range(90,360,90):
    i = i * 0.0174532925
    x1 = x + (r1 * math.cos(i))
    y1 = y + (r1 * math.sin(i))
    print(x1,y1)
    x2 = xd + (r2 * math.cos(i + 5))
    y2 = yd + (r2 * math.sin(i + 5))
    x3 = xd + (r2 * math.cos(i - 5))
    y3 = yd + (r2 * math.sin(i - 5))
    drawLine(x1,y1,x2,y2)
    drawLine(x1,y1,x3,y3)

  """
def drawNails():
  for i in range(1,10):
    ttl.penup()
    ttl.goto(13,250 - (9.5 * i))
    ttl.dot(3,'black')
  for i in range(1,35):
    ttl.penup()
    ttl.goto(-100 + (10 * i),150)
    ttl.dot(3,'black')
  for i in range(1,10):
    ttl.penup()
    ttl.goto(137,250 - (9.5 * i))
    ttl.dot(3,'black')
    
    
    

  
    

  
  
  
  
  


def main():
  
  #Draw big wheel
  drawCircle(-200,10,50,'red')
  drawCircle(-200,20,39,'red')
  drawCircle(-200,45,12.4,'red')
  drawWheels(-200,45,-200,20,12.4,39)
  
  #Draw two small wheels
  drawCircle(0,10,40,'red')
  drawCircle(0,19,31.5,'red')
  drawCircle(0,39,10,'red')

  drawWheels(0,39,0,19,10,31.5)
  
  drawCircle(150,10,40,'red')
  drawCircle(150,19,31.5,'red')
  drawCircle(150,39,10,'red')
  drawWheels(150,39,150,19,10,31.5)

  #Draw Rails
  drawRails()

  #Draw Windows
  for i in range (2):
    drawWindows(-280 + (i * 95),200,4,55)

  #Draw Roof
  drawRoof(-320, 300,4,180)
  #Draw body of train
  drawHouse()
  drawBody()
  drawTop()
  drawDetail()
  drawNails()
  drawFront()
  


main()

