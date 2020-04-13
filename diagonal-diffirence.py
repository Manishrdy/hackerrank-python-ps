# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:54:20 2020

@author: Manish
"""

def diagonalDifference(arr):
    # Write your code here
    d1=d2=0
    for i in range(0,n):
        for j in range(0,n):
            if(i==j):
                d1 = d1 + arr[i][j]
            if(i== n-j-1):
                d2 = d2 + arr[i][j]
    return(abs(d1-d2))

n = int(input().strip())
arr = []
for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

result = print(diagonalDifference(arr))