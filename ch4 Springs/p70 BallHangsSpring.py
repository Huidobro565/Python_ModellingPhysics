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
radiusBall=0.02
ball=sphere(pos=(0,spring.axis.y - (radiusBall/2), 0),
            radius=radiusBall,
            color=color.orange,
            opacity=0.2)
#data
L0=20*10**-2#m
ks=0.9 #N/m
m=20*10**-3#kg
v=vector(0,0,0)
p=m*v
t=0
dt=0.01
F_grav=vector(0,-9.8,0)
while True:
    rate(1)
    L=ball.pos-spring.pos
    Lhat=L/mag(L)
    s=mag(L)-L0 #stretch may be + or -
    F_spring=vector(-ks*s*Lhat)
    F_net=F_spring+F_grav
    '''momentum principle for motion:Fnet, update momentum,update position'''
    pf=vector(p+F_net*dt)
    ball.pos=ball.pos+(pf/m)*dt
    spring.axis=ball.pos
    p=pf#for the loop
    t=t+dt
    
    
