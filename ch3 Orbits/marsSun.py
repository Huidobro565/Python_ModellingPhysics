'''p68, mars and the sun'''
'''mars orbit period is:687 days, I should calc initial speed from this:
24027.7m/s. THIS SPEED IS RIGTH, so there has to be something wron in the
coding because at this speed it mars doesnt even orbit. It has to be an
extreme speed for it to '''
'''something kinda wrong with my initial speed'''
from visual import*
#data
sun_radius=695500000 
m1=1.989*10**30 
mars_radius=3390000
m2=6.39*10**23
mars_sunD=227*10**9
#scalefactors
scalesizesun=10**2
scalesizemars=10**3
forcefactor=10**12
#initial conditions
G=6.11*10**-11
v1=vector(0,0,0)
p1=v1*m1
v2=vector(0,24027.7*10**6,0)
p2=v2*m2
#objects
sun=sphere(pos=(0,0,0),
             radius=sun_radius*scalesizesun,
             color=color.yellow,
             opacity=0.5)
mars=sphere(pos=(mars_sunD,0,0),
             radius=mars_radius*scalesizemars,
             color=color.red,
             opacity=1,
             make_trail=True)
#forces and equations interactions sun mars
r=mars.pos-sun.pos #2-1
rhat=r/mag(r)
Fmag=(G*m1*m2/mag(r)**2) * forcefactor
F_on2by1=Fmag*(-rhat)
F_on1by2=-F_on2by1
t=0
deltat=1
#arrow
sunmarsr_vector=arrow(pos=sun.pos,
                      axis=r,
                      color=color.green,
                      opacity=0.1,
                      shaftwidth=0.01*mag(r))
while True:
    rate(10000)
    r=mars.pos-sun.pos#update distance each loop
    rhat=r/mag(r)
    Fmag=G*m1*m2/mag(r)**2#update the force magnitude
    print (Fmag)
    F_on2by1=Fmag*(-rhat)*forcefactor#update the force on 1 by two, then apply momentum principle for 
    p2=p2+F_on2by1*deltat
    mars.pos=mars.pos+(p2/m2)*deltat
    

