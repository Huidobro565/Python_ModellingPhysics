'''base code ch 3 ranger mission crash into the moon because of not back propellers'''
'''fix the code and perform p81 ch 6'''
'''p71, ranger mission ship crashed the moon because it
didnt have repulsion propellers'''
'''specific to this problem : calculate the work done by the earth and the moon
on the spacecraft. W=f*deltar'''
from visual import *
from visual.graph import*
import math
#data and scalefactors
moon_earthD=384400*10**3
ship_mass=173
earth_mass=5.972*10**24 
moon_mass=7.34767309*10**22
moon_radius=1.75*10**6
earth_radius=6.4*10**6
scalefactorR=10#scaling radius for the planets
#objects
ship=sphere(pos=(-moon_earthD+earth_radius+50*10**3,0,0),#start 50km above surface of earth
             radius=3*10**6,#exaggerated just to ba able to see it
             color=color.yellow,
            make_trail=True)
earth=sphere(pos=(-moon_earthD,0,0),#scaled for visualization
             radius=earth_radius * scalefactorR,
             color=color.red,
             opacity=0.4)
realearth=sphere(pos=(-moon_earthD,0,0),#real scale earth
             radius=earth_radius,
             color=color.red,
             opacity=1)
moon=sphere(pos=(0,0,0),#scaled for visualization
             radius=moon_radius * scalefactorR,
             color=color.cyan,
             opacity=0.4)
realmoon=sphere(pos=(0,0,0),#real size
             radius=moon_radius,
             color=color.cyan,
             opacity=1)
#initial data for the three bodies and their interaction 1=earth,2=moon,3=ship
G=6.6*10**-11
#scape velocity K+U=0
scapeVelocity=math.sqrt(((2*G*ship_mass*earth_mass)/mag(ship.pos-earth.pos))/ship_mass)
print(scapeVelocity)#doesnt scape with this scapeVelocity, have to add a little more.
v1=vector(0,0,0)#earth
p1=v1*earth_mass
v2=vector(0,0,0)#moon
p2=v2*moon_mass
v3=vector(scapeVelocity+182,0,0)#this is the minimun speed I could od to make it to the moon
p3=v3*ship_mass
t=0
dt=60#seconds
dr=1000#meters
vecdr=(dr,0,0)
WorkbyMoon=0#initialize
WorkbyEarth=0#initialize
Ki=((mag(p3))**2) / (2*ship_mass)#initial kinetic energy of ship
gd = gdisplay(x=500, y=0, width=600, height=600, 
      title='K of spacecraft(yellow) and W by both earthandmoon(cyan)',
      xtitle='t', ytitle='K and W')
f1=gcurve(color=color.yellow)
f2=gcurve(color=color.cyan)
while True:
    rate(200000000)#iterations per second
    #moonship
    r_moonship=ship.pos-moon.pos
    rhat_moonship=r_moonship/mag(r_moonship)
    fabs_moonship=(G*moon_mass*ship_mass)/(mag(r_moonship)**2)
    fvec_moonship=fabs_moonship * (-rhat_moonship)
    #earthship
    r_earthship=ship.pos-earth.pos
    rhat_earthship=r_earthship/mag(r_earthship)
    fabs_earthship=(G*earth_mass*ship_mass)/(mag(r_earthship)**2)
    fvec_earthship=fabs_earthship * (-rhat_earthship)
    #updates(Fnet, momentum, position)
    Fnet_onShip=fvec_earthship+fvec_moonship
    p3=p3+Fnet_onShip*dt
    ship.pos=ship.pos+(p3/ship_mass) * dt
    #work done by the moon on the ship
    W_onshipbymoon=fvec_moonship.dot(vecdr)
    WorkbyMoon=WorkbyMoon+W_onshipbymoon
    #work done by earth on ship
    W_onshipbyeaerth=fvec_earthship.dot(vecdr)
    WorkbyEarth=WorkbyEarth+W_onshipbyeaerth
    #work done by moon and earth added toguether
    O=WorkbyMoon+WorkbyEarth
    #kinetic energy of ship
    K=(mag(p3)**2)/(2*ship_mass)
    print(O,K)
    f1.plot(pos=(t,K))
    f2.plot(pos=(t,O))
    if(mag(r_earthship) < realearth.radius):
        break
    if(mag(r_moonship) < realmoon.radius):
        print("dt=60, time is seconds to crash:",t, "in days:",(t)/(60*60*24))# takes 5 days to crash with dt=60
        print("work done by moon:",WorkbyMoon,"work done by earth:",WorkbyEarth)
        print("work moon+earth:",(WorkbyMoon+WorkbyEarth))
        print("Kf:",K,"Ki",Ki,"Kf-Ki",K-Ki)
        print("initial speed:",mag(v3),"final speed:", mag(p3)/ship_mass)
        break
    t=t+dt
print("end of program")

