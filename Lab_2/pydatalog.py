from pyDatalog import pyDatalog
import random
pyDatalog.create_terms('Sum,Y,SumRndInt,median,SR')
"""
Task 1
"""
Sum[Y] = Y+Sum[Y-1]
Sum[1] = 1
print(Sum[100]==Y)
"""
Task 2
"""
SR[Y]=(Y+1)/2
SR[1]=1
print(SR[100]==Y)
"""
Task 3
"""
SumRndInt[Y] = random.randint(1,100) + SumRndInt[Y-1]
SumRndInt[1] = random.randint(1,100)
print(SumRndInt[100]==Y)
"""
Task 4
"""
median[Y] = (random.randint(1,100) + median[Y-1]) / 2
median[1] = random.randint(1,100)
print(median[100]==Y)



