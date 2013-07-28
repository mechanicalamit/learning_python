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


print('this program displays the prime factors of a number entered')
i=1
j=1
k=0
num=int(input('enter a number'))
while i<=num:
  if num%i==0:
    k=0
    while j<=i
      if i%j==0:
        k=k+1
      j=j+1
      if k==2:
        print(i)
  i=i+1      
