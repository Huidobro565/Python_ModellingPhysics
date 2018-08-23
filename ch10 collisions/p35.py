from visual import*
from visual.graph import*
'''base code p34'''
'''
the momentum graphs look good, momentum is conserved
'''
#plots
gdx=gdisplay(x=1000,y=400,width=500,title='p_x,Alpha magenta,Au yellow,red is total',xtitle='t',ytitle='momentum.x')
p_Au_x_graph=gcurve(color=color.yellow)
p_Alpha_x_graph=gcurve(color=color.magenta)
totalx=gcurve(color=color.red)

gdy=gdisplay(x=500,y=0,width=500,title='p_y,Alpha magenta,Au yellow, red is total',xtitle='t',ytitle='momentum.y')
p_Au_y_graph=gcurve(color=color.yellow)
p_Alpha_y_graph=gcurve(color=color.magenta)
totaly=gcurve(color=color.red)
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
Alpha_pos=vector(-1e-13,7.5e-14 ,0)#original=((-1e-13,5e-15,0))#the y value of this is the impact parameter
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
while t<1.3e-20:
    rate(100000000)
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
    #plotting the gcurves:
    p_Alpha_x_graph.plot(pos=(t,pf_Alpha.x))
    p_Au_x_graph.plot(pos=(t,pf_Au.x))
    totalx.plot(pos=(t,pf_Alpha.x+pf_Au.x))
    p_Alpha_y_graph.plot(pos=(t,pf_Alpha.y))
    p_Au_y_graph.plot(pos=(t,pf_Au.y))
    totaly.plot(pos=(t,pf_Alpha.y+pf_Au.y))
    #looping:
    p_Alpha=pf_Alpha
    p_Au=pf_Au
    t=t+deltat
dis=Alpha.pos-initialposAlpha
deltax=Alpha.pos.x-initialposAlpha.x
angle_maybe=degrees(acos(deltax/mag(dis)))
print("angle?",angle_maybe)#looks reasonable
