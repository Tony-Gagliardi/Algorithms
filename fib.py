#/usr/bin/env python

def fib(n):
	Memo = {0: 0, 1: 1} # Memoization dictionary for base cases
	def fib2(n):
		if n not in Memo:
			Memo[n] = fib2(n-2) + fib2(n-1) # Fib sequence arithmetic
		return Memo[n]
	return fib2(n)
print fib(200) # Calculate and print out Fib sequence of 200
