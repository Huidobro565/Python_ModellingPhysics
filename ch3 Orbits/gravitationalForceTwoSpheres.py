from visual import *
from visual.graph import*
'''
-movement of one ball due to another statinary ball
-also plotted graph distance vs force
-obviously this code could be optimized
sucess, but only movement of one ball due to the grav force of a stationary ball. Next I shall do both moving
because of the reciprocal force excerted at each other
'''
#objects
ball1=sphere(pos=(0,0,0),
             radius=0.5,
             color=color.blue)
ball2=sphere(pos=(5,5,0),
             radius=1,
             color=color.red,
             opacity=0.4)
#graph
graph1 = gdisplay(x=0, y=0,# width=600, height=150, # By default, any graphing objects created following a gdisplay belong to that window, or you can specify which window a new object belongs toby looking at documentation.
          title='N vs. t', xtitle='distance', ytitle='force', 
 #         xmax=50., xmin=-20., ymax=5E3, ymin=-2E3, 
          foreground=color.white, background=color.black)
distanceVSForce=gcurve(color=color.yellow)

#data and initial conditions
m1=1
m2=2
r_vector=ball2.pos-ball1.pos
r_abs=mag(r_vector)
rhat=r_vector/r_abs
G=6.7*10**-11
scalefactor=10**12
gravf_vector=-G*(m1*m2/(r_abs)**2)*rhat #python needs operator with the parenthesis
print("position vector: ",r_vector,"rhat is: ",rhat,"gravitational force: ",gravf_vector) #works well
#the arrow force test, force on 2 by 1. IWANT TO UPDATE POS AND AXIS
f_vector=arrow(pos=ball2.pos,
               axis=scalefactor *gravf_vector,
               color=color.green,
               opacity=0.2)


''' all above works great, now lets try to make them move: the momentum principle remember: Fnet, update momentum, update position works'''
#data for movement
vi=vector(0,0,0)
pi=vi*m2
t=0
dt=0.01

while True: 
    #momentum principle(assume first it moves then the force incrase)
    rate(100)
    Fnet21=gravf_vector*scalefactor*100
    pf2=pi+Fnet21*dt
    vball2=pf2/m2
    ball2.pos=ball2.pos+vball2*dt
    f_vector.pos=ball2.pos
    f_vector.axis=gravf_vector*scalefactor

    #the forces are updated after each move
    r_vector=ball2.pos-ball1.pos
    r_abs=mag(r_vector)
    rhat=r_vector/r_abs
    gravf_vector=-G*(m1*m2/(r_abs)**2)*rhat
    print("distance: ",mag(r_vector), "forceMag: ",mag(gravf_vector))
    distanceVSForce.plot(pos=(mag(r_vector),mag(gravf_vector)))
    if mag(r_vector)<ball1.radius+ball2.radius: #make it stop when the surface of the balls touch each other
        break
    
print('end of program')
