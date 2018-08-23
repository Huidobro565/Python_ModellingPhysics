'''p44 ch 7 with base code p70 ch 4'''
'''observation: K+U oscilates, I believe it shouldbe constant but I can't
figure why it's not'''
from visual import*
from visual.graph import*

floor=box(pos=(0,0,0),
          size=(0.25,0.01,0.25),
          color=color.green,
          opacity=0.7)
spring=helix(pos=(0,0,0),
             axis=(0,-30*10**-2,0),
             radius=0.012,
             coils=25,
             color=color.yellow)
radiusBall=0.02
ball=sphere(#pos=(0,spring.axis.y - (radiusBall/2), 0),#original, this was making it move without any push
            pos=(0,spring.axis.y,0),#good, now it doesnt move without momentum    
            radius=radiusBall,
            color=color.orange,
            opacity=0.5,
            make_trail=True)
lengthSpring=arrow(pos=floor.pos,#just to visualize the relaxed spring length
                   axis=(0,-20*10**-2,0),
                   color=color.blue,
                   opacity=0.2)
#data
L0=20*10**-2#m
ks=100 #N/m
m=230*10**-3#kg original mass
v=vector(0,0,0)
p=m*v
t=0
dt=0.01
#F_grav=vector(0,-9.8,0)
#graphs
gd = gdisplay(x=420, y=0, width=500, height=500,
              title='K(yellow),U(red),K+U(orange)', xtitle='r or t, look at code', ytitle='K,U,K+U')
f1=gcurve(color=color.yellow)#K
f2=gcurve(color=color.red)#U
f3=gcurve(color=color.orange)#K+U
while True:
    rate(30)
    L=ball.pos-spring.pos
    Lhat=L/mag(L)
    s=mag(L)-L0 #stretch may be + or -
    #print(s)
    F_spring=-ks*s*Lhat
    F_net=F_spring#+F_grav#often take oput gravity to test differences
    '''obs:even without gravity it does oscillate a little, dont know why
    also K+U looks a lot better(more like what would be anticipated)'''
    '''momentum principle for motion:Fnet, update momentum,update position'''
    pf=p+F_net*dt
    ball.pos=ball.pos+(pf/m)*dt
    spring.axis=ball.pos
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
    
