from math import sqrt
from random import randrange as rnd, choice
import tkinter as tk
import math
import time


WINDOW_SIZE = (800, 650)

xc = 400
yc = 325
dt = 1
a = 200
R = 300
name = None


enemys3 = []
enemys=[]
enemys2 = []
grenades=[]
balls=[]
boxes = []
medes = []
scores = []
text = None

def pass_event():
    pass


class Ball():
    def __init__(self, canvas, x, y):

        self.canvas = canvas
        self.x = x
        self.y = y

        self.r = 3

        self.vx = 15
        self.vy = 15

        self.color = choice(['blue', 'green', 'red', 'brown'])


        self.id = self.canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

        self.live = 40

    def set_coords(self):
        self.canvas.coords(
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
    def __init__(self, canvas, x, y):

        self.canvas = canvas
        self.time = time
        self.r = 3
        self.bangtime = 4
        self.x = x
        self.y = y
        self.Rexp = 20
        self.live = 40

        self.vx = 10
        self.vy = 10
        self.color =['purple']

        self.id = self.canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )



    def set_coords(self):
        self.canvas.coords(
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
    def __init__(self, canvas):

        #self.game = Game()

        self.canvas = canvas
        self.w = 0.002
        
        self.id_level = self.canvas.create_text(730,590,text = 'Difficulty: Default',font = '28')
        
        self.i_max = 8
        
        self.boundv = 0.1

        self.x = xc
        self.y = yc

        self.k_x = 1
        self.k_y = 1

        self.hp = 100
        self.x_hp = 200

        self.t0_med = 17
        self.t_med = 20
        self.id_med_time = self.canvas.create_text(725,110,text = '00:00',font = '28') 
        
        self.t0_box = 15
        self.t_box = 20
        self.id_box_time = self.canvas.create_text(725,150,text = '00:00',font = '28')

        self.x_box = rnd(260,540)
        self.y_box = rnd(185,465)

        self.a_box = 20
        self.b_box = 40


        self.ay = 0
        self.ax = 0

        self.m = 10
        self.F = 1
        
        self.an = 1

        self.R1 = 30
        self.R2 = 15

        self.vx = 0
        self.vy = 0

        self.v = math.sqrt(self.vx**2 + self.vy**2)

        self.l = 50
        self.bull = 15
        self.gren = 5

        self.id1 = canvas.create_oval(
                self.x - self.R1,
                self.y - self.R1,
                self.x + self.R1,
                self.y + self.R1,
                fill='blue'
        )

        self.id3 = canvas.create_line(self.x, self.y ,self.x, self.y - self.l, width=6)

        self.id2 = canvas.create_oval(
                self.x - self.R2,
                self.y - self.R2,
                self.x + self.R2,
                self.y + self.R2,
                fill='yellow'
        )


    def start(self):
        self.bind_all()


    def set_coords1(self):
        self.canvas.coords(
            self.id1,
            self.x - self.R1,
            self.y - self.R1,
            self.x + self.R1,
            self.y + self.R1
        )


    def set_coords2(self):
        self.canvas.coords(
            self.id2,
            self.x - self.R2,
            self.y - self.R2,
            self.x + self.R2,
            self.y + self.R2
        )

#в targetting разве не задается уже положение пушки? см таргетинг
    def set_coords3(self):
        self.canvas.coords(
            self.id3,
            self.x,
            self.y,
            self.x + self.l*self.k_x,
            self.y + self.l*self.k_y
        )


    def fire_bull_start(self, event):
        global balls
        if self.bull > 0:
            new_ball = Ball(self.canvas, self.x, self.y)
            new_ball.r += 5
            self.bull-=1
            new_ball.vx = new_ball.vx * math.cos(self.an)
            new_ball.vy = - new_ball.vy * math.sin(self.an)
            self.vx+= -self.boundv*math.cos(self.an)
            self.vy+= -self.boundv*math.sin(self.an)
            balls += [new_ball]
        #elif self.bull == 0:
            #clip_no_bull.play()

    def fire_gren_start(self, event):
        global grenades
        if self.gren > 0:
            new_gr = Grenade(self.canvas, self.x, self.y)
            new_gr.r += 5
            self.gren -=1
            self.an = math.atan2((event.y-new_gr.y) , (event.x-new_gr.x))
            new_gr.vx = new_gr.vx * math.cos(self.an)
            new_gr.vy = - new_gr.vy * math.sin(self.an)
            grenades += [new_gr]
        #elif self.gren == 0:
            #clip_no_gren.play()

#Что значит event=0? зачем вообще нужен event если мы в bind all см ниже уже говорим на какую кнопку запускается функция?
# Почему здесь просто не прописать setcoords3?
    def targetting(self, event=0):
        if event:
            self.an = math.atan2((event.y-self.y) , (event.x-self.x))
            self.canvas.coords(self.id3, 
                    self.x, 
                    self.y,
                    self.x + self.l*math.cos(self.an),
                    self.y + self.l*math.sin(self.an)
                    )
        self.k_x = math.cos(self.an)
        self.k_y = math.sin(self.an)
        
        
    def acceleration(self):
        #sina = (self.y-self.yc)/math.sqrt( (self.x-self.xc)**2 + (self.y-self.yc)**2   )
        #cosa =(self.x-self.xc)/math.sqrt( (self.x-self.xc)**2 + (self.y-self.yc)**2  ) 
        #self.ax = self.F*k_x/self.m + k_x * 2*w*self.vy + w**2*(self.x-self.xc)
        #self.ay = self.F*k_y/self.m + k_y * 2*w*self.vx + w**2*(self.y-self.yc)
        self.ax =  -2*self.w*self.vy + (self.w**2)*(self.x-xc)
        self.ay =  2*self.w*self.vx +(self.w**2)*(self.y-yc)
        self.vx +=self.ax*dt 
        self.vy +=self.ay*dt
        self.v = math.sqrt(self.vx**2 + self.vy**2)


    def move(self):
        #global k_x, k_y
        #self.x += -k_y*self.v
        #self.y += k_x*self.v
        self.x+=self.vx#*0.1
        self.y+=self.vy#*0.1
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
    def move_right(self, event):
        self.vx+=-self.F*self.k_y/self.m
        self.vy+=self.F*self.k_x/self.m
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
    def move_left(self, event):
        self.vx+=self.F*self.k_y/self.m
        self.vy+=-self.F*self.k_x/self.m
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
    def move_up(self, event):
        self.vx+=self.F*self.k_x/self.m
        self.vy+=self.F*self.k_y/self.m
        #self.x += k_x*self.v
        #self.y += k_y*self.v
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
    def move_down(self, event):
        self.vx+=-self.F*self.k_x/self.m
        self.vy+=-self.F*self.k_y/self.m
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
# зачем нужен pass , по другому кнопки не сделать?
    def pass_event(self, event):
        pass
    
    def new_box(self):
        global boxes
        if (self.x_box - xc)**2 + (self.y_box - yc)**2 <= a**2:
            self.id_box = self.canvas.create_rectangle(self.x_box, self.y_box, self.x_box + self.a_box, self.y_box + self.b_box, fill='green', width=2)
            self.box={'id': self.id_box, 'x': self.x_box, 'y': self.y_box}
            boxes.append(self.box)


    def new_aptechka(self):
        global medes
        if (self.x_box - xc)**2 + (self.y_box - yc)**2 <= a**2:
            self.id_med = self.canvas.create_rectangle(self.x_box, self.y_box, self.x_box + self.a_box, self.y_box + self.b_box, fill='aqua', width=2)
            self.med={'id': self.id_med, 'x': self.x_box, 'y': self.y_box}
            medes.append(self.med)


    def time_of_medicaments(self):
        self.t0_med+=1
        self.canvas.delete(self.id_med_time)
        if self.t_med - self.t0_med >= 10:
            self.id_med_time = self.canvas.create_text(725,150,text = '00:' + str(self.t_med-self.t0_med), font = '32')
        elif self.t_med - self.t0_med > 0:
            self.id_med_time = self.canvas.create_text(725,150,text = '00:0' + str(self.t_med-self.t0_med), font = '32')
        elif self.t_med - self.t0_med == 0:
            self.t0_med = 0
            self.id_med_time = self.canvas.create_text(725,150,text = '00:00', font = '32')
            self.new_aptechka()


    def time_of_boxes(self):
        self.t0_box+=1
        self.canvas.delete(self.id_box_time)
        if self.t_box - self.t0_box >= 10:
            self.id_box_time = self.canvas.create_text(725,110,text = '00:' + str(self.t_box-self.t0_box), font = '32')
        elif self.t_box - self.t0_box > 0:
            self.id_box_time = self.canvas.create_text(725,110,text = '00:0' + str(self.t_box-self.t0_box), font = '32')
        elif self.t_box - self.t0_box == 0:
            self.t0_box = 0
            self.id_box_time = self.canvas.create_text(725,110,text = '00:00', font = '32')
            self.new_box()

    def stop(self):
        self.unbind_all()
    
    def unbind_all(self):
        root = self.canvas.get_root()

        root.bind('<Right>', self.pass_event)    
        root.bind('<Left>', self.pass_event)
        root.bind('<Up>', self.pass_event)
        root.bind('<Down>', self.pass_event)

        root.bind('<Motion>', self.pass_event)
        root.bind('<Button-1>', self.pass_event)
        root.bind('<Button-3>', self.pass_event)
    
    def bind_all(self):
        root = self.canvas.get_root()
        root.bind('<Motion>', self.targetting)
        root.bind('<Right>', self.move_right)    
        root.bind('<Left>', self.move_left)
        root.bind('<Up>', self.move_up)
        root.bind('<Down>', self.move_down)
        root.bind('<Button-1>', self.fire_bull_start)
        root.bind('<Button-3>', self.fire_gren_start)


class Enemy():
    def __init__(self, canvas):
              
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(10, 15)
        self.w = 0.003 
        self.e_max = 5
        self.e2_max = 3
        
        self.x2 = rnd(100, 700)
        self.y2 = rnd(100, 500)
        self.r2 = rnd(10, 15)
        self.r3 = 7
        self.t = 40
        #self.vx2 = rnd(-1, 1)
        #self.vy2 = rnd(-1, 1)
        
        
        #self.vx = rnd(-6, 6)
        #self.vy = rnd(-6, 6)
        
        
        self.vx2 = 0
        self.vy2 = 0
        
        self.vx = 0
        self.vy = 0
        
        self.enemys = 0
        self.enemys3 = 0
        self.enemys2 = 0
#!что такое canvas где он находится 
        self.canvas = canvas

    
    def define_max_num(self, P):
        self.e_max = P.i_max
        self.w = P.w
    
    def get_r_vector_x(self, x, y):
        self.length_vector = sqrt((xc-x)**2 + (yc-y)**2)
        self.radius_vector_x = (xc-x) / self.length_vector
        return self.radius_vector_x


    def get_r_vector_y(self, x, y):
        self.length_vector = sqrt((xc-x)**2 + (yc-y)**2)
        self.radius_vector_y = (yc-y) / self.length_vector
        return self.radius_vector_y


    def get_normal_x(self, x, y):
        self.length_vector = sqrt((xc-x)**2 + (yc-y)**2)
        self.normal_vector_x = (yc-y) / self.length_vector
        return self.normal_vector_x


    def get_normal_y(self, x, y):
        self.length_vector = sqrt((xc-x)**2 + (yc-y)**2)
        self.normal_vector_y = -(xc-x) / self.length_vector
        return self.normal_vector_y


    def scalar_multiplication(self, vector_1_x, vector_1_y, vector_2_x, vector_2_y):
        self.scalar = vector_1_x*vector_2_x + vector_1_y*vector_2_y
        return self.scalar


    def change_velocity_vx(self, vx, vy, x, y):
        self.vel_normal_0_x = self.get_r_vector_x(x,y)*self.scalar_multiplication(self.get_r_vector_x(x,y), self.get_r_vector_y(x,y),vx, vy)

        self.vel_normal_0_y = self.get_r_vector_y(x,y)* self.scalar_multiplication(self.get_r_vector_x(x,y), self.get_r_vector_y(x,y),vx, vy)


        self.vel_tau_x = self.get_normal_x(x,y)* self.scalar_multiplication(self.get_normal_x(x,y), self.get_normal_y(x,y),vx, vy)

        self.vel_tau_y = self.get_normal_y(x,y)* self.scalar_multiplication(self.get_normal_x(x,y), self.get_normal_y(x,y),vx, vy)


        self.i_x = 1
        self.i_y = 0

        self.vel_1_x = self.scalar_multiplication(-self.vel_normal_0_x, -self.vel_normal_0_y, self.i_x, self.i_y)
        self.vel_2_x = self.scalar_multiplication(self.vel_tau_x, self.vel_tau_y, self.i_x, self.i_y)
        self.vx = self.vel_1_x + self.vel_2_x
        
        return self.vx


    def change_velocity_vy(self, vx, vy, x, y):

        self.vel_normal_0_x = self.get_r_vector_x(x,y)*self.scalar_multiplication(self.get_r_vector_x(x,y), self.get_r_vector_y(x,y),vx, vy)

        self.vel_normal_0_y = self.get_r_vector_y(x,y)* self.scalar_multiplication(self.get_r_vector_x(x,y), self.get_r_vector_y(x,y),vx, vy)


        self.vel_tau_x = self.get_normal_x(x,y)* self.scalar_multiplication(self.get_normal_x(x,y), self.get_normal_y(x,y),vx, vy)

        self.vel_tau_y = self.get_normal_y(x,y)* self.scalar_multiplication(self.get_normal_x(x,y), self.get_normal_y(x,y),vx, vy)


        self.j_x = 0
        self.j_y = 1
        
        self.vel_1_y = self.scalar_multiplication(-self.vel_normal_0_x, -self.vel_normal_0_y, self.j_x, self.j_y)
        self.vel_2_y = self.scalar_multiplication(self.vel_tau_x, self.vel_tau_y, self.j_x, self.j_y)
        
        self.vy = self.vel_1_y + self.vel_2_y
        
        return self.vy


    def new_enemy(self):
        
        if (self.x - xc)**2 + (self.y - yc)**2 >= a**2 and (self.x - xc)**2 + (self.y - yc)**2 <= (R-40)**2 and self.enemys < self.e_max:
            self.id_ = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,fill = 'black', width=0, activefill = 'green')
            self.enemy={'id': self.id_, 'x': self.x, 'y': self.y, 'r': self.r, 'vx': self.vx, 'vy': self.vy}
            self.enemys+=1
            enemys.append(self.enemy)
                
    def new_enemy2(self):
            
        if (self.x2 - xc)**2 + (self.y2 - yc)**2 >= a**2 and (self.x2 - xc)**2 + (self.y2 - yc)**2 <= (R-40)**2 and self.enemys2 < self.e2_max:
            self.id2 = self.canvas.create_oval(self.x2 - self.r2, self.y2 - self.r2, self.x2 + self.r2, self.y2 + self.r2,fill = 'blue', width=0, activefill = 'green')
            self.enemy2={'id': self.id2, 'x': self.x2, 'y': self.y2, 'r': self.r2, 'vx': self.vx2, 'vy': self.vy2}
            self.enemys2+=1
            enemys2.append(self.enemy2)
    def new_enemy3(self, x, y, vx, vy):
            
        #if (x - xc)**2 + (y - yc)**2 >= a**2 and (x - xc)**2 + (y - yc)**2 <= (R-40)**2 :
        if (x - xc)**2 + (y - yc)**2 <= (R-40)**2 :
            self.id3 = self.canvas.create_oval(x - self.r3, y - self.r3, x + self.r3, y + self.r3,fill = 'gold', width=0, activefill = 'green')
            self.enemy3={'id': self.id3, 'x': x, 'y': y, 'r': self.r3, 'vx': vx, 'vy': vy, 't':self.t}
            self.enemys3+=1
            enemys3.append(self.enemy3)

    def motion(self):
        for e in enemys:
            e['vx']+= ( -2*self.w*e['vy'] + (self.w**2)*(-xc + e['x'])  )*dt
            e['vy']+= ( +2*self.w*e['vx'] + (self.w**2)*(-yc + e['y'])  )*dt
            if (xc - e['x'])**2 + (yc - e['y'])**2 >= (R-e['r'])**2:
                v_x = self.change_velocity_vx(e['vx'], e['vy'], e['x'], e['y'])
                v_y = self.change_velocity_vy(e['vx'], e['vy'], e['x'], e['y'])
                e['vx'] = v_x
                e['vy'] = v_y
            e['x']+=e['vx']
            e['y']+=e['vy']
            self.canvas.move(e['id'], e['vx'], e['vy'])
    
    def motion2(self, P):
        for e in enemys2:
            v = sqrt(e['vx']**2 + e['vy']**2)
            sina = (P.y - e['y'])/sqrt((P.x-e['x'])**2 + (P.y - e['y'])**2 )
            cosa = (P.x - e['x'])/sqrt((P.x-e['x'])**2 + (P.y - e['y'])**2 )
            e['vx'] = v*cosa
            e['vy'] = v*sina
            e['x']+=e['vx']
            e['y']+=e['vy']
            self.canvas.move(e['id'], e['vx'], e['vy'])

    def motion3(self):
        for e in enemys3:
            e['x']+=e['vx']
            e['y']+=e['vy']
            self.canvas.move(e['id'], e['vx'], e['vy'])

