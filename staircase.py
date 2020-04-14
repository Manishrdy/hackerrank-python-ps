# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:43:45 2020

@author: Manish
"""

def staircase(n):
    for i in range(1,n+1):
        print(' ' * (n - i) + '#' * i)

n = int(input())
staircase(n)