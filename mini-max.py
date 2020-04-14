# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:44:48 2020

@author: Manish
"""

def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[0:len(arr)-1]),sum(arr[1:len(arr)]))

arr = []
arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)