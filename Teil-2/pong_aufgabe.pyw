#!/usr/bin/python3
#----------------------------------------------------------------
# Dateiname: pong.pyw
# Pongspiel
# Ein Schläger wird mit Pfeiltasten gesteuert, der andere von einer KI
#
# Michael Weigend
# KI-Workshop
# 
# Michael Weigend 20. Mai 2024
#--------------------------------------------------------------
from tkinter import *
import random

STEP = 50   # Millisekunden

class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.img = PhotoImage(file='ball.gif')                   
        self.iD = self.canvas.create_image(0, 0, image=self.img)
        self.start()

    def start(self):
        x = int(self.canvas['width'])/2
        self.canvas.coords(self.iD, x, 1)                        
        self.vy = 3                                             
        self.vx = random.choice([-3, 3])                              

    def bounce(self):
        if self.vx > 0:                                          
            self.vx = -self.vx -1
        else:
            self.vx = -self.vx +1
        self.canvas.move(self.iD, self.vx, self.vy)              
        
    def tick(self):                                              
        x, y = self.canvas.coords(self.iD)
        if 0 < int(x) < int(self.canvas['width']):               
            self.canvas.move(self.iD, self.vx, self.vy)
            x, y = self.canvas.coords(self.iD)
            if not(0 < int(y) < int(self.canvas['height'])):
                self.vy = - self.vy                              
        else:          
            self.start()                                         

class Bat:
    def __init__(self, canvas, ball, x):
        self.canvas, self.ball = canvas, ball
        self.img = PhotoImage(file='bat.gif')
        self.iD = self.canvas.create_image(x, 0,
                               anchor=NW, image=self.img)
        

    def up(self, event):
        self.canvas.move(self.iD, 0, -5)

    def down(self, event):
        self.canvas.move(self.iD, 0, 5)

    def tick(self):
        x1, y1, x2, y2  = self.canvas.bbox(self.iD)
        if self.ball.iD in \
           self.canvas.find_overlapping(x1, y1, x2, y2):
            self.ball.bounce()                                                           

class BatAI:
    def __init__(self, canvas, ball, x):
        self.canvas, self.ball,  = canvas, ball
        self.img = PhotoImage(file='bat.gif')
        self.iD = self.canvas.create_image(x, 220,
                             anchor=NW, image=self.img)

    def tick(self):
        x1, y1, x2, y2  = self.canvas.bbox(self.iD)
        ballX, ballY = self.canvas.coords(self.ball.iD)
        middle = (y1 + y2) // 2          # Mitte des Schlägers                     
        #  Schläger bewegen 
        if self.ball.iD in \
           self.canvas.find_overlapping(x1, y1, x2, y2):
            self.ball.bounce()


class Pong:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(master=self.window, bg="black", 
                             width=800, height=450)
        self.canvas.pack()
        self.ball = Ball(self.canvas)
        self.leftBat = Bat(self.canvas, self.ball, 20)
        self.rightBat = BatAI(self.canvas, self.ball, 760)
        self.window.bind('<KeyPress-Up>',self.leftBat.up)
        self.window.bind('<KeyPress-Down>',self.leftBat.down)
        self.window.after(STEP, self.tick)
        self.window.mainloop()

    def tick(self):                                            
        self.ball.tick()
        self.leftBat.tick()
        self.rightBat.tick()
        self.window.after(STEP, self.tick)                       
        
        
Pong()  
  
