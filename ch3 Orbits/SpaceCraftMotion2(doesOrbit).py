from visual import *
'''p65'''
'''good, I managed to make the shit orbit, now I have to
figure out what went wrong with my previous program SpaceCraftMotion.py'''
#objects
ship=sphere(pos=(-10*6.4*10**6,0,0),
             radius=2*10**6,#exaggerated just to ba able to see it
             color=color.yellow,
            make_trail=True)
earth=sphere(pos=(0,0,0),
             radius=6.4*10**6,
             color=color.red,
             opacity=0.4)
#data and inintials
scalefactor=5
G=6.11*10**-11
m1=1500#ship mass
v1=vector(0,2*10**3 + 1000,0)
p1=v1*m1
m2=6*10**24#earth mass
p2=vector(0,0,0)
m3=7*10**22#moon mass
p3=vector(0,0,0)
#gravity equations and time
r=ship.pos-earth.pos
rhat=r/mag(r)
Fmag=G*m1*m2/mag(r)**2*scalefactor
F_on1=Fmag*(-rhat)
F_on2=-F_on1
t=0
deltat=10
#fucking arrows
force_v=arrow(pos=(ship.pos),
              axis=(F_on1 * scalefactor),
              color=color.green,
              opacity=1)
p1_vector=arrow(pos=(ship.pos),
                axis=(p1*scalefactor),
                color=color.blue,
                opacity=0.5)
#the loop
while True:
    rate(100)
    r=ship.pos-earth.pos#update distance each loop
    rhat=r/mag(r)
    Fmag=G*m1*m2/mag(r)**2*scalefactor#update the force magnitude
    F_on1=Fmag*(-rhat)#update the force on 1 by two, then apply momentum principle for 
    p1=p1+F_on1*deltat
    ship.pos=ship.pos+(p1/m1)*deltat
    #arrow momentum updates
    p1_vector.pos=ship.pos
    p1_vector.axis=p1*scalefactor
    #force arrow updates
    force_v.pos=ship.pos
    force_v.axis=F_on1*scalefactor*10**3
