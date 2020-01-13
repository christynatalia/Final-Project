#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 13:38:02 2019

@author: christynataliaj
"""

class Data():
    def __init__(self):
        self.__inputA = int(input("Input the A= "))
        self.__inputB = int(input("Input the B= "))
        self.__inputC = int(input("Input the C= "))
        
    def newInputA(self):
        return self.__inputA

    def newInputB(self):
        return self.__inputB
    
    def newInputC(self):
        return self.__inputC