from visual import *
from visual.graph import*
'''base code ch 3 p66 but removing the moon.
Goal is to code plots of the energies and analyze graph in elliptical and
circular orbits. Found: circular orbits have nearly constant K and U due to
constant distance'''
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
v1=vector(0,3*10**3,0)#very circular with (0,2.4*10**3,0)
'''observation with circular orbit: K and U are kinda constant because
the distance is the same, no fluctuation in value of potential and change
in kinetic energy'''
p1=v1*m1
m2=6*10**24#earth mass
p2=vector(0,0,0)
#gravity equations and time, interaction of planet and ship
r=ship.pos-earth.pos
rhat=r/mag(r)
Fmag=G*m1*m2/mag(r)**2#*scalefactor
F_on1=Fmag*(-rhat)#force on ship by planet
F_on2=-F_on1
t=0
deltat=60
#force net vector and all it requires, we have the two vectors, just add them toguether.
F_net=F_on1
#trying to visualize center of grav
centerOfGravity=sphere(pos=F_net,
                       radius=2*10**6,
                       color=color.red,
                       opacity=1)
'''all graphs in one window. Got the desired constant K+U'''
allgraphs = gdisplay(x=450, y=0, width=600, height=600,
                     title='Kcyan,Ugreen and K+Uyelllow', xtitle='t or r, look at code', ytitle='K,U,K+U')
kineticenergy=gcurve(color=color.cyan)
potentialenergy=gcurve(color=color.green)
kplusu=gcurve(color=color.yellow)


while True:
    rate(400)
    '''interaction with earth'''
    r=ship.pos-earth.pos#update distance each loop
    rhat=r/mag(r)
    Fmag=G*m1*m2/mag(r)**2#*scalefactor#update the force magnitude
    F_on1=Fmag*(-rhat)#update the force on 1 by two, then apply momentum principle for 
    p1=p1+F_on1*deltat
    ship.pos=ship.pos+(p1/m1)*deltat
    #update force net
    F_net=F_on1
    '''specific to this problem:plot the energy graphs'''
    #calculate kinetic energy
    K=((mag(p1))**2 )/ (2*m1) #K=mv^2 or p^2/2m if v<<c
    #calculate potential energy 
    U=-G*((m1*m2)/mag(r))
    #calculate sum of bothenergies
    #print("K:",K,"U:",U,"K+U:",(K+U))
    
    #graph both energies vs time
    kineticenergy.plot(pos=(t,K))#cyan
    potentialenergy.plot(pos=(t,U))#green
    kplusu.plot(pos=(t,(K+U)))#yellow
    '''
    #graph all energies vs r
    kineticenergy.plot(pos=(mag(r),K))#cyan
    potentialenergy.plot(pos=(mag(r),U))#green
    kplusu.plot(pos=(mag(r),(K+U)))#yellow ( maybe should be constant,its not)
    '''
    t=t+deltat#for the loop
    










    

