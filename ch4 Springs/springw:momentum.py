'''spring, but this time with momentum'''
from visual import*
from visual.graph import *
#Objects
floor=box(pos=(0,0,0),
          size=(0.25,0.01,0.25),
          color=color.green,
          opacity=0.7)
spring=helix(pos=(0,0,0),
             axis=(0,10*10**-2,0),
             radius=0.025,
             coils=15)
block=box(pos=(0,spring.axis.y,0),
          size=(0.08,0.08,0.02),
          color=color.orange,
         opacity=0.2)

#graphs
gd = gdisplay(title='pos y vs t', xtitle='t', ytitle='y')
f1 = gcurve(color=color.cyan)
gd2=gdisplay(title="F_net vs time", xtitle="t", ytitle="F_net")
f2=gcurve(color=color.yellow)

#initial data
L0=20*10**-2 #relaxed 20 cm long
ks=8*10    #8N/m stiffness
m=1*10**-3 #60 grams
#from book: the forces and eqns
L=block.pos-spring.pos  
Lhat=L/mag(L)
s=mag(L)-L0     #stretch, may be + or -
F_spring=-ks * s * Lhat
F_grav=vector(0,-9.8,0) * m
v=vector(0,0,0)
p=m*v
t=0
dt=0.01
while True:
    '''i dont know why it never stops oscilating, i did put gravity'''
    rate(10)
    L=block.pos-spring.pos  #spring stretched
    Lhat=L/mag(L)
    s=mag(L)-L0     #stifness
    F_spring=-ks * s * Lhat
    F_net=F_spring+F_grav
    print("F_grav:",mag(F_grav),"F_spring:",mag(F_spring),"F_net:",F_net)
    '''momentum principle:but here I forgot the momentum'''
    p=p+F_net*dt
    block.pos=block.pos+(p/m)*dt
    spring.axis=block.pos
    print(spring.axis)
    
    f1.plot(pos=(t, block.pos.y))
    f2.plot(pos=(t,mag(F_net)))
    
    t=t+dt#mainly to be a able to graph it otherwise time never increases
    '''
    print(mag(F_spring))
    if(mag(F_spring) < 0.010):
        print("time is: ", t)
        break
    '''
