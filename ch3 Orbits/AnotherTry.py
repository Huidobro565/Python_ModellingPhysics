from visual import *
'''nice orbit'''
ship=sphere(pos=(-10*6.4*10**6,0,0),
             radius=2*10**6,
             color=color.yellow,
            make_trail=True)
earth=sphere(pos=(0,0,0),
             radius=6.4*10**6,
             color=color.red,
             opacity=0.4)
scalefactor=5
G=6.11*10**-11
m1=1500
v1=vector(0,2*10**3,0)
p1=v1*m1
m2=6*10**24
p2=vector(0,0,0)

r=ship.pos-earth.pos
rhat=r/mag(r)
Fmag=G*m1*m2/mag(r)**2*scalefactor
F_on1=Fmag*(-rhat)
F_on2=-F_on1
t=0
deltat=60

while True:
    rate(100)
    r=ship.pos-earth.pos#update distance each loop
    rhat=r/mag(r)
    Fmag=G*m1*m2/mag(r)**2*scalefactor#update the force magnitude
    F_on1=Fmag*(-rhat)#update the force on 1 by two, then apply momentum principle for 1
    p1=p1+F_on1*deltat
    ship.pos=ship.pos+(p1/m1)*deltat
