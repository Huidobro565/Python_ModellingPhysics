from visual import*
from visual.graph import*
import math
'''reference of reality:baseball field is 400 feet or 121 metes long'''
'''results: in vaccum baseball thrower should have reached 177m,
    with air resistance it travelled 96 meters at sea level.
    At denver air is 83% as dense, distances at denver? Worked,
    it would travel 147m. around  more than at sea level.
    51 meters more in denver than sea level!(according to this code
    that could potentially have something wrong)
'''

ballDiameter=7*10**-2 #diameter if 7cm
scaleBall=8
ball=sphere(#pos=(floor.pos.x - floor.size.x/2,1.6 + floor.size.y/2,0),#whoever throws the ball made it at initial heigth of 1.6
            pos=(0,1.7,0),#initial heigth 1.7 simulating the baseball thrower
            radius=ballDiameter/2,
            color=color.yellow,
            make_trail=True)
ball2=sphere(#pos=(floor.pos.x - floor.size.x/2,1.6 + floor.size.y/2,0),#whoever throws the ball made it at initial heigth of 1.6
            pos=(0,1.7,0),#initial heigth 1.7 simulating the baseball thrower
            radius=ballDiameter/2 ,
            color=color.red,
            make_trail=True)
ballscaled=sphere(pos=(ball.pos),#just to be able to see it, scaled a factor of 2
            radius=ballDiameter/2 * scaleBall,
            color=color.yellow,
            opacity=0.3)

m=155*10**-3#kg
#initial speed of 44m/s and an angle of 45 degrees
vx=44*math.cos(45)
#print(vx)#apparently works
vy=44*math.sin(45)
v=vector(vx,vy,0)#initial velocity
p=m*v
p2=p#
#some more data
C=0.35#drag coefficient(apparently depend of the shape of object)
A_ball=math.pi * (ball.radius)**2 #cross sectional area of ball
rho_air=1.3# kg/m^3 density of air(apparently rho)
g=vector(0,-9.8,0)#gravity force constant in this range of altitude
t=0
dt=0.01
denver_rho=((83*C)/100)#use this only for denver, cause air density is 83% of sea leven
'''graphs'''
gd = gdisplay(x=420, y=0, width=500, height=500,
              title='ball, K(yellow),U(red),K+U(orange)', xtitle='r or t, look at code', ytitle='K,U,K+U')
f1=gcurve(color=color.yellow)#K
f2=gcurve(color=color.red)#U
f3=gcurve(color=color.orange)#K+U
gd2 = gdisplay(x=0, y=420, width=500, height=500,
              title='ball2, K(yellow),U(red),K+U(orange)', xtitle='r or t, look at code', ytitle='K,U,K+U')
f4=gcurve(color=color.yellow)#K
f5=gcurve(color=color.red)#U
f6=gcurve(color=color.orange)#K+U
while True:
    rate(100)
    #air resitance
    v=p/m
    vhat=v/(mag(v))
    #F_air=0.5*C*rho_air*A_ball*mag(v)**2 *(-vhat)#missing cross section area of ball
    F_air=0.5*C*denver_rho*A_ball*mag(v)**2 *(-vhat)#just for denver.
    #momentum principle Fnet, update momentum,update position
    F_grav=m*g
    Fnet=F_grav+F_air#well in this rang eof altitude Fnet is gonna be constant
    Fnetball2=F_grav#
    pf2=p2+Fnetball2*dt#
    ball2.pos=ball2.pos+(pf2/m)*dt#
    #print(Fnet)
    pf=p+Fnet*dt
    #print(p,pf)
    ball.pos=ball.pos+(pf/m)*dt
    ballscaled.pos=ball.pos
    #  graphs ball1#####
    #K=p^2/2m or 1/2 mv^2
    K=((mag(pf))**2) /(2*m)
    #U = mgh at low distance from earth  
    U=m*mag(g)*ball.pos.y
    #plots vs time
    f1.plot(pos=(t,K))
    f2.plot(pos=(t,U))
    f3.plot(pos=(t,K+U))
    #  graphs ball2######
    #K=p^2/2m or 1/2 mv^2
    K2=((mag(pf2))**2) /(2*m)
    #U = mgh at low distance from earth  
    U2=m*mag(g)*ball.pos.y
    #plots vs time
    f4.plot(pos=(t,K2))
    f5.plot(pos=(t,U2))
    f6.plot(pos=(t,K2+U2))
    if(ball.pos.y<=0.1 and ball.pos.y>=-0.1):
        print("ball1 wigth air resistance",ball.pos.x)
        #ball.pos=(ball.pos.x,ball.pos.y,0)
    if(ball2.pos.y<=0):
        print("ball2 in vacum",ball2.pos.x)
        break
    p=pf#keep looping
    p2=pf2
    t=t+dt
print('end of program')
    
    
    
