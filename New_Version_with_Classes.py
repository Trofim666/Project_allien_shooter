from math import sqrt
from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import graphics as gr
import mp3play


enemys=[]
enemys_agressive=[]
grenades=[]
balls=[]
boxes = []
medes = []

class Game():
    
    def __init__(self):
    
        self.all_points = 0
        self.hp = 100
        self.x_hp = 200
        self.gren = 5
        self.bull = 15
        self.i_max = 6
        self.i_max_agressive = 0
        self.level = 1
        
        self.trigger=0
        
        self.t_med = 20000
        self.t0_med = 0
        self.t_box = 20000
        self.t0_box = 14000
        
        self.deltav = 10
        self.boundv = 0.1
        
        self.streak = 0
    
        self.k_x = 1
        self.k_y = 1 
        self.i=0
        self.k=0
        self.x_0 = 100
        self.y_0 = 25
        self.R = 300
        self.a = 200
        self.M = 1
        self.dt = 1
        self.w = 0.002
        self.yc = 325
        self.xc = 400
        self.a_box = 20
        self.b_box = 40


class Ball():
    
    def __init__(self, x=400, y=325):
        
        
        
        
        self.x = x
        self.y = y
        self.r = 3
        
        

        self.live = 40
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


class Grenade():
    
    def __init__(self, x=400, y=325):
        self.Rexp = 10
        self.r0 = 3
        self.bangtime = 4
        self.x = x
        self.y = y
        self.r = 5
        self.e = 3
        self.live = 40
        self.vx = 40
        self.vy = 40
        self.color =['purple']
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
        
    
    def blowup(self):
        for i in range(self.bangtime):
            self.r0+=self.Rexp
            boom = canv.create_oval(
                self.x - self.r0,
                self.y - self.r0,
                self.x + self.r0,
                self.y + self.r0,
                fill='orange'
            )
            canv.update()
            time.sleep(0.06)
            canv.delete(boom)
            
        


class Player():
    
    def __init__(self):
        self.f2_power = 20
        self.x = 400
        self.y = 325
        self.live = 100
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
        self.vy = 0
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


        
    def check_minus_hp(self):
        global enemys, hp, x_hp,  id_hp, trigger, screen1
        
        for e in enemys:
            if (e['x'] - self.x)**2 + (e['y'] - self.y)**2 <= (self.a1 + e['r'])**2:
                self.live -= 1
                hp -= 1
                x_hp -= 2
                canv.itemconfig(id_hp_percents, text = str(hp) + '%')
                canv.delete(id_hp)
                id_hp = canv.create_rectangle(10, 45, x_hp, 75, fill='green', width = 2)
        
        for e in enemys_agressive:
            if (e['x'] - self.x)**2 + (e['y'] - self.y)**2 <= (self.a1 + e['r'])**2:
                self.live -= 1
                hp -= 1
                x_hp -= 2
                canv.itemconfig(id_hp_percents, text = str(hp) + '%')
                canv.delete(id_hp)
                id_hp = canv.create_rectangle(10, 45, x_hp, 75, fill='green', width = 2) 
        
        
        if self.live <= 0 or (self.x - self.xc)**2 + (self.y - self.yc)**2 >= R**2:
            start_new_game()


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
        global balls, bull
        if bull > 0:
            new_ball = Ball(self.x, self.y)
            new_ball.r += 5
            bull-=1
            self.an = math.atan2((event.y-new_ball.y) , (event.x-new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
            self.vx+= -boundv*math.cos(self.an)
            self.vy+= -boundv*math.sin(self.an)
            balls += [new_ball]
        elif bull == 0:
            clip_no_bull.play()

    def fire1_start(self, event):
        global grenades, gren
        if gren > 0:
            new_gr = Grenade(self.x, self.y)
            new_gr.r += 5
            gren -=1
            self.an = math.atan2((event.y-new_gr.y) , (event.x-new_gr.x))
            new_gr.vx = self.f2_power * math.cos(self.an)
            new_gr.vy = - self.f2_power * math.sin(self.an)
            grenades += [new_gr]
        elif gren == 0:
            clip_no_gren.play()
 
    def targetting(self, event=0):
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
        
        
    def acceleration(self):
        global k_x, k_y
        #sina = (self.y-self.yc)/math.sqrt( (self.x-self.xc)**2 + (self.y-self.yc)**2   )
        #cosa =(self.x-self.xc)/math.sqrt( (self.x-self.xc)**2 + (self.y-self.yc)**2  ) 
        #self.ax = self.F*k_x/self.m + k_x * 2*w*self.vy + w**2*(self.x-self.xc)
        #self.ay = self.F*k_y/self.m + k_y * 2*w*self.vx + w**2*(self.y-self.yc)
        self.ax =  -2*w*self.vy + (w**2)*(self.x-self.xc)
        self.ay =  2*w*self.vx +(w**2)*(self.y-self.yc)
        self.vx +=self.ax*dt 
        self.vy +=self.ay*dt
        self.v = math.sqrt(self.vx**2 + self.vy**2)
        
        
    def move(self):
        global k_x, k_y
        #self.x += -k_y*self.v
        #self.y += k_x*self.v
        self.x+=self.vx#*0.1
        self.y+=self.vy#*0.1
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
        
        
    def move_right(self, event):  
        global k_x, k_y

        self.vx+=-self.F*k_x/self.m
        self.vy+=self.F*k_y/self.m

        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
        
        
    def move_left(self, event):
        global k_x, k_y

        self.vx+=self.F*k_x/self.m
        self.vy+=-self.F*k_y/self.m

        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
        
        
    def move_up(self, event):
        global k_x, k_y
        
        self.vx+=self.F*k_x/self.m
        self.vy+=self.F*k_y/self.m
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
        
        
    def move_down(self, event):
        global k_x, k_y
        

        self.vx+=-self.F*k_x/self.m
        self.vy+=-self.F*k_y/self.m

        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
        
    
    