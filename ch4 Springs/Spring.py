'''spring'''
from visual import*
from visual.graph import *
#Objects
floor=box(pos=(0,0,0),
          size=(0.25,0.25,0.001),
          color=color.green,
          opacity=0.7)
spring=helix(pos=(0,0,0),
             axis=(0,0,10*10**-2),
             radius=0.025,
             coils=15)
block=box(pos=(0,0,spring.axis.z),
          size=(0.08,0.08,0.02),
          color=color.orange,
          opacity=0.2)
#graphs
gd = gdisplay(title='z vs t', xtitle='t', ytitle='z')
f1 = gcurve(color=color.cyan)
gd2=gdisplay(title="force vs time", xtitle="t", ytitle="springforce")
f2=gcurve(color=color.yellow)
#initial data
L0=20*10**-2 #relaxed 20 cm long
ks=8*2    #8N/m stiffness
m=1*10**-3 #60 grams
#from book: the forces and eqns
L=block.pos-spring.pos  
Lhat=L/mag(L)
s=mag(L)-L0     #stretch, may be + or -
F_spring=-ks * s * Lhat
F_grav=vector(0,0,-9.8) * m
t=0
dt=0.01
while True:
    rate(100)
    L=block.pos-spring.pos  #spring stretched
    Lhat=L/mag(L)
    s=mag(L)-L0     #stifness
    F_spring=-ks * s * Lhat
    F_total=F_spring+F_grav
    '''momentum principle'''
    block.pos=block.pos+F_total*dt
    spring.axis=block.pos
    print(spring.axis)
    f1.plot(pos=(t, block.pos.z))
    f2.plot(pos=(t,mag(F_spring)))
    t=t+dt#mainly to be a able to graph it otherwise time never increases
    print(mag(F_spring))
    if(mag(F_spring) < 0.010):
        print("time is: ", t)
        break
