#!usr/bin/python2.7

import turtle
from random import randint
from Tkinter import *



#the drawsens function is here to determine in what sens your draw could it be realized, taking as first parameter the angle and in second parameter the sens as a binary value, 0 for a right rotation, 1 for a left rotation
def drawsens(turtle, angle, sens):
	if sens == 0:
		turtle.rt(angle) 
	if sens == 1:
		turtle.lt(angle)
	return	
	
	
#gradient function allow to make gradient from a colour to void or from void to colour, the fade parameter is used in order to get what you want as gradient, only an integer is required, 0 for a void to color you want (specified as first parameter as a short int value beetween 0 and 255), 1 for a color to void 
def gradientcolor(color, fade):
	if fade == 0:
		if color != 255:
			color = color + 5
	if fade == 1:
		if color != 0:
			color = color - 5
	return color
		
		
#first mandala based on random variable to never be the same 
def randmandala1(bg):
	#set up the turtle
	configcvturtle = turtle.TurtleScreen(bg)
	cvturtle = turtle.RawTurtle(configcvturtle)
	configcvturtle.bgcolor("black")
	cvturtle.speed(0)
	cvturtle.hideturtle()
	cvturtle.goto(bg.winfo_width()/2, bg.winfo_height()/2*-1)
	cvturtle.pencolor("white")
	configcvturtle.colormode(255)

	#start the draw function
	constrand = randint(0,90)
	randist = randint(90, 250)
	randsens = randint(0,1)
	x = 0
	cvturtle.down()
	while randist / 2 > x:
		r = randint(0,255) 
		g = randint(0,255) 
		b = randint(0,255)
		cvturtle.pencolor(r,g,b)
		drawsens(cvturtle, 45, randsens)
		cvturtle.fd(randist)
		drawsens(cvturtle, 270, randsens)
		cvturtle.fd(randist)
		drawsens(cvturtle, 270, randsens)
		cvturtle.fd(randist)
		drawsens(cvturtle, 270, randsens)
		cvturtle.fd(randist * 2)
		drawsens(cvturtle, 90, randsens)
		cvturtle.fd(randist)
		drawsens(cvturtle, 90, randsens)
		cvturtle.fd(randist)
		drawsens(cvturtle, 90, randsens)
		cvturtle.fd(randist)
		drawsens(cvturtle, constrand, randsens)
		x = x + 1
	cvturtle.up()
	return
	
	
#second mandala based on random variable to never be the same 
def randmandala2(bg):
	#set up the turtle
	configcvturtle = turtle.TurtleScreen(bg)
	cvturtle = turtle.RawTurtle(configcvturtle)
	configcvturtle.bgcolor("black")
	cvturtle.speed(0)
	cvturtle.hideturtle()
	cvturtle.goto(bg.winfo_width()/2, bg.winfo_height()/2*-1)
	cvturtle.pencolor("white")
	y = bg.winfo_height()/2*-1
	x = bg.winfo_width()/2
	configcvturtle.colormode(255)
	
	#start the draw function
	loop = 0
	angle1 = randint(0, 360)
	angle2 = randint(0, 360)
	spaceangle = randint(90, 210)
	dist1 = randint(100, 350) 
	dist2 = randint(100, 350)
	randsens = randint(0, 1)
	cvturtle.down()
	while loop < spaceangle / 2 :
		r = randint(0,255) 
		g = randint(0,255) 
		b = randint(0,255) 
		
        	cvturtle.pencolor(r,g,b)
		drawsens(cvturtle, angle1, randsens)
		cvturtle.fd(dist1)
		drawsens(cvturtle, angle2, randsens)
		cvturtle.fd(dist2)
		cvturtle.goto(x, y)
		drawsens(cvturtle, x*spaceangle, randsens)
		loop = loop + 1
	cvturtle.up()	
	return


