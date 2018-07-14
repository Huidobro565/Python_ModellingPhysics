from visual import *
'''p57 ch 5 from base code of p65 ch 3'''
'''shit going on with scalefactors, the perpendicular and paraell
forces are hard to display apparently due to their magnitudes.
Good, I managed to scale and see everything'''
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
scaledownMomentum=0.5
scalefactor=5
G=6.11*10**-11
m1=1500#ship mass
v1=vector(0,2*10**3 + 1000,0)
p1=v1*m1
m2=6*10**24#earth mass
p2=vector(0,0,0)
#gravity equations and time
r=ship.pos-earth.pos
rhat=r/mag(r)
Fmag=G*m1*m2/mag(r)**2*scalefactor
F_on1=Fmag*(-rhat)
F_on2=-F_on1
t=0
deltat=10
#fucking arrows
force_v=arrow(pos=(ship.pos),#force net
              axis=(F_on1 * scalefactor),
              color=color.green,
              opacity=1)
p1_vector=arrow(pos=(ship.pos),
                axis=(p1*scalefactor),
                color=color.blue,
                opacity=0.2)
#adding to this previous program,exclusive of p57:
p1_hat=norm(p1)
F_para=dot(F_on1, p1_hat)*p1_hat
F_perp=F_on1-F_para
force_paralell=arrow(pos=(ship.pos),
              axis=(F_para * scalefactor),
              color=color.cyan,
              opacity=0.3)
force_perpendicular=arrow(pos=(ship.pos),
              axis=(F_perp * scalefactor),
              color=color.orange,
              opacity=0.5)
#the loop
while True:
    rate(300)
    r=ship.pos-earth.pos#update distance each loop
    rhat=r/mag(r)
    Fmag=G*m1*m2/mag(r)**2*scalefactor#update the force magnitude
    F_on1=Fmag*(-rhat)#update the force on 1 by two, then apply momentum principle for 
    #p1=p1+F_on1*deltat
    #ship.pos=ship.pos+(p1/m1)*deltat
    #arrow momentum updates
    p1_vector.pos=ship.pos
    p1_vector.axis=p1*scalefactor*scaledownMomentum
    #force net arrow updates
    force_v.pos=ship.pos
    force_v.axis=F_on1*scalefactor*10**3
    #update paralell and perpendicular force arrows: exclusive of this problem
    #problem: not visualizing them
    p1_hat=norm(p1)
    F_para=dot(F_on1, p1_hat)*p1_hat
    F_perp=F_on1-F_para
    force_paralell.pos=ship.pos
    force_paralell.axis=F_para * scalefactor**6
    force_perpendicular.pos=ship.pos
    force_perpendicular.axis=F_perp * scalefactor**6
    #update for the loop
    p1=p1+F_on1*deltat
    ship.pos=ship.pos+(p1/m1)*deltat





    
