# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:18:02 2020

@author: Manish
"""

import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count = 0
    for i in range(len(apples)):
        if(apples[i]>=0):
            d = a + apples[i]
            if d in range(s,t+1):
                count = count + 1
            
    print(count)
    count1 = 0
    for j in range(len(oranges)):
        if(oranges[j]<0):
            #oranges[j]=-1*oranges[j]
            d = b + oranges[j]
            #print(d)
            if d in range(s,t+1):
                count1 = count1 + 1
    print(count1)
    
st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
countApplesAndOranges(s, t, a, b, apples, oranges)
