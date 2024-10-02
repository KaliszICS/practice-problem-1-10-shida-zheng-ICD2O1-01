'''
    Lesson: Math Library
    Author: Mr. Kalisz
    Date Created: October 2, 2024
    Date Last Modified: October 2, 2024
'''

#import - Not part of basic python, it needs to be imported
import math #Has to be at the top of your file

#ceil - ceiling -> round up
#ceil returns a integer
#creates a copy

num = 3.2

print(math.ceil(num)) # Function

#floor

print(math.floor(num))

#isqrt - integer square root, only usable on integers

num = 8

#print(math.isqrt(num)) #this will give a runtime error
print(math.isqrt(num)) #always be rounded down

#sqrt - square root - always returns a float

print(math.sqrt(9.8))

#trunc - removes the decimal point and everything after it, the same as int()

print(math.trunc(9.7))
print(math.trunc(-9.7))
print(math.floor(-9.7))
print(int(-9.7))

#Many More: https://docs.python.org/3/library/math.html