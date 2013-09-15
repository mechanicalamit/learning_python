from math import sqrt

#to check whether  a number is prime
def isprime(n):
    x=int(sqrt(n))
    for i in range(2,x+1):
        if n%i==0:
            return False
    else:
        return True

"""
Lets write an algorithm to check for a prime

First some thoughts to help us

1. Defintion of Prime : natural number greater than 1 that has no positive
   divisors other than 1 and itself

2. If the number has a divisor, it must have more than one divisor.
   e.g 24, divisors are 2,3,4,6,8,12.
   Also the divisors would be paired, 2 pairs with 12, 3 pairs with 8, etc.
   So if we have a big divisor, we must also have a smaller paired divisor
   Hence checking till floor(sqrt(n)) is sufficient

3. Finding one divisor is sufficient
   If we find one divisor, we can immediately tell the number is not prime, 
   we do not need to continue looping over the complete list

So an algorithm would look like this

-- get n into function
---- loop over index from 2 thru floor(sqrt(n))
------ if the index is a divisor to n, return False immediately, no need to check for others
---- if the loop exists and we still have not found a divisor, the number must be prime, return true

"""