#thirst mandala based on random variable to never be the same, take as parameter the default position x, and y in order to be placed wherever we want 
def seashell(x,y,bg):
	#set up the turtle
	configcvturtle = turtle.TurtleScreen(bg)
	cvturtle = turtle.RawTurtle(configcvturtle)
	configcvturtle.bgcolor("black")
	cvturtle.speed(0)
	cvturtle.hideturtle()
	cvturtle.goto(bg.winfo_width()/2, bg.winfo_height()/2*-1)
	configcvturtle.colormode(255)
	
	#start the draw function
	cvturtle.up()
	cvturtle.setx(x)
	cvturtle.sety(y)
	cvturtle.down()
	angle = 0
	randbool = randint(0,1)
	r = 0
	g = 0 
	b = 0
	colorchoose = randint(0, 5)
	
	while angle < 150:
		
		g = gradientcolor(g, 0)
		if g == 255:
			b = gradientcolor(b, 0)
			if b == 255:
				r = gradientcolor(r, 0)
	
		
		if colorchoose == 0:
			cvturtle.pencolor(r,g,b)
		if colorchoose == 1:
			cvturtle.pencolor(r,b,g)
		if colorchoose == 2:
			cvturtle.pencolor(b,r,g)
		if colorchoose == 3:
			cvturtle.pencolor(b,g,r)
		if colorchoose == 4:
			cvturtle.pencolor(g,b,r)
		if colorchoose == 5:
			cvturtle.pencolor(g,r,b)
				
		cvturtle.circle(40+angle)
		
		drawsens(cvturtle, 2, randbool)
		angle = angle + 1
	return 

#fourth mandala based on random variables to be drown, and the first who come with real random gradient colors
def rotatesqrt(bg):
	#set up the turtle
	configcvturtle = turtle.TurtleScreen(bg)
	cvturtle = turtle.RawTurtle(configcvturtle)
	configcvturtle.bgcolor("black")
	cvturtle.speed(0)
	cvturtle.hideturtle()
	cvturtle.goto(bg.winfo_width()/2, bg.winfo_height()/2*-1)
	y = bg.winfo_height()/2*-1
	x = bg.winfo_width()/2
	configcvturtle.colormode(255)
	
	#set up the differents variables(color, random etc...)
	r = 0
	g = 0
	b = 0
	increment = 0	
	randrotate = randint(1, 44)
	colorchoose = randint(0, 5)
	
	#start to draw 
	while increment < 1000:	
		randcolor = randint(0, 5)
		if randcolor == 0:
			if r + 20 < 255:
				r = gradientcolor(r, 0) + 15
		if randcolor == 1:	
			if r - 20 > 0:
				r = gradientcolor(r, 1) - 15
		if randcolor == 2:
			if g + 20 < 255:	
				g = gradientcolor(g, 0) + 15
		if randcolor == 3:
			if g - 20 > 0:
				g = gradientcolor(g, 1) - 15
		if randcolor == 4:
			if b + 20 < 255:
				b = gradientcolor(b, 0) + 15
		if randcolor == 5:
			if b - 20 > 0:
				b = gradientcolor(b, 1)	- 15
			
		if colorchoose == 0:
			cvturtle.pencolor(r,g,b)
		if colorchoose == 1:
			cvturtle.pencolor(r,b,g)
		if colorchoose == 2:
			cvturtle.pencolor(b,r,g)
		if colorchoose == 3:
			cvturtle.pencolor(b,g,r)	
		if colorchoose == 4:
			cvturtle.pencolor(g,b,r)
		if colorchoose == 5:
			cvturtle.pencolor(g,r,b)
	
		cvturtle.up()
		cvturtle.fd(50 + (increment/2))
		cvturtle.rt(90)
		cvturtle.down()
		cvturtle.fd(50 + (increment/2))
		cvturtle.rt(90)	
		cvturtle.fd(100 + increment)
		cvturtle.rt(90)
		cvturtle.fd(100 + increment)	
		cvturtle.rt(90)	
		cvturtle.fd(100 + increment)
		cvturtle.rt(90)
		cvturtle.fd(50 + (increment/2))
		cvturtle.up()
		cvturtle.setx(x)
		cvturtle.sety(y)
		cvturtle.rt(45)
		cvturtle.fd(50 + (increment/2))
		cvturtle.down()
		cvturtle.rt(90)
		cvturtle.fd(50 + (increment/2))
		cvturtle.rt(90)
		cvturtle.fd(100 + increment)
		cvturtle.rt(90)
		cvturtle.fd(100 + increment)
		cvturtle.rt(90)
		cvturtle.fd(100 + increment)
		cvturtle.rt(90)
		cvturtle.fd(50 + (increment/2))
		cvturtle.up()
		cvturtle.setx(x)
		cvturtle.sety(y)
		increment = increment + 10
		cvturtle.rt(randrotate)	
	return

