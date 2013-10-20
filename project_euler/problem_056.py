"""A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?"""
a=1
b=1    
temp=0
y=0
def reset():
    global temp
    temp=0
import math
for a in range (1,100):
    for b in range (1,100):
        st=str(a**b)
        for i in st:
            temp=temp+int(i)
            if temp>y:
                y=temp
        reset()
print('max is', y)
