#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:04:14 2022

@author: kelvinli
"""

file1 = open('advent3.txt', 'r')
Lines = file1.readlines()


final_list = []
list = []
total = 0

for i in Lines:
    final_list.append(i.strip())
    
    
for i in range(100):
    first_half  = set(final_list[i*3])   #sorted(set(i[:len(i)//2]))
    second_half = set(final_list[i*3 + 1]) #sorted(set(i[len(i)//2:]))
    third_half = set(final_list[i*3 + 2])
        
    
    for i in first_half:
        for j in second_half:
            for k in third_half:
                if i == j and j == k:
                    list.append(i)
                    print(list)
                
                
for i in list:
    if ord(i) > 94:
        total += ord(i) - 96
        print(total)

    elif ord(i) < 94:
        total += ord(i) - 38
        print(total)

                

    
    
    


