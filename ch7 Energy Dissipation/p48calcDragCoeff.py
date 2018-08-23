from visual import*
from visual.graph import*
import math
'''first time I try this method to stop animations at desired positions,
works like a charm'''
#I will start using methods. also start getting used to use norm for unit vectors
'''determine drag coefficient experimenting the fall of a coffe filter with
the data given
results:in vaccum both filter and stack fall from altutude 2.03m in 0.63s, and
0.64 after modifying some code around.
Got coefficient of C=6.5 to match the real life experiment, the filter fell at t=1.44s
and the stack at 0.88s.
cofee filter terminal speed around 1.5m/s
'''
filter_mass=8.52*10**-3#kg
outer_radius=5.8*10**-2#m
cross_area=math.pi * (outer_radius)**2
initial_height=2.03#m, the probelm is with 2.03m
drop_time=1.44#s obviously not in vaccum
drop_stack=0.88#s for stack of  FOUR(4) coffee filters
rho_air=1.045#kg/m^3 in santa fe, Mexico(altitude 2100m)
stack_mass=4*filter_mass#kg
C=6.5# VARY THIS
def f_air(v):#v that is the only thing that is going to change with time
    return 0.5*C*rho_air*cross_area*mag(v)**2 *(-norm(v))#taking in some constant values
'''air density at altitude H is exp(-H/8500) * rho_airsealevel'''
cofee_filter=cylinder(pos=(0,initial_height,0),
                      axis=(0,0.01,0),#axis goes up, not down
                      radius=outer_radius,
                      color=color.white)
filter_stack=cylinder(pos=(0.5,initial_height,0),#4 cofee filters
                      axis=(0,0.04,0),#axis goes up, not down
                      radius=outer_radius,
                      color=color.red)
floor=box(pos=(0,-0.01,0),#floor is good
          size=(2,0.02,0.5),
          color=color.blue)
gd = gdisplay(x=420, y=0, width=500, height=500,
              title='v(yellow)', xtitle='t', ytitle='v')
f1=gcurve(color=color.yellow)#v
#f2=gcurve(color=color.red)

#more data
g=vector(0,-9.8,0)
vi_filter=vector(0,0,0)
pi_filter=filter_mass*vi_filter
vi_stack=vector(0,0,0)
pi_stack=vector(0,0,0)
t=0
dt=0.01
while True:
    rate(100)
    #the if's to break, now I just want to make it stop moving,not break
    '''Filter'''
    if(cofee_filter.pos.y < floor.pos.y+floor.size.y/2):#if pos equal or less than 0
        #print("coffee filter hits the floor in vaccum at t=",t,"pos",cofee_filter.pos.y)
        print("coffee filter hits the floor with C=",C,"at t=",t,"pos",cofee_filter.pos.y,"speed:",mag(v))
        cofee_filter.pos.y=0
    elif(cofee_filter.pos.y==0):
        cofee_filter.pos.y=0
    else:
        v=pi_filter/filter_mass#
        f1.plot(pos=(t,mag(v)))
        F_grav=filter_mass*g#just for the filter
        Fnet_filter=F_grav+f_air(v)#+F_air#take in and out F_air
        pf_filter=pi_filter+Fnet_filter*dt
        cofee_filter.pos=cofee_filter.pos+(pf_filter/filter_mass)*dt
        pi_filter=pf_filter
    '''Stack'''
    if(filter_stack.pos.y < floor.pos.y+floor.size.y/2):#ifpos equal or less than 0
        #print("stack hits the floor in vaccum at t=",t,"pos:",filter_stack.pos)
        print("coffee stack hits the floor with C=",C,"at t=",t,"pos:",filter_stack.pos.y)
        filter_stack.pos.y=0#I want it to stay static at 0
    elif(filter_stack.pos.y==0):
        filter_stack.pos.y=0
    else:
        #now the stack
        v_stack=pi_stack/stack_mass#
        F_gravstack=stack_mass*g
        #F_airstack=0.5*C*rho_air*cross_area*mag(v_stack)**2 *(-norm(v_stack))
        Fnet_stack=F_gravstack+f_air(v_stack)#method here
        pf_stack=pi_stack+Fnet_stack*dt
        filter_stack.pos=filter_stack.pos+(pf_stack/stack_mass)*dt
        pi_stack=pf_stack#loop
        
    t=t+dt#loop
    
