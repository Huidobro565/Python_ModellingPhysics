from visual import*
from visual.graph import*
'''observation: disregarding external forces the K+U graphs still a bit
sinusoidal but neraly constant. Just as the p44, still dont know why I
don't get a straigth line'''
'''here it does come to a stop with the friction, not like p45 where it
would reduce amplitude infinitely '''
'''Note:problem asks for dissipation in terms of energy loss due to
viscuous friction=c*-v and sliding friction=mu_k*-FN. They are not the same
and they both give a very similar result separatedly'''
floor=box(pos=(0,0,0),
          size=(10,0.1,2),
          color=color.blue,
          )
wall=box(pos=(5,0.5+floor.size.y/2,floor.pos.z),
         size=(0.1,1,floor.size.z),
         color=color.green)
block=box(#pos=(wall.pos.x - 4,0.5+floor.size.y,wall.pos.z),
          pos=(1,0.5+floor.size.y/2,0),
          size=(1,1,1),
          color=color.orange)
spring=helix(pos=(wall.pos),
             axis=(block.pos-wall.pos),
             radius=0.2,
             thickness=0.04,
             coils=20,
             color=color.yellow)
#data
L0=4#20*10**-2#m
ks=3 #N/m
m=1#230*10**-3#kg
v=vector(-4,0,0)
p=m*v
t=0
dt=0.01
mu_k=0.2#friction costant of the floor material
c=0.3#damping coefficient for viscuous friction
F_grav=vector(0,-9.8,0)
'''graphs'''
gd = gdisplay(x=420, y=0, width=500, height=500,
              title='K(yellow),U(red),K+U(orange)', xtitle='r or t, look at code', ytitle='K,U,K+U')
f1=gcurve(color=color.yellow)#K
f2=gcurve(color=color.red)#U
f3=gcurve(color=color.orange)#K+U
while True:
    rate(100)
    L=block.pos-wall.pos
    Lhat=L/mag(L)
    s=mag(L)-L0 #stretch may be + or -
    F_spring=-ks*s*Lhat
    #specific of this problem: resistance
    F_viscous=c*(-p/m)#viscous friction, c is a damping coefficient
    F_N=mag(m*F_grav)#MAGNITUD ofnormal force equals the weight
    F_sliding=mu_k * F_N * (-p/mag(p))#sliding friction opposed to the movement

    F_net=F_spring+F_viscous#+F_sliding#+F_grav#note viscous and sliding are not asked to do toguether, just one or the other
    #momentum principle for motion:Fnet, update momentum,update position
    pf=vector(p+F_net*dt)
    block.pos=block.pos+(pf/m)*dt
    spring.axis=block.pos-wall.pos#fixed
    
    #K=p^2/2m or 1/2 mv^2
    K=((mag(pf))**2) /(2*m)
    #Uspring=1/2ks*s^2
    U=(0.5)*(ks)*(s**2)
    '''
    #plots vs mag(L)
    f1.plot(pos=(mag(L),K))
    f2.plot(pos=(mag(L),U))
    f3.plot(pos=(mag(L),K+U))
    spring.axis=ball.pos
    '''
    #plots vs time
    f1.plot(pos=(t,K))
    f2.plot(pos=(t,U))
    f3.plot(pos=(t,K+U))
    p=pf#for the loop
    t=t+dt
    

