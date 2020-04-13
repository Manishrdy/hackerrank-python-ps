# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:48:52 2020

@author: Manish
"""

def simpleArraySum(ar):
    return(sum(ar))


ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
result = print(simpleArraySum(ar))