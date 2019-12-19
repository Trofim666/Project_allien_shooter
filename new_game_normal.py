from math import sqrt
from random import randrange as rnd, choice
import tkinter as tk
import math
import time
#import graphics as gr


WINDOW_SIZE = (800, 650)

w = 0.002
xc = 400
yc = 325
dt = 1
a = 200
R = 300


enemys=[]
grenades=[]
balls=[]
boxes = []
medes = []

def pass_event():
    pass


class Ball():
    def __init__(self, canvas, x, y):

        self.canvas = canvas
        self.x = x
        self.y = y

        self.r = 3

        self.vx = 10
        self.vy = 10

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

    def update(self):
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()

    def destroy_bullets(self):
        self.canvas.delete(self.id)


class Grenade():
    def __init__(self, canvas, x, y):

        self.canvas = canvas
        self.r = 3
        self.bangtime = 4
        self.x = x
        self.y = y

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

    def update(self):
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        
    
    def blowup(self):
        for i in range(self.bangtime):
            self.r+=Rexp
            self.boom = canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill='orange'
            )
            self.canvas.update()
            time.sleep(0.06)
            self.canvas.delete(self.boom)

    def destroy_grenades(self):
        self.canvas.delete(self.id)


class Player():
    def __init__(self, canvas):

        #self.game = Game()

        self.canvas = canvas

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


    def targetting(self, event=0):
        #global k_x, k_y
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
        #global k_x, k_y
        #sina = (self.y-self.yc)/math.sqrt( (self.x-self.xc)**2 + (self.y-self.yc)**2   )
        #cosa =(self.x-self.xc)/math.sqrt( (self.x-self.xc)**2 + (self.y-self.yc)**2  ) 
        #self.ax = self.F*k_x/self.m + k_x * 2*w*self.vy + w**2*(self.x-self.xc)
        #self.ay = self.F*k_y/self.m + k_y * 2*w*self.vx + w**2*(self.y-self.yc)
        self.ax =  -2*w*self.vy + (w**2)*(self.x-xc)
        self.ay =  2*w*self.vx +(w**2)*(self.y-yc)
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
        #global k_x, k_y

        self.vx+=-self.F*self.k_x/self.m
        self.vy+=self.F*self.k_y/self.m

        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
        
        
    def move_left(self, event):
        #global k_x, k_y

        self.vx+=self.F*self.k_x/self.m
        self.vy+=-self.F*self.k_y/self.m

        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
        
        
    def move_up(self, event):
        #global k_x, k_y
        
        self.vx+=self.F*self.k_x/self.m
        self.vy+=self.F*self.k_y/self.m
        #self.x += k_x*self.v
        #self.y += k_y*self.v
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()
        
        
    def move_down(self, event):
        #global k_x, k_y

        self.vx+=-self.F*self.k_x/self.m
        self.vy+=-self.F*self.k_y/self.m

        self.set_coords1()
        self.set_coords2()
        self.set_coords3()


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

        self.vx = rnd(-6, 6)
        self.vy = rnd(-6, 6)

        self.num_enemys = 8
        self.enemys = 0

        self.canvas = canvas


    '''def get_r_vector(self, x, y):
        self.length_vector = sqrt((xc-self.x)**2 + (yc-self.y)**2)
        self.radius_vector = Point((xc-x) / self.length_vector, (yc-y) / self.length_vector)
        return self.radius_vector


    def get_normal(self, x, y):
        self.length_vector = sqrt((xc-x)**2 + (yc-y)**2)
        self.normal_vector = Point((yc-y) / self.length_vector, -(xc-x) / self.length_vector)
        return self.normal_vector


    def scalar_multiplication(self, vector_1, vector_2):
        self.scalar = vector_1.x*vector_2.x + vector_1.y*vector_2.y
        return self.scalar


    def change_velocity_vx(self, vx, vy, x, y):
        self.velocity=Point(self.vx, self.vy)
        self.vel_normal_0 = Point(self.get_r_vector(self.x,self.y).x 
                                * self.scalar_multiplication(self.get_r_vector(self.x,self.y),self.velocity), 
                                self.get_r_vector(self.x,self.y).y 
                                * self.scalar_multiplication(self.get_r_vector(self.x,self.y),self.velocity)
        )
        self.vel_tau = Point(self.get_normal(self.x,self.y).x 
                           * self.scalar_multiplication(self.get_normal(self.x,self.y),self.velocity), 
                           self.get_normal(self.x,self.y).y 
                           * self.scalar_multiplication(self.get_normal(self.x,self.y),self.velocity)
        )
        self.vel_normal_1 = Point(-self.vel_normal_0.x,-self.vel_normal_0.y)
        self.i = Point(1, 0)

        self.vel_1_x = self.scalar_multiplication(self.vel_normal_1, self.i)
        self.vel_2_x = self.scalar_multiplication(self.vel_tau, self.i)
        self.vx = self.vel_1_x + self.vel_2_x
        
        return self.vx


    def change_velocity_vy(self, vx, vy, x, y):
        self.velocity=Point(self.vx, self.vy)
        self.vel_normal_0 = Point(self.get_r_vector(self.x,self.y).x 
                                * self.scalar_multiplication(self.get_r_vector(self.x,self.y),self.velocity), 
                                self.get_r_vector(self.x,self.y).y 
                                * self.scalar_multiplication(self.get_r_vector(self.x,self.y),self.velocity)
        )
        self.vel_tau = Point(self.get_normal(x,y).x 
                           * self.scalar_multiplication(self.get_normal(self.x,self.y),self.velocity), 
                           self.get_normal(self.x,self.y).y 
                           * self.scalar_multiplication(self.get_normal(self.x,self.y),self.velocity)
        )
        self.vel_normal_1 = Point(-self.vel_normal_0.x,-self.vel_normal_0.y)
        self.j = Point(0, 1)
        
        self.vel_1_y = self.scalar_multiplication(self.vel_normal_1, self.j)
        self.vel_2_y = self.scalar_multiplication(self.vel_tau, self.j)
        
        self.vy = self.vel_1_y + self.vel_2_y
        
        return self.vy'''


    def new_enemy(self):
            if (self.x - xc)**2 + (self.y - yc)**2 >= a**2 and (self.x - xc)**2 + (self.y - yc)**2 <= (R-40)**2 and self.enemys < self.num_enemys:
                self.id_ = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,fill = 'black', width=0, activefill = 'green')
                self.enemy={'id': self.id_, 'x': self.x, 'y': self.y, 'r': self.r, 'vx': self.vx, 'vy': self.vy}
                self.enemys+=1
                enemys.append(self.enemy)


    def motion(self):
        global enemys
        for e in enemys:
            e['vx']+= ( -2*w*e['vy'] + (w**2)*(-xc + e['x'])  )*dt
            e['vy']+= ( +2*w*e['vx'] + (w**2)*(-yc + e['y'])  )*dt
            if (xc - e['x'])**2 + (yc - e['y'])**2 >= (R-e['r'])**2:
                #v_x = self.change_velocity_vx(e['vx'], e['vy'], e['x'], e['y'])
                #v_y = self.change_velocity_vy(e['vx'], e['vy'], e['x'], e['y'])
                e['vx'] = -e['vx']
                e['vy'] = -e['vy']
            e['x']+=e['vx']
            e['y']+=e['vy']
            self.canvas.move(e['id'], e['vx'], e['vy'])


