#to check whether  a number is prime
from math import sqrt
n=0;
x=0;
def isprime():
    i=2;
    count=0;
    x=int(sqrt(n))
    while i<=x:
        if n%i==0:
            count=count+1
            i=i+1
        else:
            i=i+1
    if count==0:
        print(' True')
    else:
        print('false')
n=int(input('Enter a number :'))
isprime()
