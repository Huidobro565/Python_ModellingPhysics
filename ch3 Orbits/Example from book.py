'''from the book'''
from visual import *
rock1=sphere(pos=(5,5,0),
             radius=0.5,
             color=color.yellow)
rock2=sphere(pos=(-5,-5,0),
             radius=1,
             color=color.red,
             opacity=0.4)
scalefactor=10**12
G=6.11*10**-11
m1=1
p1=vector(-2,0,0)
m2=2
p2=vector(+2,0,0)
'''#maybe this part can me ommited as it is on the while loop
r=rock1.pos-rock2.pos
rhat=r/mag(r)
Fmag=G*m1*m2/mag(r)**2*scalefactor
F_on1=Fmag*(-rhat)
F_on2=-F_on1
'''
t=0
deltat=0.01
while True:
    rate(100)
    r=rock1.pos-rock2.pos
    rhat=r/mag(r)
    Fmag=G*m1*m2/mag(r)**2*scalefactor
    F_on1=Fmag*(-rhat)
    p1=p1+F_on1*deltat
    rock1.pos=rock1.pos+(p1/m1)*deltat
    F_on2=-F_on1
    p2=p2+F_on2*deltat
    rock2.pos=rock2.pos+(p2/m2)*deltat

