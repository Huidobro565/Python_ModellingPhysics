from visual import *
from visual.graph import*
'''nice orbits for 3 bodies with different initial speeds.
Energy graph look a lot different with 3 bodies. According to my code
K+U is sinusoidal'''
#objects
ship=sphere(pos=(-10*6.4*10**6,0,0),
             radius=2*10**6,#exaggerated just to ba able to see it
             color=color.yellow,
            make_trail=True,
            retain=3*10**4)
earth=sphere(pos=(0,0,0),
             radius=6.4*10**6,
             color=color.red,
             opacity=0.4)
moon=sphere(pos=(4*10**8,0,0),
             radius=1.75*10**6,
             color=color.cyan,
             opacity=1)
#data and inintials
G=6.11*10**-11
m1=1500#ship mass
v1=vector(0,2.8*10**3,0)
p1=v1*m1
m2=6*10**24#earth mass
p2=vector(0,0,0)
m3=7*10**22#moon mass
p3=vector(0,0,0)
t=0
deltat=60
'''all graphs in one window. Got the desired constant K+U'''
allgraphs = gdisplay(x=450, y=0, width=600, height=600,
                     title='Kcyan,Ugreen and K+Uyelllow', xtitle='t or r, look at code', ytitle='K,U,K+U')
kineticenergy=gcurve(color=color.cyan)
potentialenergy=gcurve(color=color.green)
kplusu=gcurve(color=color.yellow)


while True:
    rate(4000)
    '''interaction with earth'''
    r=ship.pos-earth.pos
    rhat=r/mag(r)
    Fmag=G*m1*m2/mag(r)**2
    F_on1=Fmag*(-rhat)#force on ship by planet
    '''integraction with moon'''
    r_moon=ship.pos-moon.pos#update distance each loop
    rhat_moon=r_moon/mag(r_moon)
    Fmag_moon=G*m1*m2/mag(r_moon)**2
    F_moonship=Fmag_moon*(-rhat_moon)
    '''update momentum and position of ship due to moon and earth'''
    F_net=F_on1+F_moonship  #when ignoring the influence of the moon its a constant orbit.
    p1=p1+F_net*deltat#when the moon is taken into account ship spirals into earth
    ship.pos=ship.pos+(p1/m1)*deltat
    '''specific to this problem:plot the energy graphs'''
    #ship-earth
    #calculate kinetic energy 
    K=((mag(p1))**2 )/ (2*m1) #K=mv^2 or p^2/2m if v<<c
    #calculate potential energy 
    U=-G*((m1*m2)/mag(r))#with earth
    #calculate sum of bothenergies
    #print("K:",K,"U:",U,"K+U:",(K+U))
    #moon-earth
    U_moon=-G*((m1*m3)/mag(r_moon))
    Utotal= U+U_moon
    #graph both energies vs time
    kineticenergy.plot(pos=(t,K))#cyan
    potentialenergy.plot(pos=(t,Utotal))#green #see Modify Utotal for valuesof interest
    kplusu.plot(pos=(t,(K+Utotal)))#yellow
    '''
    #graph all energies vs r
    kineticenergy.plot(pos=(mag(r),K))#cyan
    potentialenergy.plot(pos=(mag(r),U))#green
    kplusu.plot(pos=(mag(r),(K+U)))#yellow ( maybe should be constant,its not)
    '''
    #stop when ship crashes
    if(mag(r) < earth.radius):
        break
    if(mag(r_moon) < moon.radius):
        break
    t=t+deltat#for the loop
print("end of program")
    
