"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

n=0
d=0
i=1
summ=0
l=1
s=0
def reset():
    global i,l,d,s
    s=0
    i=1
    l=1
    d=0
for n in range(1,10000):
    for i in range (1,int(n/2+1)):
        if n%i==0:
            d=d+i
    for l in range(1,int(d/2+1)):
        if d%l==0:
            s=s+l
    if s==n and n!=d:
        summ=summ+d
    reset()
print(summ)
