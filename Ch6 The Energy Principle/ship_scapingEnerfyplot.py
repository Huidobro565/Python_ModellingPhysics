from visual import *
from visual.graph import*
import math
'''in this program the ship will try to scape from surface of earth,
Remember that scape velocity is when K+U is 0 at least. Goal is K+U to be
positive so that it can be a UNbound system and the potential doesnt trap
the ship and doesnt let it scape'''
'''K+U at least equal to zero to scape. That means
K+U=0, K=-U, 1/2 mv^2 = -U,...solve for v and you have the equation that
solves for minimun v to scape.'''

#objects
ship=sphere(pos=(0,1*6.4*10**6,0),#starts at surface of earth
             radius=2*10**6,#exaggerated just to ba able to see it
             color=color.yellow,
            make_trail=True)
earth=sphere(pos=(0,0,0),
             radius=6.4*10**6,
             color=color.red,
             opacity=0.4)
#some data
G=6.11*10**-11
m1=1500#ship mass
#v1=vector(0,3*10**4,0)
#p1=v1*m1
m2=6*10**24#earth mass
#v2=vector(0,0,0)
#p2=v2*m2
#gravity equations and time
r=ship.pos-earth.pos
rhat=r/mag(r)
Fmag=G*m1*m2/mag(r)**2#*scalefactor
F_on1=Fmag*(-rhat)
F_on2=-F_on1
t=0
deltat=10
#Plot initializers
allgraphs = gdisplay(title='Kcyan,Ugreen and K+Uyellow', xtitle='t or r, look at your code', ytitle='K,U,K+U')
kineticenergy=gcurve(color=color.cyan)
potentialenergy=gcurve(color=color.green)
kplusu=gcurve(color=color.yellow)
#initial velocity and momentum
U=-(G*m1*m2)/(mag(r))
scapeVelocity=math.sqrt(-U*2 / m1)#WORKS! SHIP SCAPED! and it didnt even have propulsion,
print("scape velocity is", scapeVelocity)#apparenlty just initial velocity
v1=vector(0,scapeVelocity,0)
p1=v1*m1
v2=vector(0,0,0)
p2=v2*m2
while True:
    rate(200)
    r=ship.pos-earth.pos#update distance each loop
    rhat=r/mag(r)
    Fmag=G*m1*m2/mag(r)**2
    F_on1=Fmag*(-rhat)#update the force on 1 by two, then apply momentum principle for 
    F_on2=-F_on1
    p1=p1+F_on1*deltat
    p2=p2+F_on2*deltat
    ship.pos=ship.pos+(p1/m1)*deltat
    earth.pos=earth.pos+(p2/m2)*deltat#works great
    #K and U
    deltaKship= (mag(p1)**2)/(2*m1)
    deltaKearth= (mag(p2)**2)/(2*m2)
    deltaKsystem=deltaKship+deltaKearth
    deltaUsystem=-(G*m1*m2)/(mag(r))
    O=deltaKsystem+deltaUsystem#just assinging to a variable.
    
    #plot vs t
    kineticenergy.plot(pos=(t,deltaKsystem))
    potentialenergy.plot(pos=(t,deltaUsystem))
    kplusu.plot(pos=(t,O))#I cannot make it be constant as supposed
    '''
    #plot vs r
    kineticenergy.plot(pos=(mag(r),deltaKsystem))
    potentialenergy.plot(pos=(mag(r),deltaUsystem))
    kplusu.plot(pos=(mag(r),O))
    '''
    if(mag(ship.pos) < 6.4*10**6):#works wonders for any direction
        break
    t=t+deltat
print("end of program")
