'''p45 ch 7 with base code p70 ch 4'''
'''observation: K+U oscilates(without grav,with grav is a complete mess),
I believe it should be constant but I still can't figure why it's not'''
'''change ball for flat so that modelling air resistance is easier for now'''
import math
from visual import*
from visual.graph import*

floor=box(pos=(0,0,0),
          size=(0.25,0.01,0.25),
          color=color.green,
          opacity=0.7)
spring=helix(pos=(0,0,0),
             axis=(0,-20*10**-2,0),
             radius=0.012,
             coils=25,
             color=color.yellow)
ball=cylinder(#pos=(0,spring.axis.y - (radiusBall/2), 0),#original, this was making it move without any push
            pos=(0,spring.axis.y,0),#good, now it doesnt move without momentum    
            axis=(0,-0.01,0),
            color=color.orange,
            radius=0.09,
            opacity=0.5,
            make_trail=True)
lengthSpring=arrow(pos=floor.pos,#just to visualize the relaxed spring length
                   axis=(0,-20*10**-2 ,0),#L0 below
                   color=color.blue,
                   opacity=0.2)
#data
'''specific to this problem you have to define some new variables'''
C=1#shape effect reflects sharpness or bluntness of object. this drag coefficient typically 0.3<C<1.0. I'll assume 1 is for completely blunt 
rho_air= 1.225#kg/m^3 density of the air
A_ball=math.pi * (ball.radius)**2#cross sectional area of the object
L0=20*10**-2#m
ks=100 #N/m
m=230*10**-3#kg original mass
v=vector(0,-0.5,0)
p=m*v
t=0
dt=0.01
F_grav=vector(0,-9.8,0)
#graphs
gd = gdisplay(x=420, y=0, width=500, height=500,
              title='K(yellow),U(red),K+U(orange)', xtitle='r or t, look at code', ytitle='K,U,K+U')
f1=gcurve(color=color.yellow)#K
f2=gcurve(color=color.red)#U
f3=gcurve(color=color.orange)#K+U
while True:
    rate(1000)
    #after the loop reinitiates I have a new p
    #specific to this problem
    v=p/m
    vhat=v/(mag(v))
    F_air=0.5*C*rho_air*A_ball*mag(v)**2 *(-vhat)
    #print(F_air)#works
    L=ball.pos-spring.pos
    Lhat=L/mag(L)
    s=mag(L)-L0 #stretch may be + or -
    #print(s)
    F_spring=-ks*s*Lhat
    F_net=F_spring+F_air+F_grav#often take oput gravity to test differences,gravity screws the graphs enormously

    pf=p+F_net*dt
    ball.pos=ball.pos+(pf/m)*dt
    spring.axis=ball.pos
    
    p=pf#for the loop
    t=t+dt


