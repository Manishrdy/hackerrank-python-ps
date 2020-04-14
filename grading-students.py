# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:49:01 2020

@author: Manish
"""

def gradingStudents(grades):
    for i in range(0,grades_count):
        if(grades[i] > 37):
            mod = grades[i] % 5
            if(mod >= 3):
                grades[i] = grades[i] + (5 - mod)
    return(grades)

grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = print(gradingStudents(grades))