#draw a wtf 3D colored 
def wtf3d(bg):
	#set up the turtle
	configcvturtle = turtle.TurtleScreen(bg)
	cvturtle = turtle.RawTurtle(configcvturtle)
	configcvturtle.bgcolor("black")
	cvturtle.speed(0)
	cvturtle.hideturtle()
	cvturtle.goto(bg.winfo_width()/2, bg.winfo_height()/2*-1)
	configcvturtle.colormode(255)
	y = bg.winfo_height()/2*-1
	x = bg.winfo_width()/2
	
	#create differents variables(loop, sens of draw...)
	loop = 0
	dimensionx = randint(0, 1)
	dimensiony = randint(0, 1)
	
	#create a start position points of the different letters
	Xw = -800 + x
	Yw = 300 + y
	Xt = -200 + x
	Yt = 300 + y
	Xf = 400 + x
	Yf = 300 + y
	
	#first part which set the color 
	r = 0
	g = 0
	b = 0
	randcolor = randint(0,2)
	#randcolor2 is set with 3 possibilities = fade into 2 others colors or void 
	randcolor2 = randint(0, 2)
	if randcolor == 0:
		r = 255
	if randcolor == 1:
		g = 255
	if randcolor == 2:
		b = 255
	
	
	#start to draw 
	while loop < 100:	
		
		
		#second part which set the color inside the loop so we can have a nice gradient 
		if randcolor == 0:
			r = gradientcolor(r, 1)
			if randcolor2 == 0:
				g = gradientcolor(g, 0)
			if randcolor2 == 1:
				b = gradientcolor(b, 0)
		if randcolor == 1:
			g = gradientcolor(g, 1)
			if randcolor2 == 0:
				r = gradientcolor(r, 0)
			if randcolor2 == 1:
				b = gradientcolor(b, 0)
		if randcolor == 2:
			b = gradientcolor(b, 1)
			if randcolor2 == 0:
				g = gradientcolor(g, 0)
			if randcolor2 == 1:
				r = gradientcolor(r, 0)
		
		cvturtle.pencolor(r, g, b)
		
		#draw a 'W'	
		
		
		#start positionning the pen and the draw direction 
		cvturtle.up()
		if dimensionx == 0:
			cvturtle.setx(Xw + loop)
		if dimensionx == 1:
			cvturtle.setx(Xw - loop)
		if dimensiony == 0:
			cvturtle.sety(Yw + loop)
		if dimensiony == 1:
			cvturtle.sety(Yw - loop)
		cvturtle.down()
		
		#drawing 
		cvturtle.fd(100)
		cvturtle.rt(90)
		cvturtle.fd(400)
		cvturtle.lt(90)
		cvturtle.fd(100)
		cvturtle.lt(90)
		cvturtle.fd(400)
		cvturtle.rt(90)
		cvturtle.fd(100)
		cvturtle.rt(90)
		cvturtle.fd(400)
		cvturtle.lt(90)
		cvturtle.fd(100)
		cvturtle.lt(90)
		cvturtle.fd(400)
		cvturtle.rt(90)
		cvturtle.fd(100)
		cvturtle.rt(90)
		cvturtle.fd(500)
		cvturtle.rt(90)
		cvturtle.fd(500)
		cvturtle.rt(90)
		cvturtle.fd(500)
		cvturtle.rt(90)
		cvturtle.up()
			
	
		
		#draw a 'T'
		
		#start positionning the pen and the draw direction 
		cvturtle.up()
		if dimensionx == 0:
			cvturtle.setx(Xt + loop)
		if dimensionx == 1:
			cvturtle.setx(Xt - loop)
		if dimensiony == 0:
			cvturtle.sety(Yt + loop)
		if dimensiony == 1:
			cvturtle.sety(Yt - loop)
		cvturtle.down()
		
		#drawing
		cvturtle.down()
		cvturtle.fd(500)
		cvturtle.rt(90)
		cvturtle.fd(100)
		cvturtle.rt(90)
		cvturtle.fd(200)
		cvturtle.lt(90)
		cvturtle.fd(400)
		cvturtle.rt(90)
		cvturtle.fd(100)	
		cvturtle.rt(90)	
		cvturtle.fd(400)	
		cvturtle.lt(90)
		cvturtle.fd(200)
		cvturtle.rt(90)
		cvturtle.fd(100)
		cvturtle.rt(90)
		cvturtle.up()
	
		#draw a 'F'
		
		#start positionning the pen and the draw direction 
		cvturtle.up()
		if dimensionx == 0:
			cvturtle.setx(Xf + loop)
		if dimensionx == 1:
			cvturtle.setx(Xf - loop)
		if dimensiony == 0:
			cvturtle.sety(Yf + loop)
		if dimensiony == 1:
			cvturtle.sety(Yf - loop)
		cvturtle.down()
		
		
		#drawing 
		cvturtle.down()
		cvturtle.fd(500)
		cvturtle.rt(90)
		cvturtle.fd(100)
		cvturtle.rt(90)
		cvturtle.fd(400)
		cvturtle.lt(90)
		cvturtle.fd(100)
		cvturtle.lt(90)
		cvturtle.fd(300)
		cvturtle.rt(90)
		cvturtle.fd(100)
		cvturtle.rt(90)
		cvturtle.fd(300)
		cvturtle.lt(90)
		cvturtle.fd(200)
		cvturtle.rt(90)
		cvturtle.fd(100)
		cvturtle.rt(90)
		cvturtle.fd(500)
		cvturtle.rt(90)
		loop= loop + 2

	return 

