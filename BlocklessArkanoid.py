from tkinter import *
import random
import time
tk = Tk()
tk.title("Bounce")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width =500,height=500,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
global counter
counter =0
class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas =canvas
        self.paddle=paddle
        self.id = canvas.create_oval(10,10,25,25,fill = color)
        self.canvas.move(self.id,245,100)
        start= [-3,-2,2,3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-1
        self.canvas_height =self.canvas.winfo_height()
        self.canvas_width =self.canvas.winfo_width()

    def hitPaddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        paddleLength = paddle_pos[2] - paddle_pos[0]
        if pos[3] >=paddle_pos[1] and pos[3] <=paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[0] <=paddle_pos[0]+paddleLength/3:
                return 1
            if pos[2] >= paddle_pos[0]+paddleLength/3 and pos[0] <=paddle_pos[0] +(2*paddleLength)/3:
                return 2
            if pos[2] >= paddle_pos[0]+(2*paddleLength)/3 and pos[0] <=paddle_pos[2]:
                return 3
        return 0
        
    
    def draw(self,speed):
        self.canvas.move(self.id,speed*self.x,speed*self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=1
        if pos[3]>=self.canvas_height:
            self.y=-1
            global counter
            counter = counter +1
        if pos[2]>=self.canvas_width:
            self.x=-1
        if pos[0]<=0:
            self.x=1
        if self.hitPaddle(pos)==1:
            if self.x == 1:
                self.x = -1
            self.y = -1
        if self.hitPaddle(pos)==2:
            self.y = -1
        if self.hitPaddle(pos)==3:
            if self.x ==  -1:
                self.x = 1
            self.y = -1
               

class Paddle:
    def __init__(self,canvas,color,sensitivity):
        self.canvas =canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,490)
        self.x =0
        self.canvas_width= self.canvas.winfo_width()
        self.sensitivity = sensitivity
        self.canvas.bind_all('<Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <=0:
            self.x =0
        if pos[2]>=self.canvas_width:
            self.x =0
        
        
    def turn_left(self,event):
            self.x= -self.sensitivity
        
        
    def turn_right(self,event):
            self.x= self.sensitivity
                
paddle = Paddle(canvas,'blue',16)
ball = Ball(canvas,paddle,'red')

while 1:
    ball.draw(10)
    paddle.draw()
    global counter
    canvas.create_text(150,150,text="Score: " +str(counter),font=("calibri", 30), fill="#66FF99", anchor=E, tag="score")
    tk.update_idletasks()
    tk.update()
    time.sleep(0.1)
    canvas.delete("score")
       
     

    
