#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:04:14 2022

@author: kelvinli
"""

file1 = open('advent3.txt', 'r')
Lines = file1.readlines()

final_list = []
list1 = []
list2 = []
total1 = 0
total2 = 0

# strip list
for i in Lines:
    final_list.append(i.strip())
    
for i in final_list:
    first_half = sorted(set(i[:len(i)//2]))
    second_half = sorted(set(i[len(i)//2:]))
    
    for char1 in first_half:
        for char2 in second_half:
            if char1 == char2:
                list1.append(char2)
                
for i in list1:
    if ord(i) > 94:
        total1 += ord(i) - 96
    elif ord(i) < 94:
        total1 += ord(i) - 38

        
for i in range(int(len(final_list)/3)):
    first_num  = set(final_list[i*3])
    second_num = set(final_list[i*3 + 1]) 
    third_num = set(final_list[i*3 + 2])
        
    
    for char1 in first_num:
        for char2 in second_num:
            for char3 in third_num:
                if char1 == char2 and char2 == char3:
                    list2.append(char3)
                        
for i in list2:
    if ord(i) > 94:
        total2 += ord(i) - 96
    elif ord(i) < 94:
        total2 += ord(i) - 38
        
print("Total 1:", total1)
print("Total 2:", total2)

                
    


