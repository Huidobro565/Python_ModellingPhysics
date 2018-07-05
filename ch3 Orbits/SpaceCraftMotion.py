from visual import*
'''compare with  SpaceCraftMotion2 to find any bugs,
this one does not orbit, just falls.'''
#data earth and ship and moon
radius_earth=6.4*10**6
ship_mass=1500
earth_mass=6*10**24
moon_mass=7*10**22
#objects
earth=sphere(pos=(0,0,0),
             radius=radius_earth,
             color=color.blue)
ship=sphere(pos=(-20*radius_earth,0,0),
             radius=radius_earth/3,
             color=color.red,
             opacity=0.8,
            make_trail=True)
#data
G=6.7*10**-11
scalefactor=10**12
scaleForce=10**4
#gravity equations
r_vector=ship.pos-earth.pos
r_abs=mag(r_vector)
rhat=r_vector/r_abs
gravf_vector=-G*(earth_mass*ship_mass/(r_abs)**2)*rhat
magForce=mag(gravf_vector)


#data for movement
vi=vector(5,18,0)
pi=vi*ship_mass
t=0
dt=160

#arrows for momentum and force
momentum=arrow(pos=ship.pos,
            axis=pi,
            color=color.cyan,
            opacity=0.5)
force=arrow(pos=ship.pos,
            axis=gravf_vector,
            color=color.green,
            opacity=1)

#movement
while True:
        rate(10000)
        r_vector=ship.pos-earth.pos
        r_abs=mag(r_vector)
        rhat=r_vector/r_abs
        gravf_vector=-G*(earth_mass*ship_mass/(r_abs)**2)*rhat # forceon the ship
        Fnet=gravf_vector
        pfShip=pi+Fnet*dt
        vShip=pfShip/ship_mass
        ship.pos=ship.pos+vShip*dt
            
''' definitely something wrong here
while True:
    #momentum principle
    rate(200000)
    ForceonPlanetbyEarth=gravf_vector
    Fnet=ForceonPlanetbyEarth# I need to find a way to update the Fnet
    pfShip=pi+Fnet*dt
    vShip=pfShip/ship_mass
    ship.pos=ship.pos+vShip*dt
    
    #update the fucking arrows
    force.pos=ship.pos
    force.axis=gravf_vector*scaleForce
    
    momentum.pos=ship.pos
    momentum.axis=pfShip*scalefactor
    

    #update Fnet by upgrading f_vector gravity equations
    r_vector=ship.pos-earth.pos
    r_abs=mag(r_vector)
    rhat=r_vector/r_abs
    gravf_vector=-G*(earth_mass*ship_mass/(r_abs)**2)*rhat
'''
