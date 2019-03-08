# Created by: Chris Asante
# Created on: 08-Mar-2019
# Created for: ICS3U
# Unit 3-05
# This program calculates the factorial of a number

fact=1
num=int(input("enter the number:"))

i=1
while(i<num):
    i=i+1
    fact=fact*i
    
print(fact)