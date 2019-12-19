from math import sqrt
from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import graphics as gr
import mp3play 

filename_1_easy = r'easy-1.mp3'
filename_2_easy = r'easy-2.mp3'
filename_1_medium = r'medium-1.mp3'
filename_2_medium = r'medium-2.mp3'
filename_1_hard = r'hard-1.mp3'
filename_2_hard = r'hard-2.mp3'
filename_1_ultrahard = r'ultrahard-1.mp3'
filename_2_ultrahard = r'ultrahard-2.mp3'

clip_1_easy = mp3play.load(filename_1_easy)
clip_2_easy = mp3play.load(filename_2_easy)
clip_1_medium = mp3play.load(filename_1_medium)
clip_2_medium = mp3play.load(filename_2_medium)
clip_1_hard = mp3play.load(filename_1_hard)
clip_2_hard = mp3play.load(filename_2_hard)
clip_1_ultrahard = mp3play.load(filename_1_ultrahard)
clip_2_ultrahard = mp3play.load(filename_2_ultrahard)

filename00 = r'davit.mp3'
filename01 = r'ud3.mp3'
filename02 = r'1-kill.mp3'
filename03 = r'valera.mp3'

filename10 = r'ud3.mp3'
filename11 = r'na.mp3'
filename12 = r'1-kill.mp3'
filename13 = r'za_pushku.mp3'

filename2 = r'2-kill.mp3'
filename3 = r'3-kill.mp3'
filename4 = r'4-kill.mp3'
filename5 = r'5-kill.mp3'
filename6 = r'boy.mp3'
filename7 = r'sasha.mp3'
filename8 = r'crazy.mp3'
filename9 = r'hor7.mp3'

filename_box = r'box.mp3'
filename_no_bull = r'nobullets.mp3'
filename_minus_hp = r'minus_hp.mp3'
filename_med = r'hill.mp3'
filename_no_gren = r'no_gren.mp3'

clip00 = mp3play.load(filename00)
clip01 = mp3play.load(filename01)
clip02 = mp3play.load(filename02)
clip03 = mp3play.load(filename03)

clip10 = mp3play.load(filename10)
clip11 = mp3play.load(filename11)
clip12 = mp3play.load(filename12)
clip13 = mp3play.load(filename13)

clip2 = mp3play.load(filename2)
clip3 = mp3play.load(filename3)
clip4 = mp3play.load(filename4)
clip5 = mp3play.load(filename5)
clip6 = mp3play.load(filename6)
clip7 = mp3play.load(filename7)
clip8 = mp3play.load(filename8)
clip9 = mp3play.load(filename9)


clip_box = mp3play.load(filename_box)
clip_no_bull = mp3play.load(filename_no_bull)
clip_no_gren = mp3play.load(filename_no_gren)
clip_minus_hp = mp3play.load(filename_minus_hp)
clip_med = mp3play.load(filename_med)
clip_no_gren = mp3play.load(filename_no_gren)

clip_game_level_easy = [clip_1_easy, clip_2_easy]
clip_game_level_medium = [clip_1_medium, clip_2_medium]
clip_game_level_hard = [clip_1_hard, clip_2_hard]
clip_game_level_ultrahard = [clip_1_ultrahard, clip_2_ultrahard]

clip_00 = [clip00, clip01, clip02, clip03]
clip_10 = [clip10, clip11, clip12, clip13]
clip_r = [clip2, clip3, clip4, clip5]
clip_r5 = [clip6, clip7, clip8, clip9]


#load = PIL.Image.open("fon.jpg")
#render = PIL.ImageTk.PhotoImage(load)


#img = Label(self, image=render)
#img.image = render
#img.place(x=0, y=0)

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x650')
canv = tk.Canvas(root, bg='pink')
canv.pack(fill=tk.BOTH, expand=1)

all_points = 0
hp = 100
x_hp = 200
gren = 5
bull = 15
i_max = 6
i_max_agressive = 0
level = 1

trigger=0

t_med = 20000
t0_med = 0
t_box = 20000
t0_box = 14000

deltav = 10
boundv = 0.1

