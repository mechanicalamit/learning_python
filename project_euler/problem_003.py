""" 
Project Euler Problem #3

Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

""" Hints to make better
1. Make a function isprime(int) which returns True of False
2. Instead of counting up from 1 to search for largest prime factor,
   you can count down from the number itselt. The first match is the
   largest, no need to store a max
3. It can be optimized further too, hint will be updated, once 1 and 2 
   are completed.
"""


i=2;
n=600851475143;
x=1;
def reset():
    global x
    x=1
from math import sqrt
while i<=int(sqrt(n)):
               if n%i==0:
                   while x<=int(sqrt(i)):
                     if i%x==0:
                       print(i)
                       x=x+1
                     else:
                       x=x+1 
                   i=i+1
                   reset()
               else:
                   i=i+1
                   reset() 
