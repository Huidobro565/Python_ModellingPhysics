from visual import*
#objects
floor=box(pos=(0,-5,0),
          size=(10,0.1,10),
          color=color.yellow)
wallR=box(pos=(5,0,0),
          size=(0.1,10,10),
          color=color.yellow)
wallL=box(pos=(-5,0,0),
          size=(0.1,10,10),
          color=color.yellow)
wall3=box(pos=(0,0,-5),
          size=(10,10,0.1),
          color=color.yellow)
ceiling=box(pos=(0,5,0),
          size=(10,0.1,10),
          color=color.yellow)
ball=sphere(pos=(0,0,2),
            radius=0.5,
            color=color.red)
spring_floor=helix(pos=floor.pos,
                   axis=ball.pos-floor.pos,
                   radius=0.25,
                   color=color.blue,
                   thickness=0.25/7,
                   coils=10)
spring_wallR=helix(pos=wallR.pos,
                   axis=ball.pos-wallR.pos,
                   radius=0.25,
                   color=color.blue,
                   thickness=0.25/7,
                   coils=10)
spring_wallL=helix(pos=wallL.pos,
                   axis=ball.pos-wallL.pos,
                   radius=0.25,
                   color=color.blue,
                   thickness=0.25/7,
                   coils=10)
spring_wall3=helix(pos=wall3.pos,
                   axis=ball.pos-wall3.pos,
                   radius=0.25,
                   color=color.blue,
                   thickness=0.25/7,
                   coils=10)
spring_ceiling=helix(pos=ceiling.pos,
                   axis=ball.pos-ceiling.pos,
                   radius=0.25,
                   color=color.blue,
                   thickness=0.25/7,
                   coils=10)
spring=helix(pos=(0,0,5),
             axis=ball.pos-(0,0,5),
             radius=0.25,
             color=color.blue,
             thickness=0.25/7,
             coils=10)
#data, all springs similar
L0=5
ks=30
m=1
vi=vector(10,0,0)
pi=vi*m
t=0
dt=0.01

while True:
    rate(100)
    # L for all springs
    L_floor=ball.pos-spring_floor.pos
    L_wallR=ball.pos-spring_wallR.pos
    L_wallL=ball.pos-spring_wallL.pos
    L_wall3=ball.pos-spring_wall3.pos
    L_ceiling=ball.pos-spring_ceiling.pos
    L_spring=ball.pos-spring.pos
    #Lhats
    Lhat_floor=L_floor/mag(L_floor)
    Lhat_wallR=L_wallR/mag(L_wallR)
    Lhat_wallL=L_wallL/mag(L_wallL)
    Lhat_wall3=L_wall3/mag(L_wall3)
    Lhat_ceiling=L_ceiling/mag(L_ceiling)
    Lhat_spring=L_spring/mag(L_spring)
    #s's
    s_floor=mag(L_floor)-L0
    s_wallR=mag(L_wallR)-L0
    s_wallL=mag(L_wallL)-L0
    s_wall3=mag(L_wall3)-L0
    s_ceiling=mag(L_ceiling)-L0
    s_spring=mag(L_spring)-L0
    #forces each spring
    F_floor=-ks*mag(L_floor)*Lhat_floor
    F_wallR=-ks*mag(L_wallR)*Lhat_wallR
    F_wallL=-ks*mag(L_wallL)*Lhat_wallL
    F_wall3=-ks*mag(L_wall3)*Lhat_wall3
    F_ceiling=-ks*mag(L_ceiling)*Lhat_ceiling
    F_spring=-ks*mag(L_spring)*Lhat_spring
    #momentum principle,Fnet, momentum,position
    F_net=F_floor+F_wallR+F_wallL+F_wall3+F_ceiling+F_spring
    pf=pi+F_net*dt
    ball.pos=ball.pos+(pf/m)*dt
    #update position of axis of all springs
    spring_floor.axis=ball.pos-floor.pos
    spring_floor.axis=ball.pos-floor.pos
    spring_wallR.axis=ball.pos-wallR.pos
    spring_wallL.axis=ball.pos-wallL.pos
    spring_wall3.axis=ball.pos-wall3.pos
    spring_ceiling.axis=ball.pos-ceiling.pos
    spring.axis=ball.pos-spring.pos
    pi=pf
    t=t+dt




















