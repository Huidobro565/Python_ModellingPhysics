from visual import *
sun=sphere(pos=(0,0,0),
             radius=695508*10**3,
             color=color.yellow,
            )
mars=sphere(pos=(0,-227.9*10**9,0),
             radius=3390*10**3,
             color=color.red,
             opacity=0.4,
            make_trail=True)
'''
#masses and initial data
m1=1.989*10**33
m2=6.39*10**26
scalefactor=5
G=6.11*10**-11
v1=vector(0,0,0)
p1=v1*m1
v2=vector(0,0,0)
p2=v2*m2
#gravity equations and time, interaction of planet and sun
r=mars.pos-sun.pos
rhat=r/mag(r)
Fmag=G*m1*m2/mag(r)**2*scalefactor
F_on1=Fmag*(-rhat)
F_on2=-F_on1
t=0
deltat=60
#fucking arrows earth ship
force_v=arrow(pos=(mars.pos),
              axis=(F_on1 * scalefactor),
              color=color.green,
              opacity=1)
p1_vector=arrow(pos=(mars.pos),
                axis=(p1*scalefactor),
                color=color.blue,
                opacity=0.5)
while True:
    rate(10000)
    
    r=mars.pos-sun.pos#update distance each loop
    rhat=r/mag(r)
    Fmag=G*m1*m2/mag(r)**2*scalefactor#update the force magnitude
    F_on1=Fmag*(-rhat)#update the force on 1 by two, then apply momentum principle for 
    p1=p1+F_on1*deltat
    mars.pos=mars.pos+(p1/m1)*deltat
    #arrow momentum updates
    p1_vector.pos=mars.pos
    p1_vector.axis=p1*scalefactor
    #force arrow updates
    force_v.pos=mars.pos
    force_v.axis=F_on1*scalefactor*10**2
'''