#simple function for spread some 2000 stars randomly on the screen 	
def spreadstars(bg):
	#set up the turtle
	configcvturtle = turtle.TurtleScreen(bg)
	cvturtle = turtle.RawTurtle(configcvturtle)
	configcvturtle.bgcolor("black")
	cvturtle.speed(0)
	cvturtle.hideturtle()
	cvturtle.color("white")
	#create the x variable and start to draw inside the loop function
	x = 0
	while x < 200:
		#set the pen to a random position on the screen
		cvturtle.up()
		randx = randint(-900,1800)
		randy = randint(-1000,800)
		cvturtle.setx(randx)
		cvturtle.sety(randy)
		cvturtle.down()
		
		#draw a star
		cvturtle.fd(1)
		cvturtle.rt(90)
		cvturtle.fd(1)
		cvturtle.rt(90)
		cvturtle.fd(1)
		x = x + 1
	return 
	

def trippystar(bg):
	#set up the turtle
	configcvturtle = turtle.TurtleScreen(bg)
	cvturtle = turtle.RawTurtle(configcvturtle)
	configcvturtle.bgcolor("black")
	cvturtle.speed(0)
	cvturtle.hideturtle()
	cvturtle.goto(bg.winfo_width()/2, bg.winfo_height()/2*-1)	
	y = bg.winfo_height()/2*-1
	x = bg.winfo_width()/2
	configcvturtle.colormode(255)
	
	
	#create the differents variables needed to draw(the corners of the star, the loops, the colors and the random variables)
	topstar = y + 500
	bottomstar = y - 500
	loop1 = 0
	loop2 = 0
	r = 0
	g = 0
	b = 0
	randcolor = randint(0,2)
	randcolor2 = randint(0, 2)
	
	#select a start color in order to do a gradient(end of the color algo inside the loop)
	if randcolor == 0:
		r = 255
	if randcolor == 1:
		g = 255
	if randcolor == 2:
		b = 255
	
	#start to draw 
	while loop1 < 500:
		
		#every 2 loops the grandient fade into another random color
		if loop1 % 2 == 0:
			if randcolor == 0:
				r = gradientcolor(r, 1)
				if randcolor2 == 0:
					g = gradientcolor(g, 0)
				if randcolor2 == 1:
					b = gradientcolor(b, 0)
			if randcolor == 1:
				g = gradientcolor(g, 1)
				if randcolor2 == 0:
					r = gradientcolor(r, 0)
				if randcolor2 == 1:
					b = gradientcolor(b, 0)
			if randcolor == 2:
				b = gradientcolor(b, 1)
				if randcolor2 == 0:
					g = gradientcolor(g, 0)
				if randcolor2 == 1:
					r = gradientcolor(r, 0)
	
		cvturtle.pencolor(r,g,b)
		cvturtle.up()
		cvturtle.goto(x - loop1, y)
		cvturtle.down()
		cvturtle.goto(x, topstar)
		cvturtle.up()
		cvturtle.goto(x, bottomstar)
		cvturtle.down()
		cvturtle.goto(x + loop1, y)
		loop1 = loop1 + 5
		bottomstar = bottomstar + 5
		topstar = topstar - 5
	
	#reset variables needed for the second loop 
	randcolor = randint(0,2)
	randcolor2 = randint(0, 2)
	topstar = y + 500
	bottomstar = y - 500
	
	#reset the color algo 
	if randcolor == 0:
		r = 255
	if randcolor == 1:
		g = 255
	if randcolor == 2:
		b = 255
	
	
	#sdo the same as the first loop 
	while loop2 < 500:
		
		if loop2 % 2 == 0:
			if randcolor == 0:
				r = gradientcolor(r, 1)
				if randcolor2 == 0:
					g = gradientcolor(g, 0) 
				if randcolor2 == 1:
					b = gradientcolor(b, 0) 
			if randcolor == 1:
				g = gradientcolor(g, 1) 
				if randcolor2 == 0:
					r = gradientcolor(r, 0) 
				if randcolor2 == 1:
					b = gradientcolor(b, 0) 
			if randcolor == 2:
				b = gradientcolor(b, 1) 
				if randcolor2 == 0:	
					g = gradientcolor(g, 0) 
				if randcolor2 == 1:
					r = gradientcolor(r, 0)
	
		cvturtle.pencolor(r,g,b)
	
		cvturtle.up()
		cvturtle.goto(x - loop2, y)
		cvturtle.down() 
		cvturtle.goto(x, bottomstar)
		cvturtle.up()
		cvturtle.goto(x, topstar)
		cvturtle.down()
		cvturtle.goto(x + loop2, y)
		loop2 = loop2 + 20
		bottomstar = bottomstar + 20
		topstar = topstar- 20
	return 	