class BattleField(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, background='pink')

        self.dedected_restart = False
        self.select=0
        self.k_func = 0
        
        self.trigger = 0
        self.screen1 = self.create_text(400, 300, text='', font = "Times 100 italic bold")
        self.max = None
        self.r = 5
        #!self.canvas = canvas#почему нельзя вызвать canvas
        
        self.all_points = 0
        self.id_points = self.create_text(30,30,text = 'Score:' + str(self.all_points),font = '28')

        self.id_bullets = self.create_text(730,30,text = 'Bullets:0',font = '28')
        self.id_grenades = self.create_text(730,50,text = 'Grenades:0',font = '28')

        self.id_med_time = self.create_text(725,90,text = 'Next ammunition:', font = '28')
        self.id_box_time = self.create_text(725,130,text = 'Next aptechka:',font = '28')

        self.out1 = self.create_oval (xc - R, yc - R, xc + R, yc + R, outline="gray", fill="red", width=2)
        self.out1 = self.create_oval (xc - a, yc - a, xc + a, yc + a, fill="white", width=2)

        self.player = Player(self)

        self.id_hp = self.create_rectangle(10, 45, self.player.x_hp, 75, fill='green', width = 2)
        self.id_hp_percents = self.create_text(25,90,text = str(self.player.hp) + '%',font = '28')
        #self.screen1 = self.create_text(400, 300, text='', font = "Times 100 italic bold")

    
    def easy_game(self, event):
        """self.player.level = 1
        self.player.t_med = 10
        self.player.t_box = 10
        self.player.Rexp = 10
        self.player.w = 0.004
        self.player.i_max = 8
        self.player.t_med = 0
        self.player.t_box = 14
        self.player.canvas.delete(self.player.id_level)
        self.player.id_level = self.player.canvas.create_text(730,590,text = 'Difficulty: Easy',font = '28')"""
        
    def easy_game1(self):
        self.player.level = 1
        self.player.t_med = 10
        self.player.t_box = 10
        self.player.Rexp = 10
        self.player.w = 0.004
        self.enemy.e2_max = 0
        self.player.i_max = 8
        self.player.t_med = 0
        self.player.t_box = 14
        self.player.canvas.delete(self.player.id_level)
        self.player.id_level = self.player.canvas.create_text(730,590,text = 'Difficulty: Easy',font = '28')
        
    def medium_game(self, event):
        """self.player.level = 2
        self.player.t_med = 30
        self.player.t_box = 30
        self.player.Rexp = 8
        self.player.w = 0.002
        self.player.i_max = 10
        self.player.t0_med = 20
        self.player.t0_box = 14
        self.player.canvas.delete(self.player.id_level)
        self.player.id_level = self.player.canvas.create_text(730,590,text = 'Difficulty: Medium',font = '28')"""
        
    def medium_game1(self):
        self.player.level = 2
        self.player.t_med = 30
        self.player.t_box = 30
        self.player.Rexp = 8
        self.player.w = 0.002
        self.enemy.e2_max = 2
        self.player.i_max = 10
        self.player.t0_med = 20
        self.player.t0_box = 14
        self.player.canvas.delete(self.player.id_level)
        self.player.id_level = self.player.canvas.create_text(730,590,text = 'Difficulty: Medium',font = '28')
    
    def hard_game(self, event):
        """self.player.level = 3
        self.player.t_med = 40
        self.player.t_box = 40
        self.player.Rexp = 6
        self.player.w = 0.008
        self.player.i_max = 14
        self.player.t0_med = 25
        self.player.t0_box = 30
        self.player.canvas.delete(self.player.id_level)
        self.player.id_level = self.player.canvas.create_text(730,590,text = 'Difficulty: Hard',font = '28')"""
        
    def hard_game1(self):
        self.player.level = 3
        self.player.t_med = 40
        self.player.t_box = 40
        self.player.Rexp = 6
        self.player.w = 0.008
        self.enemy.e2_max = 3
        self.player.i_max = 14
        self.player.t0_med = 25
        self.player.t0_box = 30
        self.player.canvas.delete(self.player.id_level)
        self.player.id_level = self.player.canvas.create_text(730,590,text = 'Difficulty: Hard',font = '28')
          
    def ultrahard_game(self, event):
        """self.player.level = 4
        self.player.t_med = 50
        self.player.t_box = 50
        self.player.Rexp = 4
        self.player.w = 0.015
        self.player.i_max = 16
        self.player.t0_med = 25
        self.player.t0_box = 30
        self.player.canvas.delete(self.player.id_level)
        self.player.id_level = self.player.canvas.create_text(730,590,text = 'Difficulty: Ultrahard',font = '28')"""
        
    def ultrahard_game1(self):
        self.player.level = 4
        self.player.t_med = 50
        self.player.t_box = 50
        self.player.Rexp = 4
        self.player.w = 0.015
        self.enemy.e2_max = 5
        self.player.i_max = 16
        self.player.t0_med = 25
        self.player.t0_box = 30
        self.player.canvas.delete(self.player.id_level)
        self.player.id_level = self.player.canvas.create_text(730,590,text = 'Difficulty: Ultrahard',font = '28')
    
    def choose(self):
        global balls
        if self.select==0:
            self.player.vx = 0
            self.player.vy = 0
        for b in balls:
