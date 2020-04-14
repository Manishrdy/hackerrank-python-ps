# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:53:29 2020

@author: Manish
"""

def timeConversion(s):
    #
    # Write your code here.
    #
    if(s[8:11] == "PM"):
        pm = int(s[0:2])
        if(pm is not 12):
            pm = pm + 12
        pm = str(pm)
        return(pm+s[2:8])
    elif(s[8:11] == "AM"):
        if(s[0:2] == "12"):
            pm = int(s[0:2])
            pm = pm - 12
            pm = str(pm)
            k = str("0")
            return(k+pm+s[2:8])
        elif(s[0:2] != 12):
            return(s[0:8])
    elif(s[8:11] == "PM"):
        if(s[0:11] == "12"):
            return(s[0:8])
    elif(s[0:2] == "00"):
        return(s[0:8])
    else:
        return(s[0:11])
    
s = input()
result = print(timeConversion(s))