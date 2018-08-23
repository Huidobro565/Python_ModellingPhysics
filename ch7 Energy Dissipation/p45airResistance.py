'''p45 ch 7 with base code p70 ch 4'''
'''observation: K+U oscilates(without grav,with grav is a complete mess),
I believe it should be constant but I still can't figure why it's not'''
'''change ball for flat so that modelling air resistance is easier for now'''
'''this animation didnt look very good, quite unnatural. wonder why'''
'''something wrong, use p45.py to fuck around with the program and make it run,
what I found is that by erasing the long line comment in the while loop
it run'''
import math
from visual import*
from visual.graph import*

floor=box(pos=(0,0,0),
          size=(0.25,0.01,0.25),
          color=color.green,
          opacity=0.7)
spring=helix(pos=(0,0,0),
             axis=(0,-20*10**-2,0),
             radius=0.012,
             coils=25,
             color=color.yellow)
ball=cylinder(#pos=(0,spring.axis.y - (radiusBall/2), 0),#original, this was making it move without any push
            pos=(0,spring.axis.y,0),#good, now it doesnt move without momentum    
            axis=(0,-0.01,0),
            color=color.orange,
            radius=0.09,
            opacity=0.5,
            make_trail=True)
lengthSpring=arrow(pos=floor.pos,#just to visualize the relaxed spring length
                   axis=(0,-20*10**-2 ,0),#L0 below
                   color=color.blue,
                   opacity=0.2)
#data
'''specific to this problem you have to define some new variables'''
C=1#shape effect reflects sharpness or bluntness of object. this drag coefficient typically 0.3<C<1.0. I'll assume 1 is for completely blunt 
rho_air= 1.225#kg/m^3 density of the air
A_ball=math.pi * (ball.radius)**2#cross sectional area of the object
L0=20*10**-2#m
ks=50 #N/m
m=230*10**-3#kg original mass
v=vector(0,-0.5,0)
p=m*v
t=0
dt=0.01
F_grav=vector(0,-9.8,0)
#graphs
gd = gdisplay(x=420, y=0, width=500, height=500,
              title='K(yellow),U(red),K+U(orange)', xtitle='r or t, look at code', ytitle='K,U,K+U')
f1=gcurve(color=color.yellow)#K
f2=gcurve(color=color.red)#U
f3=gcurve(color=color.orange)#K+U
while True:
    rate(100)
    #after the loop reinitiates I have a new p
    #specific to this problem
    v=p/m
    vhat=v/(mag(v))
    F_air=0.5*C*rho_air*A_ball*mag(v)**2 *(-vhat)
    #print(F_air)#works
    L=ball.pos-spring.pos
    Lhat=L/mag(L)
    s=mag(L)-L0 #stretch may be + or -
    #print(s)
    F_spring=-ks*s*Lhat
    F_net=F_spring+F_air+F_grav#often take oput gravity to test differences,gravity screws the graphs enormously
    ''''
    Note: when using the three forces its very interesting that the amplitude
    of the oscilation reduces with time, but apparently never stops,just keeps
    reducing infinitely.Interesting result. the book pointed out how to deal
    with this. Use an if and break statement
    '''
    pf=p+F_net*dt
    ball.pos=ball.pos+(pf/m)*dt
    spring.axis=ball.pos
    if(mag(pf/m) < 0.00001):#well it didnt look very good but kinda worked
        print("break man")
        break
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
    