#!почему нельзя прописать условие select=True, переменная равна True?
            if (b.x<=40) and (b.x>=0) and (b.y>=150) and (b.y<=200) and (self.select == 0):
                
                self.easy_game1()
                self.select = 1
                self.player.bull = 15
                self.player. gren = 5
                for b in balls:
                    self.delete(b.id)
                balls = []
                
            if (b.x<=40) and (b.x>=0) and (b.y>=320) and (b.y<=390) and (self.select == 0):
                
                self.medium_game1()
                self.select = 1
                self.player.bull = 15
                self.player. gren = 5
                for b in balls:
                    self.delete(b.id)
                balls = []
                
            if (b.x<=40) and (b.x>=0) and (b.y>=420) and (b.y<=500) and (self.select == 0):
                
                self.hard_game1()
                self.select = 1
                self.player.bull = 15
                self.player. gren = 5
                for b in balls:
                    self.delete(b.id)
                balls = []
                
            if (b.x<=40) and (b.x>=0) and (b.y>=550) and (b.y<=640) and (self.select == 0):
                
                self.hard_game1()
                self.select = 1
                self.player.bull = 15
                self.player. gren = 5
                for b in balls:
                    self.delete(b.id)
                balls = []
        self.after(2, self.choose)
    
    
    def start(self, event):
        global balls, enemys, boxes, medes, enemys2, enemys3

        self.delete(self.screen1)
        self.player.canvas.delete(self.player.id_level)
        self.player.id_level = self.player.canvas.create_text(730,590,text = 'Difficulty: Default',font = '28')
        self.select = 0
        
