# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:45:11 2020

@author: shiva dumnawar
"""

''' GCD (Greatest Common Divisor) or 
HCF (Highest Common Factor) of two numbers
 is the largest number that divides
 both of them.  '''

# Gcd or Hcf of two numbers

def gcd_rec(a,b):
    if b==0:
        return a
    else:
        return gcd_rec(b, a%b)
    
gcd_rec(6,21)
