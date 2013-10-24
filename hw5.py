#!/usr/bin/env python
import sys, os
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import depth_first_search

with open("wordlst.txt") as file:
  words = file.readlines()
file.close()

graph      = digraph()
alphagrams = []



for word in words:
  alphagrams.append(''.join(sorted(word.rstrip('\n'))))

alphagrams = sorted(set(alphagrams))
graph.add_nodes(alphagrams)

lol = [ [],[],[],[],[],[],[],[],[],[],[],[],[],[] ] # at index n is a list of all n-letter alphagrams

for ag in alphagrams:
  letters = len(ag)
  lol[letters - 2].append(ag)

for n in range(2,15):
  for ag in lol[n - 2]:
    for ag2 in lol[n - 1]:
      if ag2.startswith(ag):
        graph.add_edge((ag,ag2))

# print graph
