from random import randrange as rnd, choice
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x650')
canv = tk.Canvas(root, bg='pink')
canv.pack(fill=tk.BOTH, expand=1)


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
    
    
    def move_right(self):            
        self.x += self.vx
        self.set_coords()
        
        
    def move_left(self):
        self.x -= self.vx
        self.set_coords()
        
        
    def move_up(self):
        self.y -= self.y
        self.set_coords()
        
        
    def move_down(self):
        self.x += self.vx
        self.set_coords()
            
            
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