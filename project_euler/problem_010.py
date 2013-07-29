n=2;
i=2;
count=0;
s=0;
def reset():
    global count
    count=0
while n<=2000000:
    print('number is');print(n)
    for i in range(2,(n-1)):
        if n%i==0:
            count=count+1
        i=i+1
    print('number of factors'):print(count)
    if count==0:
        s=s+n
    reset()
    n=n+1
print('sum of primes')
print(s)
