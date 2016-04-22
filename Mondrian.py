#  File: Mondrian.py

#  Description: This program uses recursion to imitate the abstract art of Piet Mondrian

#  Student Name: Ernesto Canales  

#  Student UT EID: egc536

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 03/04/2015

import turtle,random


def drawCanvas(art):
  art.pensize(65)
  art.pencolor('black')
  art.penup()
  art.goto(-400,400)
  art.pendown()
  art.goto(-400,-400)
  art.goto(400, -400)
  art.goto(400,400)
  art.goto(-400,400)
  art.penup()
  
def line(level,count):
  kind = ['h','v'] * 6
  if level >= 2:
    for i in range (count):
      kind.append('n')
  return random.choice(kind)


def Mon(x,y,hl,vl,level,count,art):
  start = [1/8,2/8,3/8,4/8,5/8,6/8,7/8]
  col = ['red','blue','yellow']
  art.fillcolor(random.choice(col))

  if level == 0:
    return
  art.pensize(random.randint(5,10))
  lin = line(level,count)
  if count >= 3:
    art.begin_fill()


  if lin == 'h':
    fraction = vl * random.choice(start)
    vl = vl - fraction
    y = y - fraction
    art.penup()
    art.goto(x,y)
    art.pendown()
    art.goto(x + hl,y)
    if random.randint(1,3) and (count >= 3):
      art.end_fill()
    Mon(x,y,hl,vl,level -1,count+1,art)
  if lin == 'v':
    fraction = hl * random.choice(start)
    hl = hl - fraction
    x = x + fraction
    art.penup()
    art.goto(x,y)
    art.pendown()
    art.goto(x,y-vl)
    if random.randint(1,3) == 1 and (count >= 3):
      art.end_fill()
    Mon(x,y,hl,vl,level -1,count+1,art)

    
  if lin == 'n':
    print('none')
    Mon(x,y,hl,vl,level -1,count+1,art)

    
    
  


def main():
  level = eval(input("Enter a level of recursion between 1 and 6: "))
  turtle.setup(800,800,0,0)
  art = turtle.Turtle()
  art.speed(7.0)
  drawCanvas(art)
  for i in range(level):
    Mon(-400,400,800,800,level,0,art)

  

main()
