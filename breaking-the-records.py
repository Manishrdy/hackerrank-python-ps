# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:17:44 2020

@author: Manish
"""

# Complete the breakingRecords function below.
def breakingRecords(scores):
    current_best = scores[0]
    current_worst = scores[0]
    count_best = count_worst = 0
    for i in range(len(scores)):
        if(scores[i] > current_best):
            current_best = scores[i]
            count_best = count_best + 1
        if(scores[i] < current_worst):
            current_worst = scores[i]
            count_worst = count_worst + 1
    return(count_best,count_worst)

n = int(input())
scores = list(map(int, input().rstrip().split()))
result = print(breakingRecords(scores))