id_level = canv.create_text(730,590,text = 'Difficulty: Easy',font = '28')
id_points = canv.create_text(30,30,text = 'Score:' + str(all_points),font = '28')
id_hp = canv.create_rectangle(10, 45, x_hp, 75, fill='green', width = 2)
id_hp_percents = canv.create_text(25,90,text = str(hp) + '%',font = '28')
id_bullets = canv.create_text(730,30,text = 'Bullets:0',font = '28')
id_grenades = canv.create_text(730,50,text = 'Grenades:0',font = '28')
id_med_time1 = canv.create_text(725,90,text = 'Next ammunition:', font = '28')
id_box_time1 = canv.create_text(725,130,text = 'Next aptechka:',font = '28')
id_med_time2 = canv.create_text(725,110,text = '00:00',font = '28')
id_box_time2 = canv.create_text(725,150,text = '00:00',font = '28')


def create_objects():
    canv.create_oval (x_0, y_0, x_0 + 2*R, y_0 + 2*R, outline="gray", fill="red", width=2)
    canv.create_oval (x_0 + R-a, y_0 + R-a, x_0 + R + a, y_0 + R+a, fill="white", width=2)


streak = 0
Rexp = 10
k_x = 1
k_y = 1 
i=0
k=0
x_0 = 100
y_0 = 25
R = 300
a = 200
M = 1
dt = 1
w = 0.002
yc = 325
xc = 400

create_objects()

r_level = 0

i0 = 0
i0_agressive = 0
enemys_agressive = []

a_box = 20
b_box = 40

