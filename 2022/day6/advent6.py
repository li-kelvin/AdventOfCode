#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 20:59:50 2022

@author: kelvinli
"""

file1 = open('advent6.txt', 'r')
Lines = file1.readlines()

for i in range(13,len(Lines[0])+1):
    List = []
    
    for j in range(13,0,-1):
        List.append(Lines[0][i-j])
    
    if len(set(List)) == len(List):
        print(i+1)
        
    
    
    
        
        
    
    


    

    


