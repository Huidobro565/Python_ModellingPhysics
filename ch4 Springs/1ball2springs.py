from visual import*
from visual.graph import*
radiusBall=0.50
ball=sphere(pos=(0,0,0),
            radius=radiusBall,
            color=color.yellow,
            opacity=0.5,
            make_trail=True)
wallR=box(pos=(10,0,0),
          size=(0.01,3,3),
          color=color.green,
          opacity=0.7)
wallL=box(pos=(-10,0,0),
          size=(0.01,3,3),
          color=color.green,
          opacity=0.7)
springL=helix(pos=wallL.pos,
              axis=ball.pos-wallL.pos,
              radius=0.25,
              coils=20,
              color=color.orange)
springR=helix(pos=wallR.pos,
              axis=ball.pos-wallR.pos,
              radius=0.25,
              coils=20,
              color=color.orange)
#graph object
gd = gdisplay(title='F_netvs. t', xtitle='t', ytitle='FNet')
f1=gcurve(color=color.yellow)
#data,no gravity
L0_l=3#m
L0_r=3
ks_l=10 #N/m
ks_r=10
m=1#kg
vi=vector(-10,0,0)
pi=m*vi
t=0
dt=0.01
while True:   #_l and _r mean left and right
    rate(2000)
    '''left sprint'''
    L_l=ball.pos-springL.pos#vector L Left
    Lhat_l=L_l/mag(L_l)
    s_l=mag(L_l)-L0_l #stretch may be + or -
    F_springL=-ks_l*s_l*Lhat_l#force of the springL on ball
    '''right spring'''
    L_r=ball.pos-springR.pos#vector L Left
    Lhat_r=L_r/mag(L_r)
    s_r=mag(L_r)-L0_r #stretch may be + or -
    F_springR=-ks_r*s_r*Lhat_r#force of the springL on ball
    '''force net'''
    F_net=F_springL+F_springR
    print("springL: ",F_springL.x,"springR: ",F_springR.x,"forceNet",F_net.x)
    f1.plot(pos=(t,F_net.x))
    '''momentum principle for motion:Fnet, update momentum,update position'''
    pf=vector(pi+F_net*dt)
    ball.pos=ball.pos+(pf/m)*dt
    springR.axis=ball.pos-wallR.pos
    springL.axis=ball.pos-wallL.pos
    pi=pf#for the loop
    t=t+dt
