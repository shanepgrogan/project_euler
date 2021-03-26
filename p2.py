# Problem 2

def fib(n):
	if n < 2:
		return n
	else:
		return fib(n-1) + fib(n-2)

s = 0
n = 0
f = fib(n)
while(f<4000000):	
	if f%2 == 0:
		s += f
	n += 1
	f = fib(n)
print(s)
