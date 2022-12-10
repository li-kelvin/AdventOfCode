#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 00:05:05 2022

@author: kelvinli
"""

file1 = open('advent9.txt', 'r')
Lines = file1.readlines()

greater = 1
cycle = 0

for i in Lines:
    if i[0:4] == "noop":
        cycle += 1
    
    elif i[0:4] == "addx":
        cycle += 1
        print(cycle, greater)
        greater += int(i[5:])
        cycle += 1
        
        
        


    print(cycle, greater)
    
    
    
print(20* 21 + 60 *23    +100 * 25  +140 * 14 +180* 5 + 220*21)
