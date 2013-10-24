#!/usr/bin/env python

# ProblemSet4.py
# Anthony Gagliardi <anthony.gagliardi@colorado.edu>
# Last Modified: 3 October 2013
# This file contains solutions for problems 5-6

import sys
import os
import random


# Problem #6: Find the median of the given word list
with open("wordlst.txt") as file:
  wordlst = file.readlines()

# Here we use a simple sort algorithm to figure out what the true median
# is, that way we know if our selection algrithm is working correctly
sort = sorted(wordlst)
print sort[ len(sort) / 2]


def partition(wordlst):
	# Establishing arrays for each partition
  greater = []
  equal = []
  less = []

  pivot = random.choice(wordlst)
  for word in wordlst:
    if cmp(word, pivot) > 0:
      less.append(word)
    elif cmp(word, pivot) < 0:
      greater.append(word)
    else:
      equal.append(word)
      # Concatenating our 3 new arrays together
  partitioned = less + equal + greater
  
  # return a tuple of our index and the partitioned array
  return partitioned.index(pivot), partitioned
	
def findMedianWord(wordlst):
  pivotIndex, partitioned = partition(wordlst)
  
  # If there is only one element remaining, that is our median
  if len(partitioned) == 1:
    return partitioned[0]

  # If randomly chosen pivot is not in middle 50% -- "Good Section" -- partition again
  while True:
    if pivotIndex < len(partitioned) / 4 or pivotIndex > 3 * len(partitioned) / 4:
      pivotIndex, partitioned = partition(wordlst)
    else:
      break
  
  # If pivot is on the left portion of the good section, throw away all lesser words
  # and run again. If it's on the right portion of the good section, throw away all the
  # greater words.
  if pivotIndex < len(partitioned) / 2:
    return findMedianWord(wordlst[pivotIndex:])
  else:
    return findMedianWord(wordlst[:pivotIndex])

print findMedianWord(wordlst)