def enhancedMandala(bg):
	#set up the turtle
	configcvturtle = turtle.TurtleScreen(bg)
	cvturtle = turtle.RawTurtle(configcvturtle)
	configcvturtle.bgcolor("black")
	cvturtle.speed(0)
	cvturtle.hideturtle()
	cvturtle.goto(bg.winfo_width()/2, bg.winfo_height()/2*-1)
	configcvturtle.colormode(255)
	
	#creates a variable x with value 0	
	x = 0 
	
	#while the value of x is lesser than 120,
	while x < 300: 
	    
	    #continuously do this:
	    cvturtle.rt(11.1111)            
	    cvturtle.fd(200)     
	    cvturtle.rt(61)
	    cvturtle.fd(200)
	    cvturtle.rt(61)
	    cvturtle.fd(200)
	    cvturtle.rt(61)
	    cvturtle.fd(200)
	    cvturtle.rt(61)
	    cvturtle.fd(200)
	    cvturtle.rt(61)
	    cvturtle.fd(200)
	    cvturtle.rt(61)
	
	    cvturtle.rt(90.911)
	    r = randint(0,255)
	    g = randint(0,255) 
	    b = randint(0,255)
	


	    cvturtle.pencolor(r,g,b) 

	    cvturtle.fd(50 + x)
	    x = x+1 
	return 
