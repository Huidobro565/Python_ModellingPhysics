from visual import*
'''p64'''
#objects
planet0=sphere(pos=(0,0,0),
             radius=6.4*10**6,
             color=color.red
              )
ship1=sphere(pos=(-13*10**7,6.5*10**7,0),
             radius=2*10**6,
             color=color.orange
              )
ship2=sphere(pos=(-6.5*10**7,6.5*10**7,0),
             radius=2*10**6,
             color=color.orange
              )
ship3=sphere(pos=(0,6.5*10**7,0),
             radius=2*10**6,
             color=color.orange
              )
ship4=sphere(pos=(6.5*10**7,6.5*10**7,0),
             radius=2*10**6,
             color=color.orange
              )
ship5=sphere(pos=(13*10**7,6.5*10**7,0),
             radius=2*10**6,
             color=color.orange
              )
#data constants and equations:
planet_mass=6*10**24
ship_mass=15*10**3
G=6.7*10**-11
scalefactor=10**5
#from here data varies for each one(later use for loops for these shit)

#force on 1 by 0 (ship1 by planet)
r_vector=ship1.pos-planet0.pos
r_abs=mag(r_vector)
rhat=r_vector/r_abs
gravf_vector=-G*(planet_mass*ship_mass/(r_abs)**2)*rhat
magForce=mag(gravf_vector)
print(gravf_vector,magForce)

#an arrow representing the force on 1 by 0
f_vector=arrow(pos=(ship1.pos),
               axis=gravf_vector*scalefactor,
               color=color.green,
               opacity=0.1)

#force on 2 by 0 
r_vector=ship2.pos-planet0.pos
r_abs=mag(r_vector)
rhat=r_vector/r_abs
gravf_vector=-G*(planet_mass*ship_mass/(r_abs)**2)*rhat
magForce=mag(gravf_vector)
print(gravf_vector,magForce)

#an arrow representing the force on 1 by 0
f_vector=arrow(pos=(ship2.pos),
               axis=gravf_vector*scalefactor,
               color=color.green,
               opacity=0.1)

#force on 3 by 0 
r_vector=ship3.pos-planet0.pos
r_abs=mag(r_vector)
rhat=r_vector/r_abs
gravf_vector=-G*(planet_mass*ship_mass/(r_abs)**2)*rhat
magForce=mag(gravf_vector)
print(gravf_vector,magForce)

#an arrow representing the force on 1 by 0
f_vector=arrow(pos=(ship3.pos),
               axis=gravf_vector*scalefactor,
               color=color.green,
               opacity=0.1)

#force on 4 by 0 
r_vector=ship4.pos-planet0.pos
r_abs=mag(r_vector)
rhat=r_vector/r_abs
gravf_vector=-G*(planet_mass*ship_mass/(r_abs)**2)*rhat
magForce=mag(gravf_vector)
print(gravf_vector,magForce)

#an arrow representing the force on 1 by 0
f_vector=arrow(pos=(ship4.pos),
               axis=gravf_vector*scalefactor,
               color=color.green,
               opacity=0.1)

#force on 5 by 0 
r_vector=ship5.pos-planet0.pos
r_abs=mag(r_vector)
rhat=r_vector/r_abs
gravf_vector=-G*(planet_mass*ship_mass/(r_abs)**2)*rhat
magForce=mag(gravf_vector)
print(gravf_vector,magForce)

#an arrow representing the force on 1 by 0
f_vector=arrow(pos=(ship5.pos),
               axis=gravf_vector*scalefactor,
               color=color.green,
               opacity=0.1)




