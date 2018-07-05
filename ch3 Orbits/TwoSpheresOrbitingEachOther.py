'''from the book,beautiful'''
from visual import *
rock1=sphere(pos=(5,5,0),
             radius=0.5,
             color=color.yellow)
rock2=sphere(pos=(-5,-5,0),
             radius=1,
             color=color.red,
             opacity=0.4)
scalefactor=10**12
G=6.11*10**-11
m1=1
p1=vector(-2,0,0)
m2=2
p2=vector(+2,0,0)

r=rock1.pos-rock2.pos
rhat=r/mag(r)
Fmag=G*m1*m2/mag(r)**2*scalefactor
F_on1=Fmag*(-rhat)
F_on2=-F_on1
t=0
deltat=0.01
'''this while loop is perfect for the two of them orbiting each other, dont modify'''

while True:
    rate(100)
    r=rock1.pos-rock2.pos#update distance each loop
    rhat=r/mag(r)
    Fmag=G*m1*m2/mag(r)**2*scalefactor#update the force magnitude
    F_on1=Fmag*(-rhat)#update the force on 1 by two, then apply momentum principle for 1
    p1=p1+F_on1*deltat
    rock1.pos=rock1.pos+(p1/m1)*deltat
    F_on2=-F_on1#use reciprocity to find force on 2 by one, then apply momentum principle for 2
    p2=p2+F_on2*deltat
    rock2.pos=rock2.pos+(p2/m2)*deltat

'''this loop is just one orbiting the other no mutual interaction'''
'''
while True:
    rate(100)
    r=rock1.pos-rock2.pos#update distance each loop
    rhat=r/mag(r)
    Fmag=G*m1*m2/mag(r)**2*scalefactor#update the force magnitude
    F_on1=Fmag*(-rhat)#update the force on 1 by two, then apply momentum principle for 1
    p1=p1+F_on1*deltat
    rock1.pos=rock1.pos+(p1/m1)*deltat
'''
