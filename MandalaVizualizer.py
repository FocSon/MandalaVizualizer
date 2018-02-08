#!/usr/bin/python2.7
from libMandala import *
from Tkinter import *
import tkFont 
import turtle 
from random import randint

def play(bg):
	button.destroy()
	while True : 
		mandala = randint(0, 6) 
		clearCanvas = randint(0, 1)
		if mandala == 0:
			randmandala1(bg)
		if mandala == 1:
			randmandala2(bg)
		if mandala == 2:
			seashell(randint(0, bg.winfo_width()),randint(0, bg.winfo_height())*-1,bg)
		if mandala == 3:
			rotatesqrt(bg)
		if mandala == 4:
			wtf3d(bg)
		if mandala == 5:
			trippystar(bg)
		if mandala == 6:
			enhancedMandala(bg)
		if clearCanvas == 1:
			bg.delete("all")
	return

#create the windows and all the widgets 
fenetre = Tk()
fenetre.attributes("-fullscreen", 1)
fenetre.title("MandalaVizualizer")
MandalaVizualizerLogo = PhotoImage(file="./logo.gif")
logoLabel = Label(image=MandalaVizualizerLogo)
logoLabel.image = MandalaVizualizerLogo #keeping a reference in this line
fontOfPlayButton = tkFont.Font(family="DejaVu Serif", size=100, weight="bold")
fontOfExitButton = tkFont.Font(family="Nimbus Sans L", size=20, weight="bold")
background = Canvas(fenetre, width=fenetre.winfo_width(), height= fenetre.winfo_height(), bg='black', highlightthickness=0)
button = Button(background, text="Play", command= lambda: play(background),font=fontOfPlayButton)
buttonExit = Button(background, text="Exit", command=fenetre.destroy, font=fontOfExitButton)
button.config(foreground="white", background="black")
buttonExit.config(foreground="white", background="black")

#place widgets on the windows 


buttonExit.pack(side="bottom")
background.pack(fill='both', expand=1)
spreadstars(background)
background.create_image(background.winfo_width()/2, background.winfo_height()/2, image=MandalaVizualizerLogo)
button.pack(side="bottom") 

fenetre.mainloop()

  

    
