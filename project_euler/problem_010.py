#PROJECT EULER PROBLEM 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
n=20;
i=2;
count=0;
s=77;
from math import sqrt
def reset(): # to reset the value of count
    global count
    count=0
while n<=2000000:
   if n%2!=0 or n%3!=0 or n%5!=0 or n%7!=0 or n%11!=0 or n%13!=0 or n%17!=0 or n%19!=0:  # excluding no's divisible by primes
        for i in range(2,(n-1)/2):
         if i<=int(sqrt(n)): 
          if i%2!=0 or i%3!=0 or i%5!=0 or i%7!=0 or i%11!=0 or i%13!=0 or i%17!=0 or i%19!=0:
              if n%i==0:
                  count=count+1
              i=i+1
          else:
              i=i+1
         else:
             i=i+1
        if count==0:   
             print(n)
             s=s+n
        reset()     
        n=n+1
    else:
        n=n+1
print("sum of prime numbers")
print(s)    