#!здесь не нужно удвлять список в цикле, почему мы прописываем self.delete? 
        for bb in balls:
            self.delete(bb.id)
            balls=[]

        for e in enemys:
            self.delete(e['id'])
            enemys = []
            
        for e in enemys2:
            self.delete(e['id'])
            enemys2 = []

        for m in medes:
            self.delete(m['id'])
            medes = []
        for e in enemys3:
            self.delete(e['id'])
        enemys3 = []
        for bx in boxes:
            self.delete(bx['id'])
            boxes = []

        self.trigger = 0
        
        self.player.y = yc
        self.player.x = xc
        self.player.vx = 0
        self.player.vy = 0

        self.player.bull = 30
        self.player.gren = 0
        self.player.hp = 100
        self.player.x_hp = 200

        self.all_points = 0
        self.streak = 0
        self.deltav = 10
        self.k_func = 0

        self.player.t0_med = 17
        self.player.t_med = 20

        self.player.t0_box = 15
        self.player.t_box = 20


        self.delete(self.id_hp)
        self.delete(self.id_hp_percents)
        self.delete(self.screen1)
        self.id_hp = self.create_rectangle(10, 45, self.player.x_hp, 75, fill='green', width = 2)
        self.id_hp_percents = self.create_text(25,90,text = str(self.player.hp) + '%' ,font = '28')

        self.player.start()
        self.enemy = Enemy(self)
        self.update()
        self.choose()
        

    def change_trigger(self, event):
        self.dedected_restart = True



    def check_minus_hp(self):
        global enemys, enemys2, scores, text, enemys3
        for e in enemys:
            if (e['x'] - self.player.x)**2 + (e['y'] - self.player.y)**2 <= (self.player.R1 + e['r'])**2:
                self.player.hp -= 1
                self.player.x_hp -= 2
                self.itemconfig(self.id_hp_percents, text = str(self.player.hp) + '%')
                self.delete(self.id_hp)
                self.id_hp = self.create_rectangle(10, 45, self.player.x_hp, 75, fill='green', width = 2)
                
        for e in enemys2:
            if (e['x'] - self.player.x)**2 + (e['y'] - self.player.y)**2 <= (self.player.R1 + e['r'])**2:
                self.player.hp -= 1
                self.player.x_hp -= 2
                self.itemconfig(self.id_hp_percents, text = str(self.player.hp) + '%')
                self.delete(self.id_hp)
                self.id_hp = self.create_rectangle(10, 45, self.player.x_hp, 75, fill='green', width = 2) 
                
        for e in enemys3:
            if (e['x'] - self.player.x)**2 + (e['y'] - self.player.y)**2 <= (self.player.R1 + e['r'])**2:
                self.player.hp -= 1
                self.player.x_hp -= 2
                self.itemconfig(self.id_hp_percents, text = str(self.player.hp) + '%')
                self.delete(self.id_hp)
                self.id_hp = self.create_rectangle(10, 45, self.player.x_hp, 75, fill='green', width = 2) 
                
                
        if self.player.hp <= 0 or (self.player.x - xc)**2 + (self.player.y - yc)**2 >= R**2 :
            #self.itemconfig(self.screen1, text='GAME OVER', font = "Times 100 italic bold")
            self.screen1 = self.create_text(400, 300, text='Game Over', font = "Times 100 italic bold")
            self.trigger = 1
            self.player.stop()
            self.dedected_restart = False
            scores.append(self.all_points)
            self.max = max(scores)
            #open('Player_score.txt','w').write(name + ', ваш лучший результат:  ' + str(self.max) + ' очков!')
