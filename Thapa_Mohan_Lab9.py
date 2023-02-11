"""
Author: Mohan Thapa
CSC 131 lab 7
"""

from tkinter import *
import random

class Pong(Frame):
    COLORS=['yellow','green','red','black','purple','pink','khaki','orange','indigo','gray','khaki']
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Bouncing Ball")
        self.grid()
        canvas_width = 800  
        canvas_height = 400 
        self.canvas = Canvas(self, width = canvas_width, height = canvas_height , bg = "white")
        self.canvas.grid()

        
        ball_diameter = 20 
        top_left_x = 2  
        top_left_y = 2
        self.canvas.create_oval(top_left_x, top_left_y, top_left_x + ball_diameter,
                                top_left_y + ball_diameter, fill = "red", tags = "ball")
        
        directiony = "down" 
        directionx = 'left'
        dy = 4
        dx =2

       
        while True:
            
            if directiony == "down" and directionx == "left":
                self.canvas.move("ball", dx, dy)
                top_left_y += dy
                top_left_x +=dx
                if top_left_y + ball_diameter >= canvas_height : 
                    directiony = "up"
                    self.canvas.itemconfig('ball',fill = random.choice(Pong.COLORS))
                if top_left_x +ball_diameter >=canvas_width:
                    directionx ='right'
                    self.canvas.itemconfig('ball',fill = random.choice(Pong.COLORS))

            elif directiony == "down" and directionx == "right":
                self.canvas.move("ball", -dx, dy)
                top_left_y += dy
                top_left_x -=dx
                if top_left_y + ball_diameter >= canvas_height : 
                    directiony = "up"
                    self.canvas.itemconfig('ball',fill = random.choice(Pong.COLORS))
                if top_left_x +ball_diameter <=15:
                    directionx ='left'
                    self.canvas.itemconfig('ball',fill = random.choice(Pong.COLORS))

            elif directiony == "up" and directionx == "left":
                self.canvas.move("ball", dx, -dy)
                top_left_y -= dy
                top_left_x +=dx
                if top_left_y + ball_diameter <= 15 : 
                    directiony = "down"
                    self.canvas.itemconfig('ball',fill = random.choice(Pong.COLORS))
                if top_left_x +ball_diameter >=canvas_width:
                    directionx ='right'
                    self.canvas.itemconfig('ball',fill = random.choice(Pong.COLORS))

            else:
                self.canvas.move("ball", -dx, -dy)
                top_left_y -= dy
                top_left_x -=dx
                if top_left_y + ball_diameter <= 15 :
                    directiony = "down"
                    self.canvas.itemconfig('ball',fill = random.choice(Pong.COLORS))
                if top_left_x +ball_diameter <=15:
                    directionx ='left'
                    self.canvas.itemconfig('ball',fill = random.choice(Pong.COLORS))
                

                
   
            
                
            

            
                
            self.canvas.after(15) 
            self.canvas.update() 

def main():
    Pong().mainloop()

main()
