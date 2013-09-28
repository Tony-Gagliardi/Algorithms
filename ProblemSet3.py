#!/usr/bin/env python

# ProblemSet3.py
# Anthony Gagliardi <anthony.gagliardi@colorado.edu>
# Last Modified: 26 September 2013
# This file contains solutions for problems 3-5 on PS3

import random
import math
import sys

# Problem 3: Pseudoprime finder
def PseudoprimeFinder(primes):
    
    # Define a variable for the length
	primeLength = len(primes)

    # Accumulater storage variable
	j = 1

	while True:
		j += 1
		# size check initially set to 0
		s = 0
		for i in primes:
			s += 1
			if pow(j, i - 1, i) == 1:
				if s == primeLength:
					s += 1
					return j
			else:
				break

print PseudoprimeFinder([2,3,2013])

# Problem 4: getrand and nextprime
def getrand100():
	n = 100
	return random.randint(10**(n- 1), ((10**n) - 1))

def nextprime(i):
	# if given number is even, increment by 1
	if i % 2 == 0: i += 1
	# iterator
	j = 0
	while j < 100:
		generateRand = random.randint(1, i)
		# if our random number ^ i mod i != our random number mod i
		if (pow(generateRand,i,i)) != (generateRand % i):
			i += 2
			j = 0
		else:
			j += 1
	return i

print nextprime(2013**50) #=> 1556642001415450885363011926342364892322591839000398286585785855871067460392965421912430859681416618309437233804422680987742255926821108997052133833582998914043034313

# Problem 5: Average prime distance
def avgPrimeDistance(sampleNum):
	acc = 0
	for i in range(0, sampleNum):
		a = getrand100()
		acc += nextprime(a)

	return acc / sampleNum

print avgPrimeDistance(1000) #=> 5582562250125072648260788339340093111149791409574158708086450320531153640605042158706765385253105767


