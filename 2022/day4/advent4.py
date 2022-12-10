#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 23:10:11 2022

@author: kelvinli
"""

file1 = open('advent4.txt', 'r')
Lines = file1.readlines()

counter = 0

for line in Lines:
    list1 = []
    list2 = []
    list3 = []    

    for i in line.rsplit(','):
        for j in i.rsplit('-'):
            list3.append(j.rstrip('\n'))
    
    for k in range(int(list3[0]), int(list3[1])+1):
        list1.append(k)
        
    for k in range(int(list3[2]), int(list3[3])+1):
        list2.append(k)
    
    check1 = any(item in list1 for item in list2)

    
    
    if check1:
        counter += 1
    
    print(list1, list2, counter)
        
        

    

    


       
