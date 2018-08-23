from visual import *
from visual.graph import*
from random import random
gg=gcurve(color=color.yellow)
n=0
while n < 20:
    rate(10)
    a=random()
    print (a)
    gg.plot(pos=(n,a))
    n=n+1
'''
a) the grahs is plotting 20 times a random number from 0 to 1,
graphs are not the same every time
b) maximun number is 1
c) minimumn munber is around 0 
'''