#!sho za get root?
    def get_root(self):
        root = self.master
        while root.master is not None:
            root = root.master
        return root


    def update(self):
        global enemys3
        if self.trigger == 1:
            return
        
        for b in balls:
            b.move()
            for k, e in enumerate(enemys):   
                if (b.x-e['x'])**2 + (b.y-e['y'])**2 <= (b.r + e['r'])**2:
                    self.delete(e['id'])
                    self.streak+=1
                    if self.streak==1:
                        #clip_00[r_0].play()
                        self.all_points +=1
                    elif self.streak==2:
                        #clip_r[0].play()
                        self.all_points +=2
                    elif self.streak==3:
                        #clip_r[1].play()
                        self.all_points +=3
                    elif self.streak==4:
                        #clip_r[2].play()
                        self.all_points +=4
                    elif self.streak==5:
                        #clip_r[3].play()
                        self.all_points +=5
                    elif self.streak>=5:
                        #clip_r5[r_01].play()
                        self.all_points +=5
                    self.enemy.enemys-=1
                    del enemys[k]
                    b.x = 0
                    b.y = 0
                    b.vx = 0
                    b.vy = 0
                    b.live=0
            for k, e in enumerate(enemys2):   
                if (b.x-e['x'])**2 + (b.y-e['y'])**2 <= (b.r + e['r'])**2:
                    #if const=true
                    self.enemy.new_enemy3(e['x'], e['y'], 2, 0)
                    self.enemy.new_enemy3(e['x'], e['y'], -2, 0)
                    tk.Canvas.update(self)
                    self.enemy.new_enemy3(e['x'], e['y'], 0, 2)
                    self.enemy.new_enemy3(e['x'], e['y'], 0, -2)
                    tk.Canvas.update(self)
                    self.delete(e['id'])
                    self.streak+=1
                    if self.streak==1:
                        #clip_00[r_0].play()
                        self.all_points +=1
                    elif self.streak==2:
                        #clip_r[0].play()
                        self.all_points +=2
                    elif self.streak==3:
                        #clip_r[1].play()
                        self.all_points +=3
                    elif self.streak==4:
                        #clip_r[2].play()
                        self.all_points +=4
                    elif self.streak==5:
                        #clip_r[3].play()
                        self.all_points +=5
                    elif self.streak>=5:
                        #clip_r5[r_01].play()
                        self.all_points +=5
                    self.enemy.enemys2-=1
                    del enemys2[k]
                    b.x = 0
                    b.y = 0
                    b.vx = 0
                    b.vy = 0
                    b.live=0
                    
            for k, e in enumerate(enemys3):   
                if (b.x-e['x'])**2 + (b.y-e['y'])**2 <= (b.r + e['r'])**2:
                    self.delete(e['id'])
                    self.streak+=1
                    if self.streak==1:
                        #clip_00[r_0].play()
                        self.all_points +=1
                    elif self.streak==2:
                        #clip_r[0].play()
                        self.all_points +=2
                    elif self.streak==3:
                        #clip_r[1].play()
                        self.all_points +=3
                    elif self.streak==4:
                        #clip_r[2].play()
                        self.all_points +=4
                    elif self.streak==5:
                        #clip_r[3].play()
                        self.all_points +=5
                    elif self.streak>=5:
                        #clip_r5[r_01].play()
                        self.all_points +=5
                    self.enemy.enemys3-=1
                    del enemys3[k]
                    b.x = 0
                    b.y = 0
                    b.vx = 0
                    b.vy = 0
                    b.live=0

            if b.live == 1:
                self.streak=0
            if b.live<=0:
                self.delete(b.id)
            b.live-=1

        for g in grenades:
            g.move()

            for k, e in enumerate(enemys):   
                if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.r+e['r'])**2 :
                    #g.blowup()#как создать отдельное время лишь только для бомб, когда прописываешь time.sleep останавливается все
                    for i in range(g.bangtime):
                        g.r+=g.Rexp
                        boom = self.create_oval(
                        g.x - g.r,
                        g.y - g.r,
                        g.x + g.r,
                        g.y + g.r,
                        fill='orange'
                        )
                        tk.Canvas.update(self)#xz
                        time.sleep(0.06)
                        self.delete(boom)
                        
                    self.delete(e['id'])
                    self.delete(g.id)
                    
                    self.streak+=1

                    if self.streak==1:
                        #clip_10[r_0].play()
                        self.all_points +=1
                    elif self.streak==2:
                        #clip_r[0].play()
                        self.all_points +=2
                    elif self.streak==3:
                        #clip_r[1].play()
                        self.all_points +=3
                    elif self.streak==4:
                        #clip_r[2].play()
                        self.all_points +=4
                    elif self.streak==5:
                        #clip_r[3].play()
                        self.all_points +=5
                    elif self.streak>=5:
                        #clip_r5[r_01].play()
                        self.all_points +=5
                    for kk, e in enumerate(enemys):   
                        if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.Rexp*g.bangtime+g.r)**2 :
                            self.delete(e['id'])
                            #g.blowup()
                            self.all_points +=1
                            self.enemy.enemys-=1
                            del enemys[kk]
                    for kk, e in enumerate(enemys2):   
                        if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.Rexp*g.bangtime+g.r)**2 :
                            self.delete(e['id'])
                            #g.blowup()
                            self.all_points +=1
                            self.enemy.enemys2-=1
                            del enemys2[kk]
                    
                    for kk, e in enumerate(enemys3):   
                        if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.Rexp*g.bangtime+g.r)**2 :
                            self.delete(e['id'])
                            #g.blowup()
                            self.all_points +=1
                            self.enemy.enemys2-=1
                            del enemys3[kk]
                    
                    
                    for bb in enemys:
                        bb['vx']+= self.deltav*R*(bb['x'] - g.x)/( (bb['x'] - g.x)**2 + (bb['y'] - g.y)**2 )*0.09
                        bb['vy']+= self.deltav*R*(bb['y'] - g.y)/( (bb['x'] - g.x)**2 + (bb['y'] - g.y)**2 )*0.09
                    g.x = 0
                    g.y = 0
                    g.vx = 0
                    g.vy = 0
                        
                        
            for k, e in enumerate(enemys2):   
                if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.r+e['r'])**2 :
                    #g.blowup()#как создать отдельное время лишь только для бомб, когда прописываешь time.sleep останавливается все
                    for i in range(g.bangtime):
                        g.r+=g.Rexp
                        boom = self.create_oval(
                        g.x - g.r,
                        g.y - g.r,
                        g.x + g.r,
                        g.y + g.r,
                        fill='orange'
                        )
                        tk.Canvas.update(self)#xz
                        time.sleep(0.06)
                        self.delete(boom)
                        
                    self.delete(e['id'])
                    self.delete(g.id)
                    
                    self.streak+=1

                    if self.streak==1:
                        #clip_10[r_0].play()
                        self.all_points +=1
                    elif self.streak==2:
                        #clip_r[0].play()
                        self.all_points +=2
                    elif self.streak==3:
                        #clip_r[1].play()
                        self.all_points +=3
                    elif self.streak==4:
                        #clip_r[2].play()
                        self.all_points +=4
                    elif self.streak==5:
                        #clip_r[3].play()
                        self.all_points +=5
                    elif self.streak>=5:
                        #clip_r5[r_01].play()
                        self.all_points +=5
                    for kk, e in enumerate(enemys):   
                        if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.Rexp*g.bangtime+g.r)**2 :
                            self.delete(e['id'])
                            #g.blowup()
                            self.all_points +=1
                            self.enemy.enemys-=1
                            del enemys[kk]
                    for kk, e in enumerate(enemys2):   
                        if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.Rexp*g.bangtime+g.r)**2 :
                            self.delete(e['id'])
                            #g.blowup()
                            self.all_points +=1
                            self.enemy.enemys2-=1
                            del enemys2[kk]
                    
                    for kk, e in enumerate(enemys3):   
                        if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.Rexp*g.bangtime+g.r)**2 :
                            self.delete(e['id'])
                            #g.blowup()
                            self.all_points +=1
                            self.enemy.enemys2-=1
                            del enemys3[kk]
                    
                    for bb in enemys:
                        bb['vx']+= self.deltav*R*(bb['x'] - g.x)/( (bb['x'] - g.x)**2 + (bb['y'] - g.y)**2 )*0.09
                        bb['vy']+= self.deltav*R*(bb['y'] - g.y)/( (bb['x'] - g.x)**2 + (bb['y'] - g.y)**2 )*0.09
                    g.x = 0
                    g.y = 0
                    g.vx = 0
                    g.vy = 0

            for k, e in enumerate(enemys3):   
                if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.r+e['r'])**2 :
                    #g.blowup()#как создать отдельное время лишь только для бомб, когда прописываешь time.sleep останавливается все
                    for i in range(g.bangtime):
                        g.r+=g.Rexp
                        boom = self.create_oval(
                        g.x - g.r,
                        g.y - g.r,
                        g.x + g.r,
                        g.y + g.r,
                        fill='orange'
                        )
                        tk.Canvas.update(self)#xz
                        time.sleep(0.06)
                        self.delete(boom)
                        
                    self.delete(e['id'])
                    self.delete(g.id)
                    
                    self.streak+=1

                    if self.streak==1:
                        #clip_10[r_0].play()
                        self.all_points +=1
                    elif self.streak==2:
                        #clip_r[0].play()
                        self.all_points +=2
                    elif self.streak==3:
                        #clip_r[1].play()
                        self.all_points +=3
                    elif self.streak==4:
                        #clip_r[2].play()
                        self.all_points +=4
                    elif self.streak==5:
                        #clip_r[3].play()
                        self.all_points +=5
                    elif self.streak>=5:
                        #clip_r5[r_01].play()
                        self.all_points +=5
                    for kk, e in enumerate(enemys):   
                        if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.Rexp*g.bangtime+g.r)**2 :
                            self.delete(e['id'])
                            #g.blowup()
                            self.all_points +=1
                            self.enemy.enemys-=1
                            del enemys[kk]
                    for kk, e in enumerate(enemys2):   
                        if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.Rexp*g.bangtime+g.r)**2 :
                            self.delete(e['id'])
                            #g.blowup()
                            self.all_points +=1
                            self.enemy.enemys2-=1
                            del enemys2[kk]
                    
                    for kk, e in enumerate(enemys3):   
                        if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.Rexp*g.bangtime+g.r)**2 :
                            self.delete(e['id'])
                            #g.blowup()
                            self.all_points +=1
                            self.enemy.enemys2-=1
                            del enemys3[kk]
                    
                    for bb in enemys:
                        bb['vx']+= self.deltav*R*(bb['x'] - g.x)/( (bb['x'] - g.x)**2 + (bb['y'] - g.y)**2 )*0.09
                        bb['vy']+= self.deltav*R*(bb['y'] - g.y)/( (bb['x'] - g.x)**2 + (bb['y'] - g.y)**2 )*0.09
                    g.x = 0
                    g.y = 0
                    g.vx = 0
                    g.vy = 0

            if g.live == 1:
                self.streak=0
            if g.live<=0:
                self.delete(g.id)
            else:
                g.live+= -1

        self.itemconfig(self.id_bullets, text='Bullets:'+str(self.player.bull))
        self.itemconfig(self.id_grenades, text='Grenades:'+str(self.player.gren))    
        self.itemconfig(self.id_points, text='Score:'+str(self.all_points))
        if self.select==1:
            if self.k_func % 200 == 0:
                self.enemy.new_enemy()
                self.enemy.x = rnd(100, 700)
                self.enemy.y = rnd(100, 500)
                self.enemy.r = rnd(10, 15)
            if self.k_func % 200 == 0:
                self.enemy.new_enemy2()
                self.enemy.x2 = rnd(100, 700)
                self.enemy.y2 = rnd(100, 500)
                self.enemy.r2 = rnd(20, 25)
    
        
        self.enemy.motion()
        self.enemy.motion2(self.player)
        self.enemy.motion3()
        self.enemy.define_max_num(self.player)
        
        self.enemy.vx = rnd(-2, 2)
        self.enemy.vy = rnd(-2, 2)
        
        self.enemy.vx2 = rnd(-1, 1)
        self.enemy.vy2 = rnd(-1, 1)
        for k, e in enumerate(enemys3):
            if e['t']<=0:
                self.delete(e['id'])
                e['x']=0
                e['y']=0
                e['vx']=0
                e['vy']=0
                del enemys3[k]

        self.player.move()
        self.player.acceleration()
        self.player.targetting()
        self.check_minus_hp()
        if self.select == 1:
            if self.k_func / 1000 == 1:
                self.player.time_of_medicaments()
                self.player.time_of_boxes()

                self.player.x_box = rnd(260,540)
                self.player.y_box = rnd(185,465)

                self.k_func = 0

        for k, bx in enumerate(boxes):
            if (self.player.x-bx['x'])**2 + (self.player.y-bx['y'])**2 <= (self.player.R1 + self.player.a_box)**2:
                    self.delete(bx['id'])
                    self.player.bull+=5
                    self.player.gren+=2
                    del boxes[k]

        for k, mx in enumerate(medes):
            if (self.player.x-mx['x'])**2 + (self.player.y-mx['y'])**2 <= (self.player.R1 + self.player.a_box)**2:
                    self.delete(mx['id'])
                    if self.player.hp+20<=100:
                        self.player.hp+=20
                        self.player.x_hp+=40
                    elif self.player.hp+20>100:
                        self.player.hp = 100
                        self.player.x_hp=200
                    self.itemconfig(self.id_hp_percents, text = str(self.player.hp) + '%')
                    self.delete(self.id_hp)
                    self.id_hp = self.create_rectangle(10, 45, self.player.x_hp, 75, fill='green', width = 2)
                    #clip_med.play()
                    del medes[k]
        if self.select ==1:
            self.k_func+=20
        self.after(20, self.update)


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.num_clicks = 0
        
        self.battlefield = BattleField(self)
        self.battlefield.pack(fill=tk.BOTH, expand=1)

        self.buttom_new_game = tk.Button(self, text = 'New Game',background='blue',foreground='white', width = 10, height = 1)
        self.buttom_new_game.place_configure(x=550, y=25)
        self.buttom_new_game.bind("<Button-1>", self.start_game)
