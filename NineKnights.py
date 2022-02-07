# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 13:37:28 2021

@author: thors
"""

lina1 = input()
lina2 = input()
lina3 = input()
lina4 = input()
lina5 = input()

#Teljum alla riddara
Nknights = lina1.count("k")+lina2.count("k")+lina3.count("k")+lina4.count("k")+lina5.count("k")
TaflBord = [list(lina1), list(lina2), list(lina3), list(lina4), list(lina5)]


#Boolean breyta sem er upphafstillts sem True
valid = True
#athugum hvort það séu 9 riddarar á borði
if(Nknights==9):
    #Ef svo er þá þurfum við að covera alla reita sem riddari getur farið í og ef það er annar riddari þar þá er valid sem False
    for i in range(len(TaflBord)):
        for j in range(len(TaflBord)):
            if(TaflBord[i][j] =="k"):
                if i + 1 in range(0, len(TaflBord)-1) and j + 2 in range(0, len(TaflBord)-1):
                    if TaflBord[i+1][j+2] == "k":
                        valid = False
                if i - 1 in range(0, len(TaflBord)-1) and j + 2 in range(0, len(TaflBord)-1):
                    if TaflBord[i-1][j+2] == "k":
                        valid = False
                if i + 1 in range(0, len(TaflBord)-1) and j - 2 in range(0, len(TaflBord)-1):
                    if TaflBord[i+1][j-2] == "k":
                        valid = False
                if i - 1 in range(0, len(TaflBord)-1) and j - 2 in range(0, len(TaflBord)-1):
                    if TaflBord[i-1][j-2] == "k":
                        valid = False
                if i + 2 in range(0, len(TaflBord)-1) and j + 1 in range(0, len(TaflBord)-1):
                    if TaflBord[i+2][j+1] == "k":
                        valid = False
                if i - 2 in range(0, len(TaflBord)-1) and j + 1 in range(0, len(TaflBord)-1):
                    if TaflBord[i-2][j+1] == "k":
                        valid = False
                if i - 2 in range(0, len(TaflBord)-1) and j - 1 in range(0, len(TaflBord)-1):
                    if TaflBord[i-2][j-1] == "k":
                        valid = False
                if i + 2 in range(0, len(TaflBord)-1) and j - 1 in range(0, len(TaflBord)-1):
                    if TaflBord[i+2][j-1] == "k":
                        valid = False

else:
    valid = False

if valid:
    print("Valid")
else:
    print("invalid")
        
               