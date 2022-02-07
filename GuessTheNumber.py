# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:09:41 2021

@author: thors
"""

#Virkar
#talan sem forritið reynir að giska á

number = 1000
#listi af tölum milli 1 og 1000
sequence = list(range(1,1001))
begin_index = 0
end_index = len(sequence)-1
guesses = 0

while(guesses < 10):
    midpoint = begin_index + (end_index - begin_index) //2
    midpoint_value = sequence[midpoint]
    print(midpoint_value)
    Svar = input() 
    
    if(Svar == "correct"):
        break
    
    elif(Svar == "lower"):
        end_index = midpoint -1
        guesses +=1  
        
    else:
        begin_index = midpoint +1
        guesses +=1
    
    
        
