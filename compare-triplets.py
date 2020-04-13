# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:51:10 2020

@author: Manish
"""

def compareTriplets(a, b):
    k = m = 0
    for i in range(0,3):
        if (a[i] < b[i]):
            k = k + 1
        elif(a[i] > b[i]):
            m = m + 1
    return(m,k)

a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = print(compareTriplets(a, b))