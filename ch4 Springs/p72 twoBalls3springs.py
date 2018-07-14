from visual import*
#from visual.graph import*
'''bug pending, maybe I dont know how to add the force of the middle
spring to a realistic situation'''
radiusBall=0.50
ballL=sphere(pos=(-3,0,0),
            radius=radiusBall,
            color=color.yellow,
            opacity=0.5,
            make_trail=True)
ballR=sphere(pos=(5,0,0),
            radius=radiusBall,
            color=color.cyan,
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
springM=helix(pos=ballL.pos,
             axis=ballR.pos-ballL.pos,
             color=color.blue,
             radius=0.25,
             coils=20)
springL=helix(pos=wallL.pos,
              axis=ballL.pos-wallL.pos,
              radius=0.25,
              coils=20,
              color=color.orange)
springR=helix(pos=wallR.pos,
              axis=ballR.pos-wallR.pos,
              radius=0.25,
              coils=20,
              color=color.red)
#graph object
'''
gd = gdisplay(title='F_netvs. t', xtitle='t', ytitle='FNet')
f1=gcurve(color=color.yellow)
'''
#data,no gravity
L0_l=3#m
L0_r=3
L0_m=3
ks_l=2 #N/m
ks_r=3
ks_m=4
m_r=1#kg
m_l=1
vi_r=vector(-1,0,0)
pi_r=m_r*vi_r
vi_l=vector(0,0,0)
pi_l=m_l*vi_l
t=0
dt=0.01
while True:   #_l and _r mean left and right
    rate(100)
    '''left sprint'''
    L_l=ballL.pos-springL.pos#vector L Left
    Lhat_l=L_l/mag(L_l)
    s_l=mag(L_l)-L0_l #stretch may be + or -
    F_springL=-ks_l*s_l*Lhat_l#force of the springL on ball
    '''right spring'''
    L_r=ballR.pos-springR.pos#vector L Left
    Lhat_r=L_r/mag(L_r)
    s_r=mag(L_r)-L0_r #stretch may be + or -
    F_springR=-ks_r*s_r*Lhat_r#force of the springL on ball
    '''middle spring'''
    L_m=ballR.pos-ballL.pos
    Lhat_m=L_m/mag(L_m)
    s_m=mag(L_m)-L0_m
    F_springM=-ks_m*s_m*Lhat_m
    ''''''#force net of each ball''''''
    F_netR=F_springL+F_springR+F_springM
    F_netL=F_springL+F_springR+F_springM
    #print("springL: ",F_springL.x,"springR: ",F_springR.x,"forceNet",F_net.x)
    #f1.plot(pos=(t,F_net.x))
    ''''''#momentum principle for motion, for each ball:Fnet, update momentum,update position''''''
    #Right
    pf_r=vector(pi_r+F_netR*dt)
    ballR.pos=ballR.pos+(pf_r/m_r)*dt
    springR.axis=ballR.pos-wallR.pos
    pi_r=pf_r
    #Left
    pf_l=vector(pi_l+F_netL*dt)
    ballL.pos=ballL.pos+(pf_l/m_l)*dt
    springL.axis=ballL.pos-wallL.pos
    pi_l=pf_l

    springM.pos=ballL.pos
    springM.axis=ballR.pos-ballL.pos
    
    t=t+dt#loop
    
