#PROJECT EULER PROBLEM 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
from math import sqrt
n=2;
s=0
def abc():
    global s
    s=s+n
def isprime(n):
    i=2;
    count=0;
    x=int(sqrt(n))
    for i in range(2,x+1):
        if n%i==0:
            return
    else:
        print(n)
        abc()
while n<=2000000:
    isprime(n)
    n=n+1
print(s)
