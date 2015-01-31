#!/usr/bin/env python
# encoding: utf-8

__author__ = "Tsartsaris Sotiris"
__credits__ = ["Daniel O'Donovan,Tsartsaris Sotiris"]
__license__ = "APACHE 2.0"
__version__ = "1.0.1"
__maintainer__ = "Tsartsaris Sotiris"
__email__ = "info@tsartsaris.gr"
__status__ = "Development"



import sys
import os
import math
import gmpy
    
def shanks( y, a, n):
    """ Shanks' baby-step giant-step for finding discrete logarithms 
        of form : x = log_a ( y mod n )
    """
    s = gmpy.sqrt( n )

    S = {} # calculate the baby steps
    T = {} # calculate the giant steps
    for i in range( s ): 
        S['%s' % gmpy.mpz( ( y * (a ** i))      % n ) ] = int( i ) 
        T['%s' % gmpy.mpz( ( a ** ((i+1) * s) ) % n ) ] = int( i )
        
    # mathching and computing
    for key in S.keys():
        if key in T:
            r  =  S[key]
            st = (T[key] + 1) * s
            break
    x = st - r
    
    print 'So        log_%d %d\t(mod %d) =\t%d ' % ( a, y, n, x)
    print 'or equiv.     %d^%d\t(mod %d) =\t%d ' % ( a, x, n, y)
    return x
    
if __name__ == '__main__':
    x = shanks( 64, 2, 524287 )
