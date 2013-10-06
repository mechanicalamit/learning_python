"""The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?"""
a=1;
c=1;
n=0;
i=1;
while i<=10000:
        if(i<=2):
                n=1
        else:
                n=a+c
                a=c
                c=n
        x=str(n)
        if len(x)>1000:
                print('more than 1000 digit', i-5)
                break
        i=i+1
