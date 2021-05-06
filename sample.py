from tkinter import * 
from tkinter.ttk import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import*
from time import strftime

class clock:
    def __init__(self,root):
        self.root=root
        self.root.title("project")
        self.root.geometry("1350x700+0+0")
        self.root.config(background="#091921")
        self.title=Label(self.root,text="welcome")
        self.lbl=Label(self.root,background="red",border=20,relief=RAISED)
        self.lbl.place(x=750,y=250,height=400,width=400)
        self.label = Label(self.root, font=("ds-digital", 80), background="#091921", foreground="crimson")

        self.label.after(1000, time)

        self.working()
        self.time()

    def clock_img(self,hr,min,sec):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw =ImageDraw.Draw(clock)
        bg=Image.open("clock.jpg")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        clock.save("clock_new.jpg")

        orgin=200,200
        
        draw.line((orgin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),   fill="black", width=3 )
        draw.line((orgin, 200+ 80*sin(radians(min)), 200 - 80 * cos(radians(min))), fill="blue", width=3)
        draw.line((orgin,200+100*sin(radians(sec)),200-100*cos(radians(sec))),   fill="green", width=3 )
        #draw.ellipse((orgin,210,210),fill="black")


        clock.save("clock_new.jpg")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        print(h,m,s)
        hr=(h/12)*360
        min=(m/60)*360
        sec=(s/60*360)
        print(hr,min,sec)
        self.clock_img(hr,min,sec)
        self.img =ImageTk.PhotoImage(file="clock_new.jpg")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def time(self):
        string = strftime('%H:%M:%S %p')




        self.label.pack(anchor='center', padx='350px', pady='050px')
        root.configure(background='#091921')
        self.label.config(text=string)
        self.label.after(1000, time)







        
        









root=Tk()
obj=clock(root)
root.mainloop()



