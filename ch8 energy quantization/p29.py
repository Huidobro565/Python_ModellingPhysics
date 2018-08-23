from visual import*
from visual.graph import*
from random import random
'''random photon emission of excited atoms'''
Natoms=10000
#P is the probablility for a atom to emit during a time interval dt
P=0.1#10%
dt=0.2 #ns
t=0
tmax=5*dt/P #5 mean lifetimes
#create a bar graph
gdisplay(xtitle='t,ns',ytitle='Atoms in excited state')
excited=gvbars(color=color.yellow,delta=dt/2)#why this delta?oh, to separate the bars

while t < tmax:
    rate(100)
    #show number of atoms remaining
    excited.plot(pos=(t,Natoms))
    emissions=0
    atom=0
    while atom < Natoms:
        if random() < P: #emits?
            #count emissions in this dt
            emissions=emissions+1
        atom=atom+1#go for the next atom
    Natoms=Natoms-emissions
    t=t+dt
'''
a)
f)with x atoms find the bar whose heigth is x/e ->x*0.368,
the value of t at this point will be the mean lifetime. 
'''    
        
