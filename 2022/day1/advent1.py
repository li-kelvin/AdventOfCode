#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 00:05:05 2022

@author: kelvinli
"""

file1 = open('advent1.txt', 'r')
elves = file1.readlines()

group_cals = 0
group = 0
list = [0]


for elf in elves:
    # if lineskip;
        # +=1 to group counter, reset group calorie counter and append new group new group calorie counter to list
    if elf == "\n":
        group += 1
        group_cals = 0
        list.append(group_cals)
        
    # else:
        # add elf calorie to group calorie counter and update in current group position
    else:
        group_cals += int(elf)
        list[group] = group_cals
        
list.sort(reverse=True)        
print("Max Calorie:", list[0])
print("Sum of Top 3:", list[0]+list[1]+list[2])