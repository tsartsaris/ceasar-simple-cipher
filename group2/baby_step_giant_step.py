#!/usr/bin/env python
# encoding: utf-8

__author__ = "Tsartsaris Sotiris"


from math import *
import time
# Discrete logarithm for g^x=h (p) by baby-step giant-step

def baby_giant(h,g,p):
    baby = [1]
    giant = [h]
    n = 1+int(floor(sqrt(p-1)))

    for i in range(1,n):
        baby.append( ((baby[i-1]*g)%p) )
        
    g = (g%p)^-n
    print n
    for j in range(1,n):
        giant.append( ((giant[j-1]*g)%p) )
    
    for inters in set(baby).intersection( set(giant) ):
        # print 'i =', baby.index(inters)
        # print 'j =', giant.index(inters)
        print 'x =',  baby.index(inters)+n*giant.index(inters)
t1 = time.time()
baby_giant( 1697571506, 2, 5915587277 )
t2 = time.time()
print t2-t1, ":secs"
