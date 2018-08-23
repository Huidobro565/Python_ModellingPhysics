from visual import*
from visual.graph import*
scene.width=1024
scene.height=600
scene.autocenter=True#to get translation apparently
'''colision between moving alpha particle and a stationary gold nucleus(part
of it)
task: finish the coding
we are using collision of particles interacting electrically, they dont
touch each other.
notes(table):--------
value of b: | scattering angle:
3e-14       | 33 degrees
7.5e-14     | 13.0 degrees
1e-15       | 90 degrees
0           | 180, obvious
1.1e-17     | 168 degrees
----- end table
'''
#Data
q_e=1.6e-19
m_p=1.7e-27
oofpez=9e9
m_Au=(79+118)*m_p#i guess its adding protons and neutrons
m_Alpha=(2+2)*m_p
qAu=2*q_e
qAlpha=79*q_e#and I guess this is number of electrons
deltat=1e-23
Au_radius=4e-15
Alpha_radius=1e-15
Au_pos=vector(0,0,0)
Alpha_pos=vector(-1e-13,7.5e-14,0)#original=((-1e-13,5e-15,0))#the y value of this is the impact parameter
initialposAlpha=Alpha_pos#just storing this
b=(Alpha_pos.y-Au_pos.y)#impact paramenter distance between the centers perpendicular to the velocity
#this formula for b is only for this particular problem, not general.
print("b=",b)
#objects
Au=sphere(pos=Au_pos,
          radius=Au_radius,
          color=color.yellow,
          make_trail=True,
          opacity=0.7)
Alpha=sphere(pos=Alpha_pos,
             radius=Alpha_radius,
             color=color.magenta,
             make_trail=True)
p_Au=m_Au*vector(0,0,0)#velocity (0,0,0) stationary
p_Alpha=vector(1.043e-19,0,0)#I will assume this is initial momentum
pi_Alpha=p_Alpha
t=0#deltat is defined above in Data
while t<1:#1.3e-20:
    rate(100)
    #r=Au.pos-Alpha.pos
    r=Alpha.pos-Au.pos#lets take Au as the big guy whose arrow will affect Alpha
    rhat=r/mag(r)#norm(r)
    #gonna have to use the electric force law
    Fnet_Alpha=(oofpez*qAu*qAlpha*rhat) / (mag(r)**2)
    pf_Alpha=p_Alpha+Fnet_Alpha*deltat
    Alpha.pos=Alpha.pos+(pf_Alpha/m_Alpha)*deltat
    #now with Au
    Fnet_Au=-Fnet_Alpha
    pf_Au=p_Au+Fnet_Au*deltat
    Au.pos=Au.pos+(pf_Au/m_Au)*deltat
    #lopping
    p_Alpha=pf_Alpha
    p_Au=pf_Au        
    t=t+deltat
dis=Alpha.pos-initialposAlpha
deltax=Alpha.pos.x-initialposAlpha.x
angle_maybe=degrees(acos(deltax/mag(dis)))
print("angle?",angle_maybe)#looks reasonable
