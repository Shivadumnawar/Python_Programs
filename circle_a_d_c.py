'''  Write a  program to enter radius 
        of a cirle and  find its diameter,
      area and cirumference. 
 '''
from math import pi
r= int(input("enter radius :"))
dia = 2* r
area= pi *(r**2)
circumference = 2* pi* r
print("diameter of a circle: ",dia)
print("area of a circle :",area)
print("circumference of a circle :",circumference)