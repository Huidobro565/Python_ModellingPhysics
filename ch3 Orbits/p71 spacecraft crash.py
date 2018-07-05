'''p71, ranger mission ship crashed the moon because it
didnt have repulsion propellers'''
from visual import *
#data and scalefactors
ship_mass=173
earth_mass=5.972*10**24 
moon_mass=7.34767309*10**22
moon_earthD=4*10**8
scalefactorD=1
moon_radius=1.75*10**6
earth_radius=6.4*10**6
scalefactorR=10#scaling radius for the planets
#objects
ship=sphere(pos=(-moon_earthD*scalefactorD+earth_radius+50*10**3,0,0),
             radius=3*10**6,#exaggerated just to ba able to see it
             color=color.yellow,
            make_trail=True)
earth=sphere(pos=(-moon_earthD*scalefactorD,0,0),
             radius=earth_radius * scalefactorR,
             color=color.red,
             opacity=0.4)
moon=sphere(pos=(0,0,0),
             radius=moon_radius * scalefactorR,
             color=color.cyan,
             opacity=1)
#initial data for the three bodies and their interaction 1=earth,2=moon,3=ship
v1=vector(0,0,0)
p1=v1*earth_mass
v2=vector(0,0,0)
p2=v2*moon_mass
v3=vector(10**4,0,0)
p3=v3*ship_mass
G=6.6*10**-11

#arrow forces
scaleEarth=10**6
scaleMoon=10**9
f_moonship=arrow(pos=ship.pos,
                  axis=(0,0,0),
                  color=color.green,
                  opacity=0.5)
f_earthship=arrow(pos=ship.pos,
             axis=(0,0,0),
             color=color.red,
             opacity=0.2)

t=0
dt=60

while True:
    rate(100)
    r_moonship=moon.pos-ship.pos
    rhat_moonship=r_moonship/mag(r_moonship)
    fabs_moonship=G*moon_mass*ship_mass/mag(r_moonship)**2
    fvec_moonship=fabs_moonship * rhat_moonship

    r_earthship=earth.pos-ship.pos
    rhat_earthship=r_earthship/mag(r_earthship)
    fabs_earthship=G*earth_mass*ship_mass/mag(r_earthship)**2
    fvec_earthship=fabs_earthship * rhat_earthship

    Fnet_onShip=fvec_moonship+fvec_earthship
    #updates
    p3=p3+Fnet_onShip*dt
    ship.pos=ship.pos+(p3/ship_mass) * dt
    #update arrows
    '''
    f_moonship.pos=ship.pos
    f_moonship.axis=fvec_moonship*scaleMoon
    f_earthship.pos=ship.pos
    f_earthship.axis=fvec_earthship*scaleEarth
    '''
#interaction



