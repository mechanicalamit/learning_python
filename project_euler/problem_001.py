

def ismultiple3or5(i):
	"This functino returns true if a number is a multiple of 3 or 5"
	if (i % 5 == 0 or i % 3 == 0):
		return True
	else:
		return False

sum = 0 # variable to hold sum
for i in range(1000): # range(1000) = [0,999]
	if ismultiple3or5(i):
		sum += i

print(sum)
