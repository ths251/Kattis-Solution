# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:31:47 2021

@author: thors
"""
count = int(input())
outcome = []

    
for i in range(count):
    strengur = input()
    

    strengur1 = strengur.split()
    x1 = int(strengur1[0])
        
    
    if(strengur1[1]=="Jan"):
        #month = 1
        if(x1<21):
            outcome.append("Capricorn")
        else:
            outcome.append("Aquarius")
    
    if(strengur1[1]=="Feb"):
        if(x1<20):
            outcome.append("Aquarius")
        else:
            outcome.append("Pisces")
    
    
    if(strengur1[1]=="Mar"):
        if(x1<21):
            outcome.append("Pisces")
        else:
            outcome.append("Aries")
    
    if(strengur1[1]=="Apr"):
        if( x1<21):
            outcome.append("Aries")
        else:
            outcome.append("Taurus")
        
    if(strengur1[1]=="May"):
        if(x1<21):
            outcome.append("Taurus")
        else:
            outcome.append("Gemini")
    
    if(strengur1[1]=="Jun"):
        if(x1<22):
            outcome.append("Gemini")
        else:
            outcome.append("Cancer")
    
    if(strengur1[1]=="Jul"):
        if(x1<23):
            outcome.append("Cancer")
        else:
            outcome.append("Leo")
            
    if(strengur1[1]=="Aug"):
        if(x1<23):
            outcome.append("Leo")
        else:
            outcome.append("Virgo")
            
    if(strengur1[1]=="Sep"):
        if(x1<22):
            outcome.append("Virgo")
        else:
            outcome.append("Libra")
    
    if(strengur1[1]=="Oct"):
        if(x1<23):
            outcome.append("Libra")
        else:
            outcome.append("Scorpio")
    
    if(strengur1[1] == "Nov"):
        if(x1<23):
            outcome.append("Scorpio")
        else:
            outcome.append("Sagittarius")
    
    if(strengur1[1]=="Dec"):
        if(x1<22):
            outcome.append("Sagittarius")
        else:
            outcome.append("Capricorn")
    

print('\n'.join(map(str, outcome)))