# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:04:57 2020

@author: flowe
"""

Phys = input("Physics Grade:")
Digital_Logic = input("CSE 2301 Grade:")
CS = input("CSE 1729 Grade:")
Diffeq = input("Diff Eq Grade:")
Gen_ed = input("gen ed Grade:")



my_grades = [Phys, Digital_Logic, CS, Diffeq, Gen_ed]



total = 0
for element in my_grades[0:2]:
    if element == "A+":
        total = total + (4.0 * 4)
    elif element == "A":
        total = total + (4.0 * 4)
    elif element == "A-":
        total = total + (3.7* 4)
    elif element == "B+":
        total = total + (3.3* 4)
    elif element == "B":
        total = total + (3.0* 4)
    elif element == "B-":
        total = total + (2.7* 4)
    elif element == "C+":
        total = total + (2.3* 4)
    elif element == "C":
        total = total + (2.0* 4)
        
for element in my_grades[2:]:
    if element == "A+":
        total = total + (4.0 * 3)
    elif element == "A":
        total = total + (4.0 * 3)
    elif element == "A-":
        total = total + (3.7* 3)
    elif element == "B+":
        total = total + (3.3* 3)
    elif element == "B":
        total = total + (3.0* 3)
    elif element == "B-":
        total = total + (2.7* 3)
    elif element == "C+":
        total = total + (2.3* 3)
    elif element == "C":
        total = total + (2.0* 3)
        

print(total/17)
    




#total = 0
#i = 0

#for element in my_grades:
#    if element == "A+":
#        total = total + (4.0 * 4)
#    elif element == "A": 
#        total = total + (4.0 *4)
#        i +=1
#    elif element == "A-":
#        total = total + (3.7*4)
#        i +=1
#    elif element == "B+":
#        total = total + (3.3*4)
#    elif element == "B":
#        total = total + (3.0*4)
#    elif element[i] == "B-":
#        total = total + (2.7*4)
#    elif element[i] == "C+":
#        total = total + (2.3*4)
#    elif element[i] == "C":
#        total = total + (2.0*4)
#            
#while i >= 2:
#    for element in my_grades:
#        if element[i] == "A+":
#            total = total + (4.0 * 3)
#        elif element[i] == "A":
#            total = total + (4.0 *3)
#            i +=1
#        elif element[i] == "A-":
#            total = total + (3.7*3)
#            i +=1
#        elif element[i] == "B+":
#            total = total + (3.3*3)
#        elif element[i] == "B":
#            total = total + (3.0*3)
#        elif element[i] == "B-":
#            total = total + (2.7*3)
#        elif element[i] == "C+":
#            total = total + (2.3*3)
#        elif element[i] == "C":
#            total = total + (2.0*3)
#print(total/11)