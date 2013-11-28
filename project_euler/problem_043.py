"""The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property."""

list1b=['0','1','2','3','4','5','6','7','8','9']
li=[]
t=0
s=0
d1=0
d2=0
d3=0
d4=0
d5=0
d6=0
d7=0
d8=0
d9=0
d10=0
y=0
def reset():
    global li
    li=[]
for n in range(1023456788,9876543211):
    t=n
    d1=int(t/1000000000)
    li.append(d1)
    t=t%1000000000
    d2=int(t/100000000)
    li.append(d2)
    t=t%100000000
    d3=int(t/10000000)
    li.append(d3)
    t=t%10000000
    d4=int(t/1000000)
    li.append(d4)
    if d2*d3*d4%2==0:
        t=t%1000000
        d5=int(t/100000)
        li.append(d5)
        if d3*d4*d5%3==0:
            t=t%100000
            d6=int(t/10000)
            li.append(d6)
            if d4*d5*d6%5==0:
                t=t%10000
                d7=int(t/1000)
                li.append(d7)
                if d5*d6*d7%7==0:
                    t=t%1000
                    d8=int(t/100)
                    li.append(d8)
                    if d6*d7*d8%11==0:
                        t=t%100
                        d9=int(t/10)
                        li.append(d9)
                        if d7*d8*d9%13==0:
                            t=t%10
                            d10=t
                            li.append(d10)
                            if d8*d9*d10%17==0 and set(li)==set(list1b): 
                                s=s+n
                                print(n)
                            reset()
print(s) 
