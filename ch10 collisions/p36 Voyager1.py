from visual import*
from visual.graph import*
from Methods import grav

scene.autocenter=True
scene.width=800
scene.height=700

#difficult to visualize with friking sun, maybe dont draw it 
#Data
R=7e7#saturns radius
distance_SaturnSun=7.8e11
radius_sun=695508e3
j_mass=1.9e27
sun_mass=1.989e30
ship_mass=700
j_orbitalspeed=1.3e4
sun_pos=vector(0,0,-distance_SaturnSun)
#graphs
gdx=gdisplay(x=1000,y=400,width=500,title='plot of Vavg of ship',xtitle='t',ytitle='Vavg')
f1=gcurve(color=color.yellow)

xi=R*-24#problem asks to modify this,-R*24 is what gives me the max change of speed
#Objects
jupiter=sphere(pos=(0,0,0),
               radius=R,
               color=color.red,
               opacity=0.7,
               make_trail=True)
ship=sphere(pos=(-xi,0,-25*R),#initial position
            radius=R/4,#something visible
            color=color.cyan,
            make_trail=True,
            opacity=0.6)
initialjupiterspeed=vector(j_orbitalspeed,0,0)
p_J=j_mass*initialjupiterspeed#book said model its motions as a straight line
initialshipspeed=vector(0,0,1e4)
p_ship=ship_mass*initialshipspeed
t=0
dt=60

while (ship.pos.z<=25*R):
    rate(100)#for this rate(100)and dt=60 it is (6000s or 1.6 hours)/(real second)
    #first play with jupiters motion due to the sun
    r=jupiter.pos-sun_pos#remmeber sun_pos is fixed
    F_onJbyS=grav(r,j_mass,sun_mass)#force on jupiter by sun
    #spaceship sun
    r_shipsun=ship.pos-sun_pos
    F_onShipbyS=grav(r_shipsun,ship_mass,sun_mass)
    #spaceship and jupiter
    r_onShipbyJ=ship.pos-jupiter.pos
    F_onShipbyJ=grav(r_onShipbyJ,ship_mass,j_mass)
    F_onJbyShip=-F_onShipbyJ
    #Update jupiter
    Fnet_onJ=F_onJbyS+F_onJbyShip#constantly change this while you add stuff
    pf_J=p_J+Fnet_onJ*dt
    jupiter.pos=jupiter.pos+(pf_J/j_mass)*dt
    #update ship
    Fnet_onShip=F_onShipbyS+F_onShipbyJ
    pf_ship=p_ship+Fnet_onShip*dt
    Vavg=pf_ship/ship_mass
    ship.pos=ship.pos+(Vavg)*dt
    #graphs
    f1.plot(pos=(t,mag(Vavg)))
    #loop:
    t=t+dt
    p_J=pf_J
    p_ship=pf_ship

deltashipspeed=mag(Vavg)-mag(initialjupiterspeed)
#magdshipspeed=mag(Vavg-initialjupiterspeed)
print("we want vf-vi to be around 1.6e4")
print("vf-vi=",deltashipspeed,"and it took this many seconds:",t)

#print(abs(jupiter.pos-vector(0,0,0)))#should be the total displacement after 5 real seconds






    
