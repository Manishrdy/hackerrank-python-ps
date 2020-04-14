# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:46:39 2020

@author: Manish
"""

def birthdayCakeCandles(ar):
    count = 0
    ar.sort()
    for i in range(0,ar_count):
        if(ar[i] == ar[ar_count-1]):
            count = count + 1
    return(count)

ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
result = print(birthdayCakeCandles(ar))