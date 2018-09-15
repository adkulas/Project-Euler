# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:33:17 2018

@author: Adam
"""
sum = 0
for i in range(1000):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i
    else:
        pass
    
print(sum)
        