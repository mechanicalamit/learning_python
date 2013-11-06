"""Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal."""

t=0
p=0
h=0
n=1
m=1
l=1
a=[]
b=[]
c=[]
for n in range(1,500000):
    t=n*(n+1)/2
    a.append(t)
for l in range(1,500000):
    p=l*(3*l-1)/2
    b.append(p)
for m in range(1,500000):
    h=m*(2*m-1)
    c.append(h)
    
print(list(set(a) & set(b) & set(c)))
