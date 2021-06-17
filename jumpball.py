import turtle
win = turtle.Screen()
win.bgcolor("black")
win.title("Jumping ball")
win.setup(width=800,height=600)


#paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_wid=1,stretch_len=5)
paddle.color("red")
paddle.penup()
paddle.goto(0,-250)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
#move per 2 pixel
ball.dy = 2

#pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(300,230)
pen.write("Close to click here")

close = turtle.Turtle()
close.speed(0)
close.color("white")
close.shape("square")
close.penup()
close.goto(280,230)


#main loop
while True:
	#move ball
	ball.sety(ball.ycor()-ball.dy)
	if ball.ycor()<-230:
		ball.sety(-230)
		ball.dy*=-2

	if ball.ycor()>100:
		ball.sety(100)
		ball.dy=-3
		ball.dy*=-1

	def button(x,y):
		win.bgcolor("white")
		turtle.Screen().bye()

	close.onclick(button)

	win.update()