#что за рестарт?
#        self.buttom_restart = tk.Button(self, text = 'Restart',background='blue',foreground='white', width = 10, height = 1)
#        self.buttom_restart.place_configure(x=580, y=55)
#        self.buttom_restart.bind("<Button-1>", self.restart)
      
             
        self.buttom_easy = tk.Button(self, text = 'Easy', background='lime', foreground='black', width = 10, height = 2)
        self.buttom_easy.place_configure(x=10, y=150)
        self.buttom_easy.bind("<Button-1>", self.easy_game)        

        self.buttom_medium = tk.Button(self, text = 'Medium',background='gold',foreground='black', width = 10, height = 2)
        self.buttom_medium.place_configure(x=10, y=300)
        self.buttom_medium.bind("<Button-1>", self.medium_game)
                
        self.buttom_hard = tk.Button(self, text = 'Hard',background='orangered',foreground='black', width = 10, height = 2)
        self.buttom_hard.place_configure(x=10, y=420)
        self.buttom_hard.bind("<Button-1>", self.hard_game)

        self.buttom_ultrahard = tk.Button(self, text = 'UltraHard',background='maroon',foreground='black', width = 10, height = 2)
        self.buttom_ultrahard.place_configure(x=10, y=550)
        self.buttom_ultrahard.bind("<Button-1>", self.ultrahard_game)
  
                                                                
         
    def ultrahard_game(self, event):
        if self.battlefield.trigger == 1:
            self.battlefield.start(event)
            self.battlefield.ultrahard_game(event) 
        
    def hard_game(self, event):
        if self.battlefield.trigger == 1:
            self.battlefield.start(event)
            self.battlefield.hard_game(event)
    
    def medium_game(self, event):
        if self.battlefield.trigger == 1:
            self.battlefield.start(event)
            self.battlefield.medium_game(event)
          
    def easy_game(self, event):
        if self.battlefield.trigger == 1:
            self.battlefield.start(event)
            self.battlefield.easy_game(event)
    
# ________________________________________________________________
    
#    def restart(self, event):
#        self.battlefield.change_trigger(event)    
#        self.battlefield.start(event)
        
    def start_game(self, event):
        if self.battlefield.trigger == 1 or self.num_clicks == 0:
            #self.battlefield.choose()
            self.battlefield.start(event)
            self.num_clicks = 1


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('{}x{}'.format(*WINDOW_SIZE))

        self.main_frame = MainFrame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

    def start_game(self, event):    
        self.main_frame.start_game(event)

#print('Введите имя игрока:')
#name = input()
    
app = App()
app.start_game("<Button-1>")
#app.restart("<Button-1>")
app.mainloop()
