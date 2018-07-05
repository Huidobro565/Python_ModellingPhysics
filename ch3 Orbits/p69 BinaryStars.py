'''p69, binary stars'''
from visual import*
'''i have to give exponential speeds for it to work.Kinda have
to figure out why'''
#data
sun_radius=695500000 
m1=1.989*10**30 
star_radius=3390000*2
m2=m1/2#m1/10'''interesting the masses vary the way it orbits'''
star_sunD=227*10**9
#scalefactors
scalesizesun=10**2
scalesizestar=10**3
forcefactor=10**12
#initial conditions
G=6.11*10**-11
v1=vector(0,-24*10**8,0)
p1=v1*m1
v2=vector(0,240*10**8,0)
p2=v2*m2
#objects
sun=sphere(pos=(0,0,0),
             radius=sun_radius*scalesizesun,
             color=color.yellow,
             opacity=0.5,
             make_trail=True)
star=sphere(pos=(star_sunD,0,0),
             radius=star_radius*scalesizestar,
             color=color.red,
             opacity=1,
             make_trail=True)
#forces and equations interactions sun mars
r=star.pos-sun.pos #2-1
rhat=r/mag(r)
Fmag=(G*m1*m2/mag(r)**2) * forcefactor
F_on2by1=Fmag*(-rhat)
F_on1by2=-F_on2by1
t=0
deltat=1
#arrow
sunstarr_vector=arrow(pos=sun.pos,
                      axis=r,
                      color=color.green,
                      opacity=0.1,
                      shaftwidth=0.01*mag(r))
while True:
    rate(40)
    r=star.pos-sun.pos#update distance each loop
    rhat=r/mag(r)
    Fmag=G*m1*m2/mag(r)**2#update the force magnitude
    F_on2by1=Fmag*(-rhat)*forcefactor#update the force on 1 by two, then apply momentum principle for 
    p2=p2+F_on2by1*deltat
    star.pos=star.pos+(p2/m2)*deltat
    F_on1by2=-F_on2by1
    p1=p1+F_on1by2*deltat
    sun.pos=sun.pos+(p1/m1)*deltat
    
