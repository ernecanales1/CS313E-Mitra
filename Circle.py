import turtle

def drawCircle():
  for i in range (20,1,-1):
    # draw a circle
    turtle.penup()
    turtle.goto (200, (i * 10))
    turtle.pendown()
    #turtle.begin_fill()
    #turtle.color ('purple')
    turtle.circle (i * 5)
    turtle.end_fill()

def main():

  drawCircle()

main()