enemys=[]
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
        self.i0 = 0
        self.i0_agressive = 0
        
        
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
        global Rexp
        for i in range(self.bangtime):
            self.r0+=Rexp
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
    def __init__(self, ):
        self.game = Game()
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
            new_ball.vx = new_ball.vx * math.cos(self.an)
            new_ball.vy = - new_ball.vy * math.sin(self.an)
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
        self.ax =  -2*w*self.vy + (w**2)*(self.x-xc)
        self.ay =  2*w*self.vx +(w**2)*(self.y-yc)
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
        #self.x += k_x*self.v
        #self.y += k_y*self.v
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
        
        
    def new_aptechka(self):
        self.x_box = rnd(260,540)
        self.y_box = rnd(185,465)
        if (self.x_box - xc)**2 + (y_box - yc)**2 <= a**2:
            id_med = canv.create_rectangle(x_box, y_box, x_box + a_box, y_box + b_box, fill='aqua', width=2)
            med={'id': id_med, 'x': x_box, 'y': y_box}
            medes.append(med)


    def time_of_medicaments():
        global t0_med, id_med_time2, t_med
        t0_med+=1000
        if t_med - t0_med >= 10000:
            canv.delete(id_med_time2)
            id_med_time2 = canv.create_text(725,150,text = '00:' + str((t_med-t0_med)//1000), font = '32')
        elif t_med - t0_med > 0:
            canv.delete(id_med_time2)
            id_med_time2 = canv.create_text(725,150,text = '00:0' + str((t_med-t0_med)//1000), font = '32')
        elif t_med - t0_med == 0:
            t0_med = 0
            canv.delete(id_med_time2)
            id_med_time2 = canv.create_text(725,150,text = '00:00', font = '32')
            new_aptechka()

        root.after(1000,time_of_medicaments)

P1 = Player()

def get_r_vector(x,y):
    length_vector = sqrt(((x_0 + R)-x)**2 + ((y_0 + R)-y)**2)
    radius_vector = gr.Point(((x_0 + R)-x) / length_vector, ((y_0 + R)-y) / length_vector)
    return radius_vector


def get_normal(x,y):
    length_vector = sqrt(((x_0 + R)-x)**2 + ((y_0 + R)-y)**2)
    normal_vector = gr.Point(((y_0 + R)-y) / length_vector, -((x_0 + R)-x) / length_vector)
    return normal_vector


def scalar_multiplication(vector_1, vector_2):
    scalar = vector_1.x*vector_2.x + vector_1.y*vector_2.y
    return scalar


def change_velocity_vx(vx, vy, x, y):
    velocity=gr.Point(vx, vy)
    vel_normal_0 = gr.Point(get_r_vector(x,y).x 
                            * scalar_multiplication(get_r_vector(x,y),velocity), 
                            get_r_vector(x,y).y 
                            * scalar_multiplication(get_r_vector(x,y),velocity)
    )
    vel_tau = gr.Point(get_normal(x,y).x 
                       * scalar_multiplication(get_normal(x,y),velocity), 
                       get_normal(x,y).y 
                       * scalar_multiplication(get_normal(x,y),velocity)
    )
    vel_normal_1 = gr.Point(-vel_normal_0.x,-vel_normal_0.y)
    i = gr.Point(1, 0)

    vel_1_x = scalar_multiplication(vel_normal_1, i)
    vel_2_x = scalar_multiplication(vel_tau, i)
    vx = vel_1_x + vel_2_x
    
    return vx


def change_velocity_vy(vx, vy, x, y):
    velocity=gr.Point(vx, vy)
    vel_normal_0 = gr.Point(get_r_vector(x,y).x 
                            * scalar_multiplication(get_r_vector(x,y),velocity), 
                            get_r_vector(x,y).y 
                            * scalar_multiplication(get_r_vector(x,y),velocity)
    )
    vel_tau = gr.Point(get_normal(x,y).x 
                       * scalar_multiplication(get_normal(x,y),velocity), 
                       get_normal(x,y).y 
                       * scalar_multiplication(get_normal(x,y),velocity)
    )
    vel_normal_1 = gr.Point(-vel_normal_0.x,-vel_normal_0.y)
    j = gr.Point(0, 1)
    
    vel_1_y = scalar_multiplication(vel_normal_1, j)
    vel_2_y = scalar_multiplication(vel_tau, j)
    
    vy = vel_1_y + vel_2_y
    
    return vy


def go_to_player():
    global enemys_agressive
    for e in enemys_agressive:
        v = ((e['vx']**2 + e['vy']**2)**0.25)
        sina = (P1.y - e['y'])/sqrt((P1.x-e['x'])**2 + (P1.y - e['y'])**2 )
        cosa = (P1.x - e['x'])/sqrt((P1.x-e['x'])**2 + (P1.y - e['y'])**2 )
        e['vx'] = v*cosa
        e['vy'] = v*sina
    root.after(20 , go_to_player)


def new_enemy_agressive():
    global i0_agressive, enemys_agressive, i_max_agressive
    i0_agressive = len(enemys_agressive)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(15,20)
    vx=rnd(-2, 2)
    vy=rnd(-2, 2)
    hp_e = 4
    if i0_agressive < i_max_agressive:
        if (x - (x_0 + R))**2 + (y - (y_0 + R))**2 >= a**2 and (x - (x_0 + R))**2 + (y - (y_0 + R))**2 <= (R-40)**2 :
            id_ = canv.create_oval( x - r, y - r, x + r, y + r,fill = 'blue', width=0, activefill = 'purple')
            enemy_agressive={'id': id_, 'x': x, 'y': y, 'r': r, 'vx': vx, 'vy': vy, 'hp': hp_e}
            enemys_agressive.append(enemy_agressive)
            i0_agressive += 1
    root.after(500,new_enemy_agressive)


def new_enemy():
    global i0, i_max
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(10,15)
    vx=rnd(-6, 6)
    vy=rnd(-6, 6)
    if i0 < i_max:
        if (x - (x_0 + R))**2 + (y - (y_0 + R))**2 >= a**2 and (x - (x_0 + R))**2 + (y - (y_0 + R))**2 <= (R-40)**2 :
            id_ = canv.create_oval( x - r, y - r, x + r, y + r,fill = 'black', width=0, activefill = 'green')
            enemy={'id': id_, 'x': x, 'y': y, 'r': r, 'vx': vx, 'vy': vy}
            enemys.append(enemy)
            i0+=1
 
    root.after(200,new_enemy)


def motion():
    for e in enemys:
        e['vx']+= ( -2*w*e['vy'] + (w**2)*(-x_0 - R + e['x'])  )*dt
        e['vy']+= ( +2*w*e['vx'] + (w**2)*(-y_0 - R + e['y'])  )*dt
        if (x_0 + R - e['x'])**2 + (y_0 + R - e['y'])**2 >= (R-e['r'])**2:
            vx = change_velocity_vx(e['vx'], e['vy'], e['x'], e['y'])
            vy = change_velocity_vy(e['vx'], e['vy'], e['x'], e['y'])
            e['vx'] = vx
            e['vy'] = vy
        e['x']+=e['vx']
        e['y']+=e['vy']
        canv.move(e['id'], e['vx'], e['vy'])
    
    for e in enemys_agressive:
        #e['vx']+= ( -2*w*e['vy'] + (w**2)*(-x_0 - R + e['x'])  )*dt
        #e['vy']+= ( +2*w*e['vx'] + (w**2)*(-y_0 - R + e['y'])  )*dt
        if (x_0 + R - e['x'])**2 + (y_0 + R - e['y'])**2 >= (R-e['r'])**2:
            vx = change_velocity_vx(e['vx'], e['vy'], e['x'], e['y'])
            vy = change_velocity_vy(e['vx'], e['vy'], e['x'], e['y'])
            e['vx'] = vx
            e['vy'] = vy
        e['x']+=e['vx']
        e['y']+=e['vy']
        canv.move(e['id'], e['vx'], e['vy'])

    root.after(20 , motion)


def new_box():
    x_box = rnd(260,540)
    y_box = rnd(185,465)
    if (x_box - xc)**2 + (y_box - yc)**2 <= a**2:
        id_box = canv.create_rectangle(x_box, y_box, x_box + a_box, y_box + b_box, fill='green', width=2)
        box={'id': id_box, 'x': x_box, 'y': y_box}
        boxes.append(box)


def new_aptechka():
    x_box = rnd(260,540)
    y_box = rnd(185,465)
    if (x_box - xc)**2 + (y_box - yc)**2 <= a**2:
        id_med = canv.create_rectangle(x_box, y_box, x_box + a_box, y_box + b_box, fill='aqua', width=2)
        med={'id': id_med, 'x': x_box, 'y': y_box}
        medes.append(med)


def time_of_medicaments():
    global t0_med, id_med_time2, t_med
    t0_med+=1000
    if t_med - t0_med >= 10000:
        canv.delete(id_med_time2)
        id_med_time2 = canv.create_text(725,150,text = '00:' + str((t_med-t0_med)//1000), font = '32')
    elif t_med - t0_med > 0:
        canv.delete(id_med_time2)
        id_med_time2 = canv.create_text(725,150,text = '00:0' + str((t_med-t0_med)//1000), font = '32')
    elif t_med - t0_med == 0:
        t0_med = 0
        canv.delete(id_med_time2)
        id_med_time2 = canv.create_text(725,150,text = '00:00', font = '32')
        new_aptechka()

    root.after(1000,time_of_medicaments)


def time_of_boxes():
    global t0_box, id_box_time2, t_box
    t0_box+=1000
    if t_box - t0_box >= 10000:
        canv.delete(id_box_time2)
        id_box_time2 = canv.create_text(725,110,text = '00:' + str((t_box-t0_box)//1000), font = '32')
    elif t_box - t0_box > 0:
        canv.delete(id_box_time2)
        id_box_time2 = canv.create_text(725,110,text = '00:0' + str((t_box-t0_box)//1000), font = '32')
    elif t_box - t0_box == 0:
        t0_box = 0
        canv.delete(id_box_time2)
        id_box_time2 = canv.create_text(725,110,text = '00:00', font = '32')
        new_box()

    root.after(1000,time_of_boxes)


def start_new_game():    
    
    global balls, screen1, enemys, all_points, screen1, x_hp, hp, id_hp, id_hp_percents,enemys_agressive, boxes, medes, bull, gren, i0, t0_med, t0_box, streak
            
    #screen1 = canv.create_text(400, 300, text='GAME OVER', font = "Times 100 italic bold")
    
    for bb in balls:
        canv.delete(bb.id)
        balls=[]
            
    for e in enemys:
        canv.delete(e['id'])
        enemys = []

    for m in medes:
        canv.delete(m['id'])
        medes = []
    
    for e in enemys_agressive:
        canv.delete(e['id'])
        enemys_agressive = []
    
    for bx in boxes:
        canv.delete(bx['id'])
        boxes = []
    
    streak = 0
    P1.y = 325
    P1.x = 400
    P1.vx = 0
    P1.vy = 0
    P1.live = 100
    bull = 15
    gren = 5
    hp = 100
    x_hp = 200
    i0 = 0
    t0_box = 14000
    t0_med = 0
    canv.delete(id_hp)
    canv.delete(id_hp_percents)
    id_hp = canv.create_rectangle(10, 45, x_hp, 75, fill='green', width = 2)
    id_hp_percents = canv.create_text(25,90,text = str(hp) + '%' ,font = '28')
    P1.set_coords1
    P1.set_coords2
    P1.set_coords3
    all_points = 0


def game_process(event=''):
    global balls, all_points, grenades, Rexp, i0,i0_agressive, bull, gren, hp, x_hp, id_hp_percents, id_hp, streak, xc, yc, clip_r, clip_box, clip_00, clip_r5, Rexp, clip_10
    root.bind('<Motion>', P1.targetting)
    root.bind('<Right>', P1.move_right)    
    root.bind('<Left>', P1.move_left)
    root.bind('<Up>', P1.move_up)
    root.bind('<Down>', P1.move_down)
    root.bind('<Button-1>', P1.fire2_start)
    root.bind('<Button-3>', P1.fire1_start)

    
    for k, bx in enumerate(boxes):
        if (P1.x-bx['x'])**2 + (P1.y-bx['y'])**2 <= (P1.a1 + a_box)**2:
                canv.delete(bx['id'])
                bull+=5
                gren+=2
                clip_box.play()
                del boxes[k]
                
    for k, mx in enumerate(medes):
        if (P1.x-mx['x'])**2 + (P1.y-mx['y'])**2 <= (P1.a1 + a_box)**2:
                canv.delete(mx['id'])
                if hp+20<=100:
                    hp+=20
                    x_hp+=40
                elif hp+20>100:
                    hp = 100
                    x_hp=200
                canv.itemconfig(id_hp_percents, text = str(hp) + '%')
                canv.delete(id_hp)
                id_hp = canv.create_rectangle(10, 45, x_hp, 75, fill='green', width = 2)
                clip_med.play()
                del medes[k]
    
    for b in balls:
        b.move()
        for k, e in enumerate(enemys):   
            if (b.x-e['x'])**2 + (b.y-e['y'])**2 <= (b.r + e['r'])**2:
                canv.delete(e['id'])
                r_0 = rnd(0,4)
                r_01 = rnd(0,4)
                streak+=1
                if streak==1:
                    clip_00[r_0].play()
                    all_points +=1
                elif streak==2:
                    clip_r[0].play()
                    all_points +=2
                elif streak==3:
                    clip_r[1].play()
                    all_points +=3
                elif streak==4:
                    clip_r[2].play()
                    all_points +=4
                elif streak==5:
                    clip_r[3].play()
                    all_points +=5
                elif streak>=5:
                    clip_r5[r_01].play()
                    all_points +=5
                i0-=1
                del enemys[k]
                b.x = 0
                b.y = 0
                b.vx = 0
                b.vy = 0
                b.live=0
                
        for k, e in enumerate(enemys_agressive):
            if (b.x-e['x'])**2 + (b.y-e['y'])**2 <= (b.r + e['r'])**2:
                all_points +=1
                e['hp'] -= 1
                if e['hp'] == 0:
                    canv.delete(e['id'])
                    r_0 = rnd(0,4)
                    r_01 = rnd(0,4)
                    streak+=1
                    if streak==1:
                        clip_00[r_0].play()
                        all_points +=1
                    elif streak==2:
                        clip_r[0].play()
                        all_points +=2
                    elif streak==3:
                        clip_r[1].play()
                        all_points +=3
                    elif streak==4:
                        clip_r[2].play()
                        all_points +=4
                    elif streak==5:
                        clip_r[3].play()
                        all_points +=5
                    elif streak>=5:
                        clip_r5[r_01].play()
                        all_points +=5
                    i0_agressive-=1
                    del enemys_agressive[k]
                    b.x = 0
                    b.y = 0
                    b.vx = 0
                    b.vy = 0
                    b.live=0
                    
                    
        if b.live == 1:
            streak=0
        if b.live<=0:
            canv.delete(b.id)
        b.live-=1
    
    
    delete=[]
    for g in grenades:
        g.move()
        for k, e in enumerate(enemys):   
            if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.r+e['r'])**2 :
                canv.delete(e['id'])
                canv.delete(g.id)
                g.blowup()
                streak+=1
                r_0 = rnd(0,4)
                r_01 = rnd(0,4)
                if streak==1:
                    clip_10[r_0].play()
                    all_points +=1
                elif streak==2:
                    clip_r[0].play()
                    all_points +=2
                elif streak==3:
                    clip_r[1].play()
                    all_points +=3
                elif streak==4:
                    clip_r[2].play()
                    all_points +=4
                elif streak==5:
                    clip_r[3].play()
                    all_points +=5
                elif streak>=5:
                    clip_r5[r_01].play()
                    all_points +=5
                for kk, e in enumerate(enemys):   
                    if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (Rexp*g.bangtime)**2 :
                        canv.delete(e['id'])
                        all_points +=1
                        i0-=1
                        del enemys[kk]
                for bb in enemys:
                    bb['vx']+= deltav*R*(bb['x'] - g.x)/( (bb['x'] - g.x)**2 + (bb['y'] - g.y)**2 )*0.2
                    bb['vy']+= deltav*R*(bb['y'] - g.y)/( (bb['x'] - g.x)**2 + (bb['y'] - g.y)**2 )*0.2
                g.x = 0
                g.y = 0
                g.vx = 0
                g.vy = 0


        for k, e in enumerate(enemys_agressive):   
            if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (g.r+e['r'])**2 :
                canv.delete(e['id'])
                canv.delete(g.id)
                g.blowup()
                streak+=1
                r_0 = rnd(0,4)
                r_01 = rnd(0,4)
                if streak==1:
                    clip_10[r_0].play()
                    all_points +=1
                elif streak==2:
                    clip_r[0].play()
                    all_points +=2
                elif streak==3:
                    clip_r[1].play()
                    all_points +=3
                elif streak==4:
                    clip_r[2].play()
                    all_points +=4
                elif streak==5:
                    clip_r[3].play()
                    all_points +=5
                elif streak>=5:
                    clip_r5[r_01].play()
                    all_points +=5
                for kk, e in enumerate(enemys_agressive):   
                    if (g.x-e['x'])**2 + (g.y-e['y'])**2 <= (Rexp*g.bangtime)**2 :
                        canv.delete(e['id'])
                        all_points +=1
                        i0-=1
                        del enemys_agressive[kk]
                
                for bb in enemys:
                    bb['vx']+= deltav*R*(bb['x'] - g.x)/( (bb['x'] - g.x)**2 + (bb['y'] - g.y)**2 )*0.2
                    bb['vy']+= deltav*R*(bb['y'] - g.y)/( (bb['x'] - g.x)**2 + (bb['y'] - g.y)**2 )*0.2


                g.x = 0
                g.y = 0
                g.vx = 0
                g.vy = 0
                g.live = 0
        if g.live == 1:
            streak=0
        if g.live<=0:
            canv.delete(g.id)
        else:
            g.live+= -1
        
    
    canv.itemconfig(id_bullets, text='Bullets:'+str(bull))
    canv.itemconfig(id_grenades, text='Grenades:'+str(gren))    
    canv.itemconfig(id_points, text='Score:'+str(all_points))
    canv.update()
    P1.move()
    P1.acceleration()
    P1.targetting()
    P1.check_minus_hp()
    time.sleep(0.03)

    root.after(3, game_process)


def music(event):
    global level, r_level
    for i in range(0,2):
        clip_game_level_easy[i].stop()
        clip_game_level_medium[i].stop()
        clip_game_level_hard[i].stop()
        clip_game_level_ultrahard[i].stop()
    
    if r_level > 1:
        r_level = 0
    if level == 1:
        clip_game_level_easy[r_level].play()
        r_level += 1
    if level == 2:
        clip_game_level_medium[r_level].play()
        r_level += 1
    if level == 3:
        clip_game_level_hard[r_level].play()
        r_level += 1
    if level == 4:
        clip_game_level_ultrahard[r_level].play()
        r_level += 1


def mute(event):
    global level
    for i in range(0,2):
        clip_game_level_easy[i].stop()
        clip_game_level_medium[i].stop()
        clip_game_level_hard[i].stop()
        clip_game_level_ultrahard[i].stop()


def new_game(event):
    global buttom_new_game, trigger
    if trigger==0:
        buttom_new_game.destroy()
        trigger = 1
    while P1.live>0:
        time_of_medicaments()
        time_of_boxes()
        game_process()
        new_enemy()
        new_enemy_agressive()
        go_to_player()
        motion()


def easy_game(event):
    global id_level, t_med, t_box, Rexp, w, imax, t0_med, t0_box, level, enemys, enemys_agressive, i_max, i_max_agressive, all_points
    for i in range(0,2):
        clip_game_level_easy[i].stop()
        clip_game_level_medium[i].stop()
        clip_game_level_hard[i].stop()
        clip_game_level_ultrahard[i].stop()

    for e in enemys:
        canv.delete(e['id'])
        enemys = []


    for e in enemys_agressive:
        canv.delete(e['id'])
        enemys_agressive = []

    level = 1
    all_points = 0
    t_med = 20000
    t_box = 20000
    Rexp = 12
    w = 0.0002
    i_max_agressive = 0
    i_max = 6
    t0_med = 0
    t0_box = 14000
    canv.delete(id_level)
    id_level = canv.create_text(730,590,text = 'Difficulty: Easy',font = '28')


def medium_game(event):
    global id_level, t_med, t_box, Rexp, w, imax, t0_med, t0_box, level, enemys, enemys_agressive, i_max, i_max_agressive, all_points


    for i in range(0,2):
        clip_game_level_easy[i].stop()
        clip_game_level_medium[i].stop()
        clip_game_level_hard[i].stop()
        clip_game_level_ultrahard[i].stop()


    start_new_game()

    level = 2
    all_points = 0
    t_med = 30000
    t_box = 30000
    Rexp = 12
    w = 0.0008
    i_max_agressive = 1
    i_max = 8
    t0_med = 20000
    t0_box = 14000
    canv.delete(id_level)
    id_level = canv.create_text(730,590,text = 'Difficulty: Medium',font = '28')


def hard_game(event):
    global id_level, t_med, t_box, Rexp, w, imax, t0_med, t0_box, level, enemys, enemys_agressive, i_max, i_max_agressive, all_points


    for i in range(0,2):
        clip_game_level_easy[i].stop()
        clip_game_level_medium[i].stop()
        clip_game_level_hard[i].stop()
        clip_game_level_ultrahard[i].stop()


    start_new_game()

    level = 3
    all_points = 0
    t_med = 40000
    t_box = 40000
    Rexp = 10
    w = 0.0012
    i_max_agressive = 2
    i_max = 10
    t0_med = 25000
    t0_box = 30000
    canv.delete(id_level)
    id_level = canv.create_text(730,590,text = 'Difficulty: Hard',font = '28')


def ultrahard_game(event):
    global id_level, t_med, t_box, Rexp, w, imax, t0_med, t0_box, level, enemys, enemys_agressive, i_max, i_max_agressive, all_points


    for i in range(0,2):
        clip_game_level_easy[i].stop()
        clip_game_level_medium[i].stop()
        clip_game_level_hard[i].stop()
        clip_game_level_ultrahard[i].stop()


    start_new_game()

    level = 4
    all_points = 0
    t_med = 50000
    t_box = 50000
    Rexp = 8
    w = 0.0015
    i_max_agressive = 4
    i_max = 8
    t0_med = 25000
    t0_box = 30000
    canv.delete(id_level)
    id_level = canv.create_text(730,590,text = 'Difficulty: Ultrahard',font = '28')



buttom_off = tk.Button(root, text = 'Music off',background='yellow',foreground='black', width = 10, height = 1)
buttom_off.place_configure(x=25, y=150)
buttom_off.bind("<Button-1>", mute)

buttom_on = tk.Button(root, text = 'Music on',background='yellow',foreground='black', width = 10, height = 1)
buttom_on.place_configure(x=25, y=120)
buttom_on.bind("<Button-1>", music)

buttom_new_game = tk.Button(root, text = 'New Game',background='blue',foreground='white', width = 10, height = 1)
buttom_new_game.place_configure(x=550, y=25)
buttom_new_game.bind("<Button-1>", new_game)

buttom_easy = tk.Button(root, text = 'Easy',background='lime',foreground='black', width = 10, height = 1)
buttom_easy.place_configure(x=10, y=600)
buttom_easy.bind("<Button-1>", easy_game)

buttom_medium = tk.Button(root, text = 'Medium',background='gold',foreground='black', width = 10, height = 1)
buttom_medium.place_configure(x=10, y=560)
buttom_medium.bind("<Button-1>", medium_game)

buttom_hard = tk.Button(root, text = 'Hard',background='orangered',foreground='black', width = 10, height = 1)
buttom_hard.place_configure(x=10, y=520)
buttom_hard.bind("<Button-1>", hard_game)

buttom_ultrahard = tk.Button(root, text = 'UltraHard',background='maroon',foreground='black', width = 10, height = 1)
buttom_ultrahard.place_configure(x=10, y=480)
buttom_ultrahard.bind("<Button-1>", ultrahard_game)

root.mainloop()
