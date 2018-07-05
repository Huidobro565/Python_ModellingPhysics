from visual import *
'''p66'''
'''now with the moon'''
#objects
ship=sphere(pos=(-10*6.4*10**6,0,0),
             radius=2*10**6,#exaggerated just to ba able to see it
             color=color.yellow,
            make_trail=True)
earth=sphere(pos=(0,0,0),
             radius=6.4*10**6,
             color=color.red,
             opacity=0.4)
moon=sphere(pos=(4*10**8,0,0),
             radius=1.75*10**6,
             color=color.cyan,
             opacity=1)
#data and inintials
scalefactor=5
G=6.11*10**-11
m1=1500#ship mass
v1=vector(0,2*10**3+1000,2*10**3)
p1=v1*m1
m2=6*10**24#earth mass
p2=vector(0,0,0)
m3=7*10**22#moon mass
p3=vector(0,0,0)
#gravity equations and time, interaction of planet and ship
r=ship.pos-earth.pos
rhat=r/mag(r)
Fmag=G*m1*m2/mag(r)**2*scalefactor
F_on1=Fmag*(-rhat)#force on ship by planet
F_on2=-F_on1
t=0
deltat=60
#interaction of ship and moon
r_13=ship.pos-moon.pos
rhat_13=r_13/mag(r_13)
Fmag13=G*m1*m3/mag(r_13)**2*scalefactor
F_13=Fmag13*(-rhat_13)
#fucking arrows earth ship
force_v=arrow(pos=(ship.pos),
              axis=(F_on1 * scalefactor),
              color=color.green,
              opacity=1)
p1_vector=arrow(pos=(ship.pos),
                axis=(p1*scalefactor),
                color=color.blue,
                opacity=0.5)
#arrows ship moon
force13_v=arrow(pos=(ship.pos),
              axis=(F_13 * scalefactor),
              color=color.cyan,
              opacity=0.2)
p13_vector=arrow(pos=(ship.pos),
                axis=(p3*scalefactor),
                color=color.cyan,
                opacity=0.2)
#force net vector and all it requires, we have the two vectors, just add them toguether.
F_net=F_on1+F_13
F_netArrow=arrow(pos=ship.pos,
                  axis=(F_net),
                  color=color.orange)
#trying to visualize center of grav
centerOfGravity=sphere(pos=F_net,
                       radius=2*10**6,
                       color=color.yellow)
print(centerOfGravity.pos-earth.pos)
#the loop
while True:
    rate(10000)
    '''interaction with earth'''
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
    force_v.axis=F_on1*scalefactor*10**2
    '''interaction with moon'''
    r_13=ship.pos-moon.pos
    rhat_13=r_13/mag(r_13)
    Fmag13=G*m1*m3/mag(r_13)**2*scalefactor
    F_13=Fmag13*(-rhat_13)#update the force on 1 by two, then apply momentum principle for 
    p3=p3+F_13*deltat
    ship.pos=ship.pos+(p3/m3)*deltat
    #arrow momentum updates moon earth
    p13_vector.pos=ship.pos
    p13_vector.axis=p3*scalefactor#***BUG***:for some reason(anser: because force net from moon is never on the opposite direction) this arrow grows over time
    #force arrow updates moon earth
    force13_v.pos=ship.pos
    force13_v.axis=F_13*scalefactor*10**8
    #update force net
    F_net=F_on1+F_13
    F_netArrow.pos=ship.pos
    F_netArrow.axis=F_net*scalefactor*10**3
    










    
