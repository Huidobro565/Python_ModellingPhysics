from visual import*

table=box(pos=(0,0,0),
          size=(8,0.1,8),
          )
radiusBall=0.25
ball=sphere(pos=(0,radiusBall/2 + table.size.y * 2,2),#supposed to be the pos of the center of the ball
            radius=radiusBall,
            color=color.blue,
            make_trail=True)
rod=cylinder(pos=(0,0,0),
             axis=(0,0.5,0),
             radius=0.09,
             )
springRadius=0.2
spring=helix(pos=(0,ball.pos.y,0),
             axis=ball.pos-(0,ball.pos.y,0),
             #axis=ball.pos-rod.pos,#i dont know why this doesnt work
             radius=springRadius,
             coils=20,
             thickness=springRadius/10,
             color=color.yellow)
#constants and initia data
m=1
vi=vector(2,0,2)
pi=vi*m
L0=1
ks=10
t=0
dt=0.01
while True:
    rate(100)
    #spring eq: F=-ks*s*Lhat 
    #L=mag(spring.axis)-L0 #dont forget to upgrade axis later
    L=ball.pos-spring.pos
    Lhat=L/mag(L)
    s=mag(L)-L0
    F=-ks*s*Lhat
    #momentum principle:upgrade Fnet,momentum,position
    Fnet=F
    pf=pi+Fnet*dt
    ball.pos=ball.pos+(pf/m)*dt
    spring.axis=ball.pos-spring.pos
    pi=pf
    t=t+dt
    
    










    
