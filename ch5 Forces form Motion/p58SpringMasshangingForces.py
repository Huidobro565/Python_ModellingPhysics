'''p58 iwth base code from ch 4'''
from visual import*
floor=box(pos=(0,0,0),
          size=(0.25,0.01,0.25),
          color=color.green,
          opacity=0.7)
spring=helix(pos=(0,0,0),
             axis=(0,-20*10**-2,0),
             radius=0.01,
             coils=25,
             thickness=0.01/10,
             color=color.yellow)
radiusBall=0.02
ball=sphere(pos=(0,spring.axis.y - 2*(radiusBall/2), 0),
            radius=radiusBall,
            color=color.red,
            opacity=0.5,
            make_trail=True,
            retain=40)
Fspring_v=arrow(pos=ball.pos,
                axis=(0,0,0),#just to initialize
                color=color.orange,
                opacity=0.5)
Fnet_v=arrow(pos=ball.pos,
             axis=(0,0,0),#just to initialize
             color=color.blue,
             opacity=1)
Fnet_para=arrow(pos=ball.pos,
             axis=(0,0,0),#just to initialize
             color=color.cyan,
             opacity=1)
Fnet_perp=arrow(pos=ball.pos,
             axis=(0,0,0),#just to initialize
             #color=color.blue,
             opacity=1)
#data
L0=20*10**-2#m
ks=100 #N/m
m=230*10**-3#kg
v=vector(1,0,0)
p=m*v
t=0
dt=0.01
F_grav=vector(0,-9.8,0)
scaleDownForce=10**-2
while True:
    rate(25)
    L=ball.pos-spring.pos
    Lhat=L/mag(L)
    s=mag(L)-L0 #stretch may be + or -
    F_spring=-ks*s*Lhat
    F_net=F_spring+F_grav
    '''momentum principle for motion:Fnet, update momentum,update position'''
    pf=vector(p+F_net*dt)
    ball.pos=ball.pos+(pf/m)*dt
    spring.axis=ball.pos
    #update the force vectors
    Fspring_v.pos=ball.pos
    Fspring_v.axis=F_spring*scaleDownForce
    Fnet_v.pos=ball.pos
    Fnet_v.axis=F_net*scaleDownForce
    '''Net force perpendicular and paralell components'''
    phat=norm(p)
    Fpara=dot(F_net,phat)*phat
    Fperp=F_net-Fpara
    #update arrows for Fparalell and Fperpendicular
    Fnet_para.pos=ball.pos
    Fnet_para.axis=Fpara*scaleDownForce
    Fnet_perp.pos=ball.pos
    Fnet_perp.axis=Fperp*scaleDownForce
    p=pf#for the loop
    t=t+dt
    
    
