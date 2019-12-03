from random import randrange as rnd, choice
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x650')
canv = tk.Canvas(root, bg='pink')
canv.pack(fill=tk.BOTH, expand=1)
w = 5

def create_objects():
    canv.create_oval (100, 25, 700, 625, outline="gray", fill="red", width=2)
    a = 5
    canv.create_oval (400-a, 325-a, 400+a, 325+a, fill="blue", width=2)
    
    
class Player():
    
    def __init__(self):
        
        self.x = 400
        self.y = 325
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.a = 20
        self.vx = 10
        self.vy = 10
        
        self.id = canv.create_rectangle(
                self.x - self.a,
                self.y - self.a,
                self.x + self.a,
                self.y + self.a,
                fill=self.color
        )
        
        
    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.a,
            self.y - self.a,
            self.x + self.a,
            self.y + self.a
        )
    
    
    def move_right(self, event):            
        self.x += self.vx
        self.set_coords()
        
        
    def move_left(self, event):
        self.x -= self.vx
        self.set_coords()
        
        
    def move_up(self, event):
        self.y -= self.vy
        self.set_coords()
        
        
    def move_down(self, event):
        self.y += self.vy
        self.set_coords()
        
"""class encircling():
    def __init__(self):
        dot.id = canv.create_oval (400-a, 325-a, 400+a, 325+a, fill="black", width=2)
        
    def move_encircling():
        #dot.id = canv.create_oval (400-a, 325-a, 400+a, 325+a, fill="black", width=2)
        dot.vx = w*dot.x
        dot.vy = w*dot.y"""
class ball():
    def __init__(self, x=40, y=450):
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 180

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        if self.x+self.vx>=780 or self.x+self.vx<=15:
            self.vx = -self.vx
        if self.y - self.vy >= 580 or self.y - self.vy <= 15:
            self.vy = -self.vy
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        self.live -= 1

    def hittest(self, obj):
        if (self.x-obj.x)**2+(self.y-obj.y)**2<=(self.r+obj.r)**2:
            return True
        else:
            return False
            
            
def game_process(event=''):
    
    
    root.bind('<Right>', P1.move_right)
    root.bind('<Left>', P1.move_left)
    root.bind('<Up>', P1.move_up)
    root.bind('<Down>', P1.move_down)
    
    root.after(750, game_process)
    
create_objects()
         
P1 = Player()

game_process()



root.mainloop()
