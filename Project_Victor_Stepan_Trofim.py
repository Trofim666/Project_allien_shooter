from random import randrange as rnd, choice
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x650')
canv = tk.Canvas(root, bg='pink')
canv.pack(fill=tk.BOTH, expand=1)
k_x = 1
k_y = 1
M = 1
dt = 0.01
w = 5


def create_objects():
    canv.create_oval (100, 25, 700, 625, outline="gray", fill="red", width=2)
    a = 5
    canv.create_oval (400-a, 325-a, 400+a, 325+a, fill="blue", width=2)


class Ball():
    def __init__(self, x=400, y=325):
        
        self.x = x
        self.y = y
        self.r = 2
        self.vx = 40
        self.vy = 40
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
        

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()    


class Player():
    
    def __init__(self, ):
        self.f2_power = 20
        self.f2_on = 0
        self.x = 400
        self.y = 325
        
        
        self.ay = 0
        self.ax = 0
        self.xc = 400
        self.yc = 325
        self.m = 10
        self.F = self.m*M*0.1
        
        self.an = 1
        #self.color = choice(['blue', 'green', 'yellow', 'brown'])
        self.a1 = 30
        self.a2 = 15
        self.vx = 0
        self.vy = 1
        self.v = math.sqrt(self.vx**2 + self.vy**2)
        self.l = 50
        self.id1 = canv.create_oval(
                self.x - self.a1,
                self.y - self.a1,
                self.x + self.a1,
                self.y + self.a1,
                fill='blue'
        )
        
        self.id3 = canv.create_line(self.x, self.y ,self.x, self.y - self.l, width=6)
        
        self.id2 = canv.create_oval(
                self.x - self.a2,
                self.y - self.a2,
                self.x + self.a2,
                self.y + self.a2,
                fill='yellow'
        )
        
    def set_coords2(self):
        canv.coords(
            self.id2,
            self.x - self.a2,
            self.y - self.a2,
            self.x + self.a2,
            self.y + self.a2
        )
    
    def set_coords1(self):
        canv.coords(
            self.id1,
            self.x - self.a1,
            self.y - self.a1,
            self.x + self.a1,
            self.y + self.a1
        )
    
    
    def set_coords3(self):
        global k_x, k_y
        
        canv.coords(
            self.id3,
            self.x,
            self.y,
            self.x + self.l*k_x,
            self.y + self.l*k_y
        )


    def fire2_start(self, event):
        self.f2_on = 1


    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.y-new_ball.y) , (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0

        
        
    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        global k_x, k_y
        
        if event:
            self.an = math.atan2((event.y-self.y) , (event.x-self.x))
            canv.coords(self.id3, 
                    self.x, 
                    self.y,
                    self.x + self.l*math.cos(self.an),
                    self.y + self.l*math.sin(self.an)
                    )
        k_x = math.cos(self.an)
        k_y = math.sin(self.an)
        
        
        
    def acceleration(self, event=0):
        global k_x, k_y
        #sina = (self.y-self.yc)/math.sqrt( (self.x-self.xc)**2 + (self.y-self.yc)**2   )
        #cosa =(self.x-self.xc)/math.sqrt( (self.x-self.xc)**2 + (self.y-self.yc)**2  ) 
        #self.ax = self.F*k_x/self.m + k_x * 2*w*self.vy + w**2*(self.x-self.xc)
        #self.ay = self.F*k_y/self.m + k_y * 2*w*self.vx + w**2*(self.y-self.yc)
        self.ax =  k_x * 2*w*self.vy + (w**2)*(self.x-self.xc)
        self.ay = k_y * 2*w*self.vx + (w**2)*(self.y-self.yc)
        self.vx +=self.ax*dt 
        self.vy +=self.ay*dt
    def move(self):
        global k_x, k_y
        #self.x += -k_y*self.v
        #self.y += k_x*self.v
        self.x+=self.vx*0.001
        self.y+=self.vy*0.001
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
    def move_right(self, event):  
        global k_x, k_y
        self.x += -k_y*self.v
        self.y += k_x*self.v
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
        
        
    def move_left(self, event):
        global k_x, k_y
        self.x += k_y*self.v
        self.y += -k_x*self.v
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
        
    def move_up(self, event):
        global k_x, k_y
        self.vx+=self.F*k_x/self.m
        self.vy+=self.F*k_y/self.m
        #self.x += k_x*self.v
        #self.y += k_y*self.v
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
        
    def move_down(self, event):
        global k_x, k_y
        
        self.x += -k_x*self.v
        self.y += -k_y*self.v
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()

balls = []
bullet = 0

def game_process(event=''):
    global balls, bullet
    root.bind('<Button-1>', P1.fire2_start)
    root.bind('<ButtonRelease-1>', P1.fire2_end)
    root.bind('<Motion>', P1.targetting)
    root.bind('<Right>', P1.move_right)    
    root.bind('<Left>', P1.move_left)
    root.bind('<Up>', P1.move_up)
    root.bind('<Down>', P1.move_down)
    for b in balls:
            b.move()
    canv.update()
    P1.move()
    P1.acceleration()
    P1.targetting()
    #time.sleep(0.03)
    
    root.after(20, game_process)
    
create_objects()
         
P1 = Player()

game_process()



root.mainloop()
