'''
#INTRODUCTION
There are 3 types of numbers in python:
1.Integer- whole number,it can either positive or negative eg 1, 0, -10...
2.Float - A number with a decimal point, it can either be positive or negative eg 2.5, 1.2, -2.9...
3.Complex - A number which has a real value and an imaginary value eg 2+ 3j


# Arithmetric Operations
addition = +
subtraction = -
multiplication = *
division = /
floor division = //
modulus = %
exponent = **

'''

# Integers
x = 10
y = -5
print(x/y) 

#Float
a = 4.2 
b = 7.9
print(a/b)  

# Complex
z = 3 + 4j
print(z.real)
print(z.imag) 

#Conversions to other numeric types
float()
int()
complex()

x = 5.9
print(int(x))
print(float(x))
print(complex(x))

#Built=in methods
'''The absolute method'''
x = -10
print(abs(x))

'''The round method'''
x = 3.899
print(round(x))

'''Power method'''
x = (2,3)
print(pow(x))

'''The max and min methods'''
x =(2,4,6,8)
print(max(x))
print(min(x)) 

#Multiple assignments
'''There are many ways of writing multiple assignments'''
x, y, z = 10, 40, 50
a = b = c = 10

x,y = a,b
23,12 = 12,23
'''unpacking assignments'''
nums = [1, 2, 3]
x,y,z = nums

#Constants
'''The only of stating a constant in python is by turning the variable
into an uppercase '''
PI = 3.14
GRAVITY = 9.81






