"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included."""

n=0;
x=0;
s=0;
def reset():
    global x
    x=0
from factorial import *
for n in range(3,50000):
    a=str(n)
    for i in a:
        x=factorial(int(i))+x
    print(x)
    if x==n:
        s=s+n
    reset()
print('sum',s)
