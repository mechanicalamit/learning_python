"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

n=1;
a=0;
b=0;
count=0;
running=True
maxi=0
def reset():
    global count,running
    count=0
    running=True
while n<1000000:
    a=n;
    print(a)
    while running:
        if a%2==0:
            a=a/2
            count=count+1
            if a==1:
                running=False
        else:
            a=3*a+1
            count=count+1
    if count>maxi:
        maxi=count
        b=n
    reset()
    n=n+1
print(b,maxi)
