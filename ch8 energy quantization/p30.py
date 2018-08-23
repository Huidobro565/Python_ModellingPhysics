from visual import*
from visual.graph import*
from random import random
#start with 100 atoms in an excited state
#try larger or smaller numbers
Natoms=100
#P is the probablity for an atom to emit during interval dt
P=0.1
Pgreen=0.3
dt=0.2
t=0
tmax=5*dt/P
gdisplay(xtitle='t,ns',xmax=tmax,ytitle='Emissions of green photons')
greeng=gvbars(color=color.green,delta=dt/2)
gdisplay(y=400,xtitle='t,ns',xmax=tmax,ytitle='Emission of red photons')
redg=gvbars(color=color.red,delta=dt/2)
greens=reds=0
while t<tmax:
    rate(100)
    atom=0
    g=r=0
    while atom < Natoms:
        if random() < P:#emits?
            if random() < Pgreen:
                g=g+1
            else:
                r=r+1
        atom=atom+1
    greeng.plot(pos=(t,g))
    redg.plot(pos=(t,r))
    greens=greens+g
    reds=reds+r
    Natoms=Natoms-(g+r)
    t=t+dt
print('greens emmisions:',greens,'red emmisions:',reds)
