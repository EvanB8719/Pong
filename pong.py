from tkinter import*
import random
import time

point = 0
point1 = 0

tk = Tk()
tk.title("Pong")#titre du jeu
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)#fenetre  d'attributs
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)#Caractéristique de la fenetre
canvas.config(bg = 'black')# couleur de fond
canvas.pack()
tk.update()

canvas.create_line(250,0,250,400,fill ='white')#couleur de la ligne au centre

class Ball:#création de la balle
    def __init__(self,canvas,color,paddle,paddle1):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle = paddle1
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,235,200)
        starts = [-3,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = 500

    
    
    def draw(self):#collision de la balle sur les murs
        self.canvas.move(self.id, self.x,self.y)
        pos = self.canvas.coords(self.id)
        print(pos, self.y, self.x)
        if pos[1] <= 0:
            self.y = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
            self.score(False)
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
            self.score(True)
        if self.hit_paddle(pos) == True:
            self.x = 3
        if self.hit_paddle1(pos) == True:
            self.x = -3

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(paddle.id)
        if pos[1]>= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0]>= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False

    def hit_paddle1(self,pos):
        paddle_pos = self.canvas.coords(paddle1.id)
        if pos[1]>= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2]>= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
            return False

    def score(self,val):#création du score
        global point
        global point1

        if val == True:
            a = self.canvas.create_text(125,40,text = point, font=("Arial",60),fill= 'White')
            canvas.itemconfig(a,fill = 'black')
            point += 1
            a = self.canvas.create_text(125,40,text = point, font=("Arial",60),fill= 'White')

        if val == False:
            a = self.canvas.create_text(375,40,text = point1, font=("Arial",60),fill= 'White')
            canvas.itemconfig(a,fill = 'black')
            point1 += 1
            a = self.canvas.create_text(375,40,text = point1, font=("Arial",60),fill= 'White')

class Paddle:#création de la raquette 1
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,150,30,250, fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('a', self.turn_left)
        self.canvas.bind_all('e', self.turn_right)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y= 0
        if pos[3] >=400:
            self.y = 0
    def turn_left(self,evt):
        self.y = -3
    def turn_right(self,evt):
        self.y = 3

class Paddle1:#création de la raquette 2
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(470,150,500,250, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.y = 0
        self.canvas.bind_all('i', self.turn_left)
        self.canvas.bind_all('p', self.turn_right)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y= 0
        if pos[3] >=400:
            self.y = 0
    def turn_left(self,evt):
        self.y = 3
    def turn_right(self,evt):
        self.y = -3
 
paddle = Paddle(canvas, 'pink')
paddle1 = Paddle1(canvas, 'pink')
ball = Ball(canvas, 'white' , paddle, paddle1)


while 1:
    ball.draw()
    paddle.draw()
    paddle1.draw()
    
    if point == 10:
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        paddle1.y = 0
        canvas.create_text(250,200,text="BienJouéJ1!C'estGagné!",font=32,fill='red')
        canvas.create_text(250,215,text="Score:"+str(point1)+"-"+str(point1),font=32,fill='red')
    if point1 == 10:
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        paddle1.y = 0
        canvas.create_text(250,200,text="BienJouéJ2!C'estGagné!",font=32,fill='red')
        canvas.create_text(250,215,text="Score:"+str(point)+"-"+str(point),font=32,fill='red')

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

    if point == 5 or point1 ==5:
        time.sleep(10)