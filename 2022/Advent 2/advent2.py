#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:38:56 2022

@author: kelvinli
"""

file1 = open('advent2.txt', 'r')
Lines = file1.readlines()

final_list = []
sum = 0

for i in Lines:
    final_list.append(i.strip())

for i in final_list:
    if i == "A X":    ## rock vs rock #tie
        sum += 1 + 3
    
    elif i == "A Y":  ## rock vs paper #win
        sum += 2 + 6
        
    elif i == "A Z":  ## rock vs scissors #lost
        sum += 3 + 0
    


    elif i == "B X":  ## paper vs rock #lost
        sum += 1 + 0
        
    elif i == "B Y":  ## paper vs paper #tie
        sum += 2 + 3
    
    elif i == "B Z":  ## paper vs scissors #win
        sum += 3 + 6
        
        
        
    elif i == "C X":  ## scissors vs rock #win
        sum += 1 + 6
    
    elif i == "C Y":  ## scissors vs paper #lost
        sum += 2 + 0
        
    elif i == "C Z":  ## scissors vs scissors #tie
        sum += 3 + 3
        

print(sum)
    