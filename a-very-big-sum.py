# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:52:23 2020

@author: Manish
"""

def aVeryBigSum(ar):
    return(sum(ar))
    #return(int(sum(ar)))

ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
result = print(aVeryBigSum(ar))