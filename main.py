import tkinter as tk
import time
import math


Width=800
Height=800
Length=10
point_color="#50ff50"
FPS=60

def translate(x:float,y:float):
    x_=(x+1)/2*Width
    y_=(-y+1)/2*Height
    return (x_,y_)

def Point(p:tuple[float, float]):
    x_,y_=translate(p[0],p[1])
    x1=x_-Length/2
    x2=x_+Length/2
    y1=y_-Length/2
    y2=y_+Length/2
    return (x1,y1,x2,y2)

def Point_3D(x:float,y:float,z:float):
    x_=x/z
    y_=y/z
    return x_,y_

def delta_z(x:float,y:float,z:float,dz:float):
    return (x,y,z+dz)

def rotate_xz(x:float,y:float,z:float,angle):
    x_=x*math.cos(angle)-z*math.sin(angle)
    z_=x*math.sin(angle)+z*math.cos(angle)
    return x_, y, z_

class CanvasAnimation:
    def __init__(self,window:tk.Tk):
        self.window=window
        self.window.resizable(False, False)
        self.window.geometry('800x800')
        self.window.title("Rotating")

        self.stage=tk.Canvas(window, bg="black",width=Width, height=Height)
        self.stage.pack()

        self.start_time=time.time()
        self.Frame()

    dz=1
    angle=0
    frame_count=0

    points=(
        (0.25,0.25,0.25),
        (-0.25,0.25,0.25),
        (0.25,-0.25,0.25),
        (-0.25,-0.25,0.25),

        (0.25,0.25,-0.25),
        (-0.25,0.25,-0.25),
        (0.25,-0.25,-0.25),
        (-0.25,-0.25,-0.25),
    )

    faces=(
        (0,1,3,2),
        (4,5,7,6),
        (0,4),
        (5,1),
        (3,7),
        (6,2),
    )

    def Frame(self):
        self.frame_count+=1
        current_time=time.time()
        delta_time=current_time-self.start_time
        if delta_time>=1:
            fps_realtime=self.frame_count/delta_time
            print(f"FPS:{fps_realtime:.1f}")
            self.start_time=current_time
            self.frame_count=0


        self.stage.delete("all")
        dt=1/FPS
        # self.dz+=1*dt
        self.angle+=math.pi*dt

        """绘制点"""
        for point in self.points:
            self.stage.create_rectangle(Point(Point_3D(*delta_z(*rotate_xz(*point,self.angle),self.dz))),fill=point_color,outline=point_color)
        """绘制边"""
        for face in self.faces:
            for i in range(0,len(face)):
                a=self.points[face[i]]
                b=self.points[face[(i+1)%len(face)]]
                self.stage.create_line(*translate(*Point_3D(*delta_z(*rotate_xz(*a,self.angle),self.dz))),*translate(*Point_3D(*delta_z(*rotate_xz(*b,self.angle),self.dz))),fill="white",width=2)
        self.window.after(int(1000/FPS),self.Frame)



if __name__ == "__main__":
    window=tk.Tk()
    app=CanvasAnimation(window)
    window.mainloop()