class BattleField(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, background='pink')

        self.num_enemys = 8
        self.enemys = 0

        self.k_func = 0

        self.all_points = 0
        self.id_points = self.create_text(30,30,text = 'Score:' + str(self.all_points),font = '28')

        self.id_bullets = self.create_text(730,30,text = 'Bullets:0',font = '28')
        self.id_grenades = self.create_text(730,50,text = 'Grenades:0',font = '28')

        self.id_med_time = self.create_text(725,90,text = 'Next ammunition:', font = '28')
        self.id_box_time = self.create_text(725,130,text = 'Next aptechka:',font = '28')

        self.out1 = self.create_oval (xc - R, yc - R, xc + R, yc + R, outline="gray", fill="red", width=2)
        self.out1 = self.create_oval (xc - a, yc - a, xc + a, yc + a, fill="white", width=2)

        self.player = Player(self)
        self.enemy = Enemy(self)

        self.id_hp = self.create_rectangle(10, 45, self.player.x_hp, 75, fill='green', width = 2)
        self.id_hp_percents = self.create_text(25,90,text = str(self.player.hp) + '%',font = '28')
        self.screen1 = self.create_text(400, 300, text='', font = "Times 100 italic bold")

    def start(self):
        global balls, screen1, enemys, boxes, medes

        self.screen1 = self.create_text(400, 300, text='', font = "Times 100 italic bold")

        for bb in balls:
            self.delete(bb.id)
            balls=[]

        for e in enemys:
            self.delete(e['id'])
            enemys = []

        for m in medes:
            self.delete(m['id'])
            medes = []

        for bx in boxes:
            self.delete(bx['id'])
            boxes = []

        self.player.y = yc
        self.player.x = xc
        self.player.vx = 0
        self.player.vy = 0

        self.player.bull = 15
        self.player.gren = 5
        self.player.hp = 100
        self.player.x_hp = 200
        self.all_points = 0

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

        if self.k_func % 200 == 0:
            self.enemy.new_enemy()
            self.enemy.x = rnd(100, 700)
            self.enemy.y = rnd(100, 500)


    def check_minus_hp(self):
        global enemys
        for e in enemys:
            if (e['x'] - self.player.x)**2 + (e['y'] - self.player.y)**2 <= (self.player.R1 + e['r'])**2:
                self.player.hp -= 1
                self.player.x_hp -= 2
                self.itemconfig(self.id_hp_percents, text = str(self.player.hp) + '%')
                self.delete(self.id_hp)
                self.id_hp = self.create_rectangle(10, 45, self.player.x_hp, 75, fill='green', width = 2)
        if self.player.hp <= 0 or (self.player.x - xc)**2 + (self.player.y - yc)**2 >= R**2:
            self.itemconfig(self.screen1, text='GAME OVER', font = "Times 100 italic bold")
            #time.sleep(2)
            #self.delete(self.screen1)
            self.start()


    def get_root(self):
        root = self.master
        while root.master is not None:
            root = root.master
        return root

    def game_over():
        self.itemconfig(self.screen1, text='GAME OVER', font = "Times 100 italic bold")
        self.after(2000, self.restart)

    def update(self):  # put root.after here
        for b in balls:
            b.update()
        for g in grenades:
            g.update()


        self.itemconfig(self.id_bullets, text='Bullets:'+str(self.player.bull))
        self.itemconfig(self.id_grenades, text='Grenades:'+str(self.player.gren))    
        self.itemconfig(self.id_points, text='Score:'+str(self.all_points))

        if self.k_func % 200 == 0:
            self.enemy.new_enemy()
            self.enemy.x = rnd(100, 700)
            self.enemy.y = rnd(100, 500)

        self.enemy.motion()
        self.enemy.vx = rnd(-6, 6)
        self.enemy.vy = rnd(-6, 6)

        self.player.move()
        self.player.acceleration()
        self.player.targetting()
        self.check_minus_hp()

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

        self.k_func+=20

        self.after(20, self.update)


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__()

        self.battlefield = BattleField(self)
        self.battlefield.pack(fill=tk.BOTH, expand=1)

    def start_game(self):
        self.battlefield.start()
        self.battlefield.update()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('{}x{}'.format(*WINDOW_SIZE))

        self.main_frame = MainFrame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

    def start_game(self):
        self.main_frame.start_game()

app = App()
app.start_game()
app.mainloop()
