#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#factorial of number

factorial =1
# user input data
number = int(input('Enter a number:'))
if number <0:
    print('Factorial does not exist')
else:
    for index in range(1,number+1):
         factorial = factorial *index
    print('Factorial of',number,'is',factorial)


# In[ ]:


#prime or composite

# user input data
num = int(input('Enter a number:'))
if num>1:
    for index in range(2,num):
        if (num % index) ==0:
            print(num, 'is composite number')
            break
    else:
        print(num,'is prime number')
else:
    print('Neither it prime nor composite number')


# In[ ]:


#palindrome string
#user input data
value = input('Enter the input string: ')
#to slice the given string
if(value == value[::-1]):
    print('It is a palindrome')
else:
    print('It is not a palindrome')


# In[ ]:


#To find third side of right angled triangle
from math import sqrt
print('Consider a,b are sides of triangle and c is hypotenuse. enter which side to find (a,b,c)')
side= input('Enter the side ')
if side == 'c':
    a = float(input('Enter side of triangle a: '))
    b = float(input('Enter side of triangle b: '))
    c= sqrt(a*a + b*b)
    print('The third side c is: %g ' %(c))
#Else if, the user wants to find for the side a.
elif side == 'a':
    b = float(input('Input the length of side b: '))
    c = float(input('Input the length of side c: '))
    a = sqrt((c * c) - (b * b))
    print('The third side a is: %g ' %(a))
#Else if, the user wants to find for the side b.
elif side == 'b':
    a = float(input('Enter side of triangle a: '))
    c = float(input('Enter side of triangle c: '))
    b = sqrt(c * c - a * a)
    print('The third side b is: %g ' %(b))
else:
    print('Invalid Input!')


# In[ ]:


#frequency of characters in string

#user input data
user_input = input('enter the input string: ')
def charFrequency(user_input):
    dict = {}
    for char in user_input:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict
print('The frequency of each char in string is',charFrequency(user_input))


# In[ ]:




