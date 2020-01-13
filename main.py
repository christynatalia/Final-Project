#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 13:39:41 2019

@author: christynataliaj
"""

from inputnumbers import Data

from introduction import Introduction

import matplotlib.pyplot as plt

import math

import numpy

from matplotlib import pyplot

import sys

#Make the lists for the history
historyList = []

#Loop everytime the user type yes on the introduction
print('This program can make a quadratic equations graph.\n')
while True:
    intro = Introduction()
    intromessage = intro.programintro()
    intromessage = intromessage.lower()
    if intromessage == 'yes':
        print("The formula is Ax",chr(0x00B2) ,"+ Bx + C")
        value = Data()
        valueA = int(value.newInputA())
        valueB = int(value.newInputB())
        valueC = int(value.newInputC())
    elif intromessage == 'no':
        print('Thankyou for using this program. See you next time!')
        sys.exit()
    else:
       print("Error. Please restart this program")
       sys.exit()
       
       
    if valueA != 0:
        #function to count the discriminant. 
        def discriminant():
            global discriminantValue
            discriminantValue =(((valueB**2) - (4*valueA*valueC)))
            return discriminantValue
        print("The discriminant of this graph is = ",discriminant())
        
        
        def roots():
            if discriminantValue < 0 :
                print("can't count because it is imaginary(non-real)roots" )
                sys.exit()
            else:
                rootss = math.sqrt(int(discriminantValue))
                global x1
                global x2
                x1 = round((-valueB + rootss) / (2*valueA),2)
                x2 = round((-valueB - rootss) / (2*valueA),2)
                return x1,x2
        
        
        print("X1,X2 = ",roots())
        
        def highestpoint():
            global highx
            global highy
            highx = (-valueB) / (2 * valueA)
            highy = -((valueB**2) - (4*valueA*valueC))/ (4*valueA)
            return highx,highy
        
        print("The highest point of this graph is = ",highestpoint())
        
        #for the conclusion part.
        def conclusion():
            if (discriminantValue > 0 and valueA > 0):
                conclmsg = ("The conclusion is Graph intersects the x-axis ")
            elif (discriminantValue > 0 and valueA < 0):
                conclmsg = ("The conclusion is Graph intersects the x-axis ")
            elif (discriminantValue == 0 and valueA > 0): 
                conclmsg = ("The conclusion is Grafik menyinggung sumbu x ")
            elif (discriminantValue == 0 and valueA < 0):
                conclmsg = ("The conclusion is Grafik menyinggung sumbu x ")
            elif (discriminantValue < 0 and valueA > 0):
                conclmsg = ("No intercepts.")
            elif (discriminantValue < 0 and valueA < 0):
                conclmsg = ("No intercepts.")
            return conclmsg
        
        print(conclusion())
        
        #for the history
        historyList.append(str(valueA) + ", " + str(valueB) + ", " + str(valueC))
        
        def printHistory():
            for i in range(len(historyList)):
                print("History {}: {}".format(i + 1, historyList[i]))
        printHistory()
        
 
        #Make the graph 
        x=numpy.linspace(float(x2),float(x1),100);
        y=(valueA *( x ** 2)) +(( x * valueB ))+ valueC
        pyplot.plot(x,y);
        plt.scatter(float(highx),float(highy),s=20, c= "green",label = 'HP=' + '('+ str(highx) + ',' + str(highy)+')')
        plt.scatter(float(x1),float((valueA *( x1 ** 2)) +(( x1 * valueB ))+ valueC), s = 20, c= 'red', label = 'x1('+ str(x1)+ str(')'))
        plt.scatter(float(x2),float((valueA *( x2 ** 2)) +(( x2 * valueB ))+ valueC), s = 20, c= 'black', label = 'x2('+ str(x2)+ str(')'))
        plt.legend()
        pyplot.title("Quadratic Equations Curve")
        pyplot.xlabel("x axis")
        pyplot.ylabel("y axis")
        pyplot.grid()
        pyplot.show()
        plt.show()
        
    else:
        print("You can't assign 0 as A. Please try again.")
    


    
 
