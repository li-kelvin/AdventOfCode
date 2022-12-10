#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 23:10:11 2022

@author: kelvinli
"""

file1 = open('advent4.txt', 'r')
Lines = file1.readlines()

counter1 = 0
counter2 = 0

for line in Lines:
    
    match = []    

    for i in line.rsplit(','):
        for j in i.rsplit('-'):
            match.append(j.rstrip('\n'))
                
    list1 = []
    list2 = []
    
    for nums in range(int(match[0]), int(match[1])+1):
        list1.append(nums)
        
    for nums in range(int(match[2]), int(match[3])+1):
        list2.append(nums)
    
    check1 = all(item in list1 for item in list2) or all(item in list2 for item in list1) 
    check2 = any(item in list1 for item in list2)
    


    if check1:
        counter1 += 1
    
    if check2:
        counter2 += 1
        

print("Score 1:", counter1)
print("Score 2:", counter2)
        
    
        
        

    

    


       
