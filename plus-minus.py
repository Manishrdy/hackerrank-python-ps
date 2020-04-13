# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:56:26 2020

@author: Manish
"""

def plusMinus(arr):
    pe = ne = ze = 0
    for i in range(0,n):
        if(arr[i] > 0):
            pe = pe + 1
        if(arr[i] < 0):
            ne = ne + 1
        if(arr[i] == 0):
            ze = ze + 1
    print(round(pe/n,6))
    print(round(ne/n,6))
    print(round(ze/n,6))
    
n = int(input())
arr = list(map(int, input().rstrip().split()))
plusMinus(arr)