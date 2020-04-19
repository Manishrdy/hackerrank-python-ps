# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:18:09 2020

@author: Manish
"""

def kangaroo(x1, v1, x2, v2):
    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"

x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
result = print(kangaroo(x1, v1, x2, v2))