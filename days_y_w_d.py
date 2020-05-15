# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:25:00 2020

@author: shiva dumnawar
"""

'''  Write a program to convert days into years, 
weeks and days. '''

days=int(input("enter days :")) 

years= days//365

weeks= (days%365)//7

remaining_days= (days%365)%7

print("number of years :", years)

print("number of weeks :", weeks)

print("remaining days :", remaining_days)
