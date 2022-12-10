#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:38:56 2022

@author: kelvinli
"""

file1 = open('advent2.txt', 'r')
Lines = file1.readlines()

matches = []
rule1 = 0
rule2 = 0

## stripping lines and appending to new list
for fight in Lines:
    matches.append(fight.strip())

for match in matches:
    if match == "A X":   
        rule1 += 1 + 3 # rock vs rock #tie
        rule2 += 3 + 0 # rock vs scissors #lost 
        
    elif match == "A Y": 
        rule1 += 2 + 6 # rock vs paper #win
        rule2 += 1 + 3 # rock vs rock #tie
    
    elif match == "A Z": 
        rule1 += 3 + 0 # rock vs scissors #lost
        rule2 += 2 + 6 # rock vs papaer #win
    
    elif match == "B X":  
        rule1 += 1 + 0 # paper vs rock #lost
        rule2 += 1 + 0 #paper vs rock #lost

    elif match == "B Y":  
        rule1 += 2 + 3 # paper vs paper #tie
        rule2 += 2 + 3 #paper vs paper #tie

    elif match == "B Z":  
        rule1 += 3 + 6 # paper vs scissors #win
        rule2 += 3 + 6 # paper vs scissors #win

    elif match == "C X":  
        rule1 += 1 + 6 # scissors vs rock #win
        rule2 += 2 + 0 #scissors vs paper #lost
    
    elif match == "C Y":  
        rule1 += 2 + 0 #scissors vs paper #lost
        rule2 += 3 + 3 #scissors vs scissors #tie
        
    elif match == "C Z":
        rule1 += 3 + 3 # scissors vs scissors #tie
        rule2 += 1 + 6 #scissors vs rock #win

print("Score 1:", rule1)
print("Score 2:", rule